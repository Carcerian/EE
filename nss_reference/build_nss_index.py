#!/usr/bin/env python3
"""
build_nss_index.py
------------------
Generate a browsable reference index of NWScript functions and constants from a
tree of NWN:EE .nss include files.

For every selected include file it extracts, at FILE SCOPE only (brace depth 0):
  * function prototypes / definitions, with the leading // doc-comment block
  * constant declarations  (type NAME = value;  with optional trailing // note)

Outputs:
  <out>/README.md         master index (families -> files -> counts, links)
  <out>/<file>.md         per-file page (constants + functions, with docs)
  <out>/index.json        full machine-readable dump (for tooling / AI lookup)

Re-run whenever the source .nss files change; the index is fully regenerated.

Usage:
  python3 build_nss_index.py <NSS_ROOT> <OUT_DIR>
  # selection of "include files" is by name pattern (_i0_ / _inc_ / inc_ / nwscript)
  # restricted to base-game prefix families; edit SELECT / FAMILIES below to adjust.
"""
import os, re, sys, json, html
from pathlib import Path
from collections import defaultdict

NSS_ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("NSS")
OUT_DIR  = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("reference")

# Base-game prefix families we treat as "the includes". Edit to taste.
# Map a filename's leading token -> friendly family label (order = display order).
FAMILIES = [
    ("nwscript", "Core — nwscript.nss (engine functions & constants)"),
    ("nw",  "BioWare core (nw_*)"),
    ("x0",  "Expansion includes (x0_*)"),
    ("x1",  "Expansion includes (x1_*)"),
    ("x2",  "Expansion includes (x2_*)"),
    ("x3",  "Expansion includes (x3_*)"),
    ("xp1", "Expansion includes (xp1_*)"),
    ("xp2", "Expansion includes (xp2_*)"),
    ("inc", "Generic includes (inc_*)"),
]
FAMILY_PREFIXES = {p for p, _ in FAMILIES}

# A file is an "include" if its name looks like a library header.
INCLUDE_NAME = re.compile(r"(^nwscript$)|(_i0_)|(_inc_)|(^inc_)", re.I)

TYPES = (r"(?:void|int|float|string|object|vector|location|effect|itemproperty"
         r"|talent|action|event|json|sqlquery|cassowary|struct\s+\w+)")
SIG_START = re.compile(rf"^\s*({TYPES})\s+([A-Za-z_]\w*)\s*\(")
CONST_RE  = re.compile(rf"^\s*(?:const\s+)?({TYPES})\s+([A-Za-z_]\w*)\s*=\s*(.+?);\s*(?://\s*(.*))?$")
SKIP_FUNCS = {"main", "StartingConditional"}  # script entry points, not library API


def family_of(stem: str) -> str:
    tok = stem.split("_", 1)[0].lower()
    return tok if tok in FAMILY_PREFIXES else None


def parse_nss(path: Path):
    """Return (functions, constants) lists from file-scope declarations."""
    funcs, consts = [], []
    depth = 0
    doc = []                 # accumulated // doc lines (contiguous, above a decl)
    in_block = False
    sig_buf = None           # accumulating a (possibly multi-line) signature
    paren = 0

    text = path.read_text(encoding="utf-8", errors="replace").splitlines()
    for raw in text:
        line = raw.rstrip("\n")

        # ---- block comments /* ... */ (coarse) ----
        if in_block:
            if "*/" in line:
                in_block = False
                line = line.split("*/", 1)[1]
            else:
                continue
        # strip inline /* ... */ on one line
        while "/*" in line and "*/" in line:
            a, b = line.index("/*"), line.index("*/")
            if a < b:
                line = line[:a] + line[b + 2:]
            else:
                break
        if "/*" in line:
            in_block = True
            line = line.split("/*", 1)[0]

        stripped = line.strip()

        # ---- if we are mid-signature, keep accumulating ----
        if sig_buf is not None:
            sig_buf += " " + stripped
            paren += stripped.count("(") - stripped.count(")")
            if paren <= 0:
                _finish_sig(sig_buf, funcs, doc)
                # detect prototype vs definition by trailing char
                tail = sig_buf[sig_buf.rindex(")") + 1:].strip()
                sig_buf = None
                doc = []
                if tail.startswith("{"):
                    depth += 1  # entering a body
                depth += line.count("{") - line.count("}") if False else 0
            continue

        # ---- only collect declarations at file scope ----
        if depth == 0:
            if stripped.startswith("//"):
                doc.append(stripped[2:].strip())
                # do not reset depth tracking
                continue
            if stripped == "":
                doc = []  # blank line breaks the doc-block association
                continue

            m = SIG_START.match(line)
            if m:
                sig_buf = stripped
                paren = stripped.count("(") - stripped.count(")")
                if paren <= 0:
                    tail = stripped[stripped.rindex(")") + 1:].strip()
                    _finish_sig(stripped, funcs, doc)
                    sig_buf = None
                    doc = []
                    if tail.startswith("{"):
                        depth += 1
                continue

            c = CONST_RE.match(line)
            if c:
                ctype, cname, cval, cnote = c.group(1), c.group(2), c.group(3).strip(), (c.group(4) or "").strip()
                consts.append({"name": cname, "type": ctype, "value": cval, "note": cnote})
                doc = []
                continue

            # some other file-scope token
            doc = []

        # ---- maintain brace depth for everything else ----
        depth += line.count("{") - line.count("}")
        if depth < 0:
            depth = 0
    return funcs, consts


