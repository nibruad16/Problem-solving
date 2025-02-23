# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

def solve():
    n, k, q = map(int, input().split())
    recipes = []
    for _ in range(n):
        recipes.append(list(map(int, input().split())))

    diff = [0] * 200002
    for l, r in recipes:
        diff[l] += 1
        diff[r + 1] -= 1

    pref = [0] * 200002
    pref[0] = diff[0]
    for i in range(1, 200002):
        pref[i] = pref[i - 1] + diff[i]

    admissible = [0] * 200002
    for i in range(1, 200002):
        if pref[i] >= k:
            admissible[i] = 1

    admissible_pref = [0] * 200002
    for i in range(1, 200002):
        admissible_pref[i] = admissible_pref[i - 1] + admissible[i]

    for _ in range(q):
        a, b = map(int, input().split())
        print(admissible_pref[b] - admissible_pref[a - 1])

solve()