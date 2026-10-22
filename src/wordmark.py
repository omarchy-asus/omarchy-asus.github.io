# 5x7 wordmark drawn as an LED dot matrix, like the Slash strip on the G16 lid.
# Every cell is a dot; lit dots carry a sweep index (--d) for the one-time load animation.
F = {
 "O": ["01110","11011","11011","11011","11011","11011","01110"],
 "M": ["11011","11111","11111","10101","10001","10001","10001"],
 "A": ["01110","11011","11011","11111","11011","11011","11011"],
 "R": ["11110","11011","11011","11110","11100","11110","11011"],
 "C": ["01111","11000","11000","11000","11000","11000","01111"],
 "H": ["11011","11011","11011","11111","11011","11011","11011"],
 "Y": ["11011","11011","11011","01110","00100","00100","00100"],
 "S": ["01111","11000","11000","01110","00011","00011","11110"],
 "U": ["11011","11011","11011","11011","11011","11011","01110"],
 "-": ["00000","00000","00000","01110","00000","00000","00000"],
}
def word(s, x0, cls):
    d = []; x = x0
    for ch in s:
        for r, row in enumerate(F[ch]):
            for c, bit in enumerate(row):
                if bit == "1":
                    d.append(f'<circle class="on {cls}" style="--d:{x + c + 6 - r}" cx="{x+c}" cy="{r}" r=".4"/>')
                else:
                    d.append(f'<circle cx="{x+c}" cy="{r}" r=".4"/>')
        x += 6
    return "".join(d), x
a, x = word("OMARCHY", 0, "wm-a")
b, x2 = word("-", x, "wm-a")
c, x3 = word("ASUS", x2, "wm-b")
w = x3 - 1
print(f'<svg class="wordmark" viewBox="-0.5 -0.5 {w} 7" role="img" aria-label="omarchy-asus">{a}{b}{c}</svg>')
