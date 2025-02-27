# Problem: B - Square String? - https://codeforces.com/gym/585107/problem/B

x = int(input())
for i in range(x):
    s = input()

    if len(s) % 2 != 0:
        print("NO")
    elif s[:len(s)//2] == s[len(s)//2:]:
        print("YES")
    else:
        print("NO")