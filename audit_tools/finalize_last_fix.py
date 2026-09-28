#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data/papers.json"
p=json.loads(DATA.read_text(encoding="utf-8"))
by={x["id"]:x for x in p["papers"]}
x=by["cell-line-bottleneck"]
x["code_url"]="https://github.com/wkr112344/VirtualCellWorkbench"
x["code_status"]="repository_linked"
x["code_sources"]=list(dict.fromkeys((x.get("code_sources") or [])+[
  "https://doi.org/10.64898/2026.08.10.743942",
  "https://github.com/wkr112344/VirtualCellWorkbench/blob/main/README.md"
]))
x["updated_at"]="2026-09-28"
DATA.write_text(json.dumps(p,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

report=ROOT/"docs/final-code-sweep-2026-09-28.md"
s=report.read_text(encoding="utf-8")
s=s.replace("| Code links | 205 | 214 |","| Code links | 205 | 215 |")
s=s.replace("| Documented paper↔code correspondence | 198 | 211 |","| Documented paper↔code correspondence | 198 | 212 |")
s=s.replace("| No established code link | 80 | 71 |","| No established code link | 80 | 70 |")
if "Cell Line Bottleneck → VirtualCellWorkbench" not in s:
    s=s.replace("- **BRIDGE → tracy666/BRIDGE** — repository identifies itself as the official implementation.\n",
                "- **BRIDGE → tracy666/BRIDGE** — repository identifies itself as the official implementation.\n- **Cell Line Bottleneck → VirtualCellWorkbench** — companion repository explicitly cites the exact bioRxiv paper and provides the reproduction toolkit.\n")
report.write_text(s,encoding="utf-8")

test=ROOT/"tests/test_code_metadata.py"
t=test.read_text(encoding="utf-8")
needle="            'bridge':('https://github.com/tracy666/BRIDGE','paper_linked'),\n"
if "cell-line-bottleneck" not in t:
    t=t.replace(needle, needle+"            'cell-line-bottleneck':('https://github.com/wkr112344/VirtualCellWorkbench','repository_linked'),\n")
test.write_text(t,encoding="utf-8")
