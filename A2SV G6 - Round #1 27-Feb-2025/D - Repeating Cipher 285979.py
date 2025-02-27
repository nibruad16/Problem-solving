# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

x = int(input())
s = input()

l = 0
i = 1
ans = ""
while l < x:
    ans += s[l]
    l += i
    i += 1
print(ans)

