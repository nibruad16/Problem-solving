# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    left = 0
    max_len = 0
    best_l, best_r = 0, 0
    counts = {}

    for right in range(n):
        if a[right] not in counts:
            counts[a[right]] = 0
        counts[a[right]] += 1

        while len(counts) > k:
            counts[a[left]] -= 1
            if counts[a[left]] == 0:
                del counts[a[left]]
            left += 1

        if right - left + 1 > max_len:
            max_len = right - left + 1
            best_l, best_r = left + 1, right + 1

    print(best_l, best_r)

solve()