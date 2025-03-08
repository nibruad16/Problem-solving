# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    count = Counter(arr)

    values = list(count.values())
    values.sort()

    min_deletions = float('inf')
    
    for i in range(len(values)):

        deletions = n - (len(values) - i) * values[i]
        min_deletions = min(min_deletions, deletions)
    
    print(min_deletions)