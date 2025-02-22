# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

def solve():
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))

    def get_diagonals_sum(row, col):
        sum_val = grid[row][col]
        
    
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            sum_val += grid[r][c]
            r -= 1
            c -= 1
        
      
        r, c = row - 1, col + 1
        while r >= 0 and c < m:
            sum_val += grid[r][c]
            r -= 1
            c += 1
        
        
        r, c = row + 1, col - 1
        while r < n and c >= 0:
            sum_val += grid[r][c]
            r += 1
            c -= 1
        
    
        r, c = row + 1, col + 1
        while r < n and c < m:
            sum_val += grid[r][c]
            r += 1
            c += 1
        
        return sum_val

    max_sum = 0
    for i in range(n):
        for j in range(m):
            max_sum = max(max_sum, get_diagonals_sum(i, j))
    
    print(max_sum)
    

t = int(input())
for _ in range(t):
    solve()