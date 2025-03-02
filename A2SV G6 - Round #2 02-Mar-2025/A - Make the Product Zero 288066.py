# Problem: A - Make the Product Zero - https://codeforces.com/gym/586960/problem/A

x = int(input())
arr = [int(i) for i in input().split()]

new = []

for i in arr:
    temp = abs(i)
    new.append(temp)
print(min(new))
