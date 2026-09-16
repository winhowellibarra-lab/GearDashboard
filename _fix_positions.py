import re
from pathlib import Path

p = Path(r"C:\Users\epurpora001\OneDrive - PwC\Desktop\GEAR DASHBOARD\index.html")
t = p.read_text(encoding="utf-8")
print("Exp Associate count:", t.count("Exp Associate"))
print("position Exp Associate:", t.count('"position":"Exp Associate"'))
positions = sorted(set(re.findall(r'"position":"([^"]+)"', t)))
print("unique positions:")
for m in positions:
    print(" ", m)
