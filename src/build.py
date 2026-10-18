import json, sys
g = sys.argv[1]
t = open(f"{g}/template.html").read()
t = t.replace("{{WORDMARK}}", open(f"{g}/wordmark.svg").read().strip())
for k, v in json.load(open(f"{g}/charts.json")).items():
    t = t.replace("{{" + k + "}}", v)
assert "{{" not in t
open(sys.argv[2], "w").write(t)
