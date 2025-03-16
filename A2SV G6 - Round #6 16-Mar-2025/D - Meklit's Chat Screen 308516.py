# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import deque
n, k = map(int, input().split())
nums = list(map(int, input().split()))

ans = deque()
seen = set()

for num in nums:
    if num in seen:
        continue 
    
    if len(ans) == k:
        temp = ans.pop()
        seen.remove(temp)

    ans.appendleft(num)
    seen.add(num)

print(len(ans))
print(*ans)
