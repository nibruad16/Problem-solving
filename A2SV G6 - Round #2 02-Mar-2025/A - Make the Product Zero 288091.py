# Problem: A - Make the Product Zero - https://codeforces.com/gym/586960/problem/A

x = int(input())
nums = list(map(int,input().split()))
ans = []
for i in nums:
        ans.append(abs(i))
print(min(ans))