# Problem: G - Evenly Spaced Letters - https://codeforces.com/gym/589822/problem/G

x = int(input())
for _ in range(x):
    s = input()
    s = sorted(s)
    print("".join(s))