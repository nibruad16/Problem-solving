# Problem: C - Permutation Minimization - https://codeforces.com/gym/594077/problem/C

from collections import deque
x= int(input())
for _ in range(x):
    y = int(input())
    nums = [int(i) for i in input().split()]

    ans = deque()
    ans.append(nums[0])
    for i in range(1,len(nums)):
        
        right = ans[-1]
        left = ans[0]
        temp = nums[i]

        if temp < right and temp > left:
            ans.append(nums[i])
        elif temp >= right:
            ans.append(nums[i])
        else:
            ans.appendleft(nums[i])

    print(*ans)
        
        