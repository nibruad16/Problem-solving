# Problem: B - Nafargi's Binary Reduction Game - https://codeforces.com/gym/594077/problem/B

n = int(input())
s = input()

count = s.count('0')
temp = count * 2
result = abs(n-temp)
print(result)