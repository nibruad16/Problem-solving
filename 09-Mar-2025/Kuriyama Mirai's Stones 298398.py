# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())
nums = list(map(int,input().split()))
m = int(input())
ans = []
for _ in range(m):
    num = list(map(int,input().split()))
    ans.append(num)
num1 = nums.copy()
num1.sort()
for i in range(1,len(nums)):
    nums[i]+= nums[i-1]
    num1[i]+= num1[i-1]
for types, l, r in ans:
    if types ==2:
        if l-1>0:
            print(num1[r-1]-num1[l-2])
        else:
            print(num1[r-1])
    else:
        if l-1>0:
            print(nums[r-1]-nums[l-2])
        else:
            print(nums[r-1])
