# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mx = -1e11
    sum = 0
    check = True
    for i in range(n):
        if check:
            if a[i] < 0:
                if mx > -1e10:
                    sum += mx
                mx = -1e11
                check = False
        else:
            if a[i] > 0:
                if mx > -1e10:
                    sum += mx
                mx = -1e11
                check = True
        mx = max(a[i], mx)
    if mx > -1e10:
        sum += mx
    print(sum)
