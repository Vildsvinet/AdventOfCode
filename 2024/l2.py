# Advent of Code, 2024, day 2
def is_safe(rpt: list) -> bool:
    asc = -1 # -1=not set; 1=asc 0=desc
    for i in range(len(rpt)-1):
        d = rpt[i] - rpt[i+1]
        if abs(d) > 3 or d == 0 or (asc == 1 and d > 0) or (asc == 0 and d < 0):
            return False
        asc = 1 if d < 0 else 0
    return True

def is_safe2(rpt: list) -> bool:
    if is_safe(rpt): return True
    for i in range(len(rpt)):
        if is_safe(rpt[:i] + rpt[i+1:]): return True
    return False

with open("i2.txt", 'r') as inp:
    safe_reports = 0
    for report in inp:
        if is_safe2(list(map(int,report.split()))): safe_reports += 1

    print(safe_reports)
