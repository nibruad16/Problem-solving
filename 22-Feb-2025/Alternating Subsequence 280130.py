# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    result = []
    i = 0
    while i < n:
        if a[i] > 0:
            max_val = a[i]
            while i < n and a[i] > 0:
                max_val = max(max_val, a[i])
                i += 1
            result.append(max_val)
        else:
            max_val = a[i]
            while i < n and a[i] < 0:
                max_val = max(max_val, a[i])
                i += 1
            result.append(max_val)

    print(sum(result))

t = int(input())
for _ in range(t):
    solve()