# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F

import sys
from collections import defaultdict

n = int(sys.stdin.readline().strip())
events = defaultdict(int)

for _ in range(n):
    l, r = map(int, sys.stdin.readline().split())
    events[l] += 1
    events[r + 1] -= 1

keys = sorted(events.keys())
coverage = 0
prev = keys[0]
result = defaultdict(int)


for point in keys:
    result[coverage] += point - prev
    coverage += events[point]
    prev = point


ans = [result[k] for k in range(1, n + 1)]
print(*ans)