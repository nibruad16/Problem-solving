# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

x,y = map(int,input().split())
arr = [int(i) for i in input().split()]

diff = []
for i in range(1,len(arr)):
    diff.append(arr[i] - arr[i-1])

diff.sort(reverse=True)

gap = arr[-1] - arr[0]

for i in range(y-1):
    gap -= diff[i]

print(gap)

