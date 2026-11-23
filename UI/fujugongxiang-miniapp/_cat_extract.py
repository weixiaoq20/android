# -*- coding: utf-8 -*-
from pathlib import Path
import json
t = Path("category.html").read_text(encoding="utf-8")
start = t.find("const DATA=")
brace = t.find("{", start)
depth = 0
end = None
for i, ch in enumerate(t[brace:], brace):
    if ch == "{":
        depth += 1
    elif ch == "}":
        depth -= 1
        if depth == 0:
            end = i + 1
            break
raw = t[brace:end]
data = json.loads(raw)
out = []
for c in data["categories"]:
    out.append({
        "level1": c["level1"],
        "level2": [{"key": x["key"], "name": x["name"]} for x in c["level2"]],
    })
Path("_cats.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print("categories", len(out))
for c in out:
    print(c["level1"], ":", ", ".join(x["name"] for x in c["level2"]))
