#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
data_path=ROOT/"data/papers.json"
payload=json.loads(data_path.read_text(encoding="utf-8"))
by={p["id"]:p for p in payload["papers"]}
p=by["cell-line-bottleneck"]
p["code_url"]="https://github.com/wkr112344/VirtualCellWorkbench"
p["code_status"]="repository_linked"
p["code_sources"]=list(dict.fromkeys((p.get("code_sources") or [])+[
    "https://doi.org/10.64898/2026.08.10.743942",
    "https://github.com/wkr112344/VirtualCellWorkbench/blob/main/README.md",
]))
p["updated_at"]="2026-09-28"
data_path.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

report=ROOT/"docs/final-code-sweep-2026-09-28.md"
s=report.read_text(encoding="utf-8")
s=s.replace("| Code links | 205 | 214 |","| Code links | 205 | 215 |")
s=s.replace("| Documented paper↔code correspondence | 198 | 211 |","| Documented paper↔code correspondence | 198 | 212 |")
s=s.replace("| No established code link | 80 | 71 |","| No established code link | 80 | 70 |")
needle="- **BRIDGE → tracy666/BRIDGE** — repository identifies itself as the official implementation.\n"
line="- **Cell Line Bottleneck → VirtualCellWorkbench** — companion repository explicitly cites the exact 2026 bioRxiv paper and provides a reproduction toolkit.\n"
if line not in s:
    s=s.replace(needle,needle+line)
report.write_text(s,encoding="utf-8")

audit=ROOT/"docs/code-audit-2026-09-28.md"
s=audit.read_text(encoding="utf-8")
s=s.replace("214 code links, 211 documented correspondences, 3 project matches, and 71 records without an established code link",
            "215 code links, 212 documented correspondences, 3 project matches, and 70 records without an established code link")
audit.write_text(s,encoding="utf-8")

test=ROOT/"tests/test_code_metadata.py"
s=test.read_text(encoding="utf-8")
needle="            'bridge':('https://github.com/tracy666/BRIDGE','paper_linked'),\n"
line="            'cell-line-bottleneck':('https://github.com/wkr112344/VirtualCellWorkbench','repository_linked'),\n"
if line not in s:
    s=s.replace(needle,needle+line)
test.write_text(s,encoding="utf-8")
print("added verified VirtualCellWorkbench correspondence")
