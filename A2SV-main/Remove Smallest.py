import sys
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print("YES")
        continue

    a.sort()
    v = []
    dif = 0
    for i in range(1, n):
        dif = abs(a[i] - a[i-1])
        v.append(dif)

    v.sort(reverse=True)

    if v[0] > 1:
        print("NO")
    else:
        print("YES")