def _finish_sig(sig_text, funcs, doc):
    """Parse an accumulated signature string into return type / name / params."""
    sig = sig_text
    # cut at first ) that closes the param list
    if "(" not in sig or ")" not in sig:
        return
    name_part = sig[:sig.index("(")]
    params = sig[sig.index("(") + 1: sig.rindex(")")].strip()
    m = SIG_START.match(sig)
    if not m:
        return
    rettype, fname = m.group(1).strip(), m.group(2).strip()
    if fname in SKIP_FUNCS:
        return
    # normalize signature for display
    disp = f"{rettype} {fname}({_norm_params(params)})"
    funcs.append({
        "name": fname,
        "ret": rettype,
        "params": _norm_params(params),
        "signature": disp,
        "doc": _clean_doc(doc),
    })


def _clean_doc(lines):
    """Drop ASCII-art banner lines and tidy leading punctuation runs."""
    out = []
    for d in lines:
        s = d.strip()
        if not s:
            continue
        compact = s.replace(" ", "")
        if not compact:
            continue
        alnum = sum(ch.isalnum() for ch in compact)
        # banner/separator line (mostly // :: == -- ** ) -> skip
        if alnum / len(compact) < 0.35:
            continue
        s = s.lstrip(":/* ").rstrip()        # strip leading banner punctuation
        if s:
            out.append(s)
    return out


def _norm_params(p):
    p = re.sub(r"\s+", " ", p).strip()
    p = re.sub(r"\s*,\s*", ", ", p)
    p = re.sub(r"\s*=\s*", " = ", p)
    return p


def md_escape(s):
    return s.replace("|", "\\|")


def write_file_page(out_dir, stem, src_rel, funcs, consts):
    lines = [f"# `{stem}.nss`", "", f"Source: `{src_rel}`  ",
             f"{len(funcs)} functions · {len(consts)} constants", ""]
    if consts:
        lines += ["## Constants", "", "| Constant | Type | Value | Note |", "|---|---|---|---|"]
        for c in consts:
            lines.append(f"| `{md_escape(c['name'])}` | {c['type']} | `{md_escape(c['value'])}` | {md_escape(c['note'])} |")
        lines.append("")
    if funcs:
        lines += ["## Functions", ""]
        for f in funcs:
            lines.append(f"#### `{f['signature']}`")
            if f["doc"]:
                # join doc lines as a blockquote
                for d in f["doc"]:
                    lines.append(f"> {d}")
            lines.append("")
    (out_dir / f"{stem}.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    if not NSS_ROOT.exists():
        sys.exit(f"NSS root not found: {NSS_ROOT}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # gather include files
    selected = []
    for p in NSS_ROOT.rglob("*.nss"):
        stem = p.stem
        if not INCLUDE_NAME.search(stem):
            continue
        if family_of(stem) is None:
            continue
        funcs, consts = parse_nss(p)
        if not funcs and not consts:
            continue
        selected.append((stem, p.relative_to(NSS_ROOT.parent).as_posix(), funcs, consts))

    selected.sort(key=lambda x: (x[0] != "nwscript", x[0]))  # nwscript first, then alpha

    # group by family
    by_family = defaultdict(list)
    for stem, rel, funcs, consts in selected:
        by_family[family_of(stem)].append((stem, rel, funcs, consts))

    full = {}
    for stem, rel, funcs, consts in selected:
        write_file_page(OUT_DIR, stem, rel, funcs, consts)
        full[stem] = {"source": rel, "functions": funcs, "constants": consts}

    (OUT_DIR / "index.json").write_text(json.dumps(full, indent=1), encoding="utf-8")

    # master README
    tot_f = sum(len(f) for _, _, f, _ in selected)
    tot_c = sum(len(c) for _, _, _, c in selected)
    R = ["# NWN:EE NSS Reference Index", "",
         f"Auto-generated from `{NSS_ROOT.as_posix()}` by `build_nss_index.py`.  ",
         f"**{len(selected)} include files · {tot_f} functions · {tot_c} constants**", "",
         "Regenerate after any source change:  `python3 build_nss_index.py NSS reference`", ""]
    for prefix, label in FAMILIES:
        fam = by_family.get(prefix)
        if not fam:
            continue
        R += [f"## {label}", "", "| File | Functions | Constants |", "|---|---:|---:|"]
        for stem, rel, funcs, consts in sorted(fam, key=lambda x: (x[0] != "nwscript", x[0])):
            R.append(f"| [`{stem}.nss`]({stem}.md) | {len(funcs)} | {len(consts)} |")
        R.append("")
    (OUT_DIR / "README.md").write_text("\n".join(R), encoding="utf-8")

    print(f"files indexed : {len(selected)}")
    print(f"functions     : {tot_f}")
    print(f"constants     : {tot_c}")
    print(f"output        : {OUT_DIR}/  (README.md, index.json, {len(selected)} pages)")


if __name__ == "__main__":
    main()
