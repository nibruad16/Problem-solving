# Problem: C - Restoring to the Original - https://codeforces.com/gym/589822/problem/C

n = int(input())  
s = input()  
ones = s.count('n')  
zeros = s.count('z')  
print('1 ' * ones + '0 ' * zeros)