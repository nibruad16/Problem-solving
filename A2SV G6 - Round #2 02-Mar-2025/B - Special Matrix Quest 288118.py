# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

x = int(input())
matrix = []
for _ in range(x):
    nums = [int(i) for i in input().split()]
    matrix.append(nums)
ans = 0
mid = x // 2
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if row == col or row + col == x - 1 or row == mid or col == mid:
            ans += matrix[row][col]
print(ans)



