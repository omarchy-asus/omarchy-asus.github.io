import json, sys
from pathlib import Path
g = Path(sys.argv[1])
t = (g / "template.html").read_text(encoding="utf-8")
t = t.replace("{{WORDMARK}}", (g / "wordmark.svg").read_text(encoding="utf-8").strip())
for k, v in json.loads((g / "charts.json").read_text(encoding="utf-8")).items():
    t = t.replace("{{" + k + "}}", v)
if "{{" in t:
    sys.exit("build.py: unresolved {{...}} placeholder in the template")
Path(sys.argv[2]).write_text(t, encoding="utf-8")
