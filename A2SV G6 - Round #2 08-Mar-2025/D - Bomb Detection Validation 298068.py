# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

n, m = map(int, input().split())  
grid = []

for _ in range(n):
    row = input()
    grid.append(row)


directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def is_inbound(x, y):
   
    return 0 <= x < n and 0 <= y < m

def count_bombs(x, y):
   
    bomb_count = 0
    for dx, dy in directions:
        ni, nj = x + dx, y + dy
        if is_inbound(ni, nj) and grid[ni][nj] == '*':
            bomb_count += 1
            
    return bomb_count

valid = True  

for i in range(n):
    for j in range(m):
        if grid[i][j] == '*':
            continue 
        
        bomb_count = count_bombs(i, j)
        
        if grid[i][j] == '.': 
            if bomb_count > 0:
                valid = False
        else: 
            if int(grid[i][j]) != bomb_count:
                valid = False


print("YES" if valid else "NO")