import html
W = 32
PART = " ▏▎▍▌▋▊▉"
def bar(v, mx, w=W):
    x = max(0.0, v / mx * w)
    full = int(x); rem = int((x - full) * 8)
    s = "█" * full + (PART[rem] if rem and full < w else "")
    if not s: s = "▏"
    return s
def b(cls, s): return f'<span class="{cls}">{html.escape(s)}</span>'

def paired(rows, mx, lw, index=False):
    out = []
    for label, bv, av, fb, fa in rows:
        vb, va = (100, av / bv * 100) if index else (bv, av)
        sb, sa = bar(vb, mx), bar(va, mx)
        out.append(f"{label:<{lw}} " + b("bb", sb) + " " * (W - len(sb) + 1) + b("m", fb))
        out.append(f"{'':<{lw}} " + b("ba", sa) + " " * (W - len(sa) + 1) + fa)
        out.append("")
    return "\n".join(out[:-1])

def single(rows, mx, lw):
    out = []
    for label, v, f, cls in rows:
        s = bar(v, mx)
        out.append(f"{label:<{lw}} " + b(cls, s) + " " * (W - len(s) + 1) + f)
    return "\n".join(out)

def diverging(rows, lw, half=16, scale=1.0):
    out = []
    for label, v, cls, note in rows:
        n = abs(v) / scale * half
        full = int(round(n))
        if v < 0:
            left = " " * (half - full) + b(cls, "█" * full) if full else " " * (half - 1) + b(cls, "▕") if v else " " * half
            right = " " * half
        else:
            left = " " * half
            right = b(cls, "█" * full) + " " * (half - full) if full else " " * half
        val = "~0" if v == 0 else f"{v:+.2f}".replace("-", "−")
        out.append(f"{label:<{lw}} " + left + "│" + right + f" {val:>6}  " + b("m", note))
    axis = f"{'':<{lw}} " + f"{'−' + format(scale, 'g') + ' W':<{half}}" + "0" + f"{'+' + format(scale, 'g') + ' W':>{half}}"
    out.append(axis)
    return "\n".join(out)

charts = {}
charts["wake"] = single([
    ("stock 610/615", 13, "13 of 13 drops woke the RTX (20–25 s each)", "bb"),
    ("with #1299", 0, "0 of 3; suspended in 179/179 samples", "ba"),
], 13, 14)
charts["fans"] = paired([
    ("fan 1", 2200, 0, "2200 rpm", "0 rpm"),
    ("fan 2", 1800, 0, "1800 rpm", "0 rpm"),
    ("fan 3", 3800, 0, "3800 rpm", "0 rpm  (7 in rerun)"),
], 3800, 6)
charts["overhead"] = paired([
    ("power daemons, cpu", 2.4, 0.27, "2.4 % of a core", "0.27 %"),
    ("rog-power", 1.6, 0.25, "1.6 %", "0.25 %"),
    ("idle-power", 0.75, 0.002, "0.75 %", "0.002 %"),
    ("voxtype wakeups", 240, 39, "240/s", "39/s"),
    ("bar widget helper", 155, 18, "155 ms, 135 forks", "18 ms, 12 forks"),
    ("menu package check", 162, 5.5, "160–165 ms", "5–6 ms"),
    ("launcher gpu probe", 17000, 3, "woke the RTX ~17 s", "3 ms, no wake"),
], 100, 18, index=True)
charts["decode"] = single([
    ("software", 1.24, "1.24 s  (1.18–1.30 user)", "bb"),
    ("radeon vcn", 0.60, "0.60 s  (0.35–0.43 user + 0.21 sys)", "ba"),
], 1.24, 10)
charts["ppt"] = single([
    ("stock", 48.5, "48.5 W  limit ignored", "bb"),
    ("fan curve on", 25.0, "25.0 W  held flat (24.997–25.009)", "ba"),
], 48.5, 12)
charts["tweaks"] = diverging([
    ("epp power vs balance_power", -0.86, "ba", "shipped, 4/4 rounds"),
    ("quiet fans on battery", -0.79, "ba", "shipped, median of 4"),
    ("wi-fi power_save", -0.30, "bb", "too small"),
    ("core parking", -0.15, "bb", "too small"),
    ("irq steering", -0.13, "bb", "too small"),
    ("windows-style freq caps", -0.05, "bb", "too small"),
    ("pci runtime pm / aspm", 0.0, "bb", "noise"),
    ("teo idle governor", 0.35, "bc", "worse, rejected"),
], 26)
import json, sys
json.dump(charts, open(sys.argv[1], "w"))
for k, v in charts.items():
    import re; print(k); print(re.sub("<[^>]+>", "", html.unescape(v))); print()
