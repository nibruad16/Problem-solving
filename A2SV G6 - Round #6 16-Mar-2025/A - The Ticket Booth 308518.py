# Problem: A - The Ticket Booth - https://codeforces.com/gym/594077/problem/A


n, s = map(int,input().split())


result = (s + n - 1) // n


print(result)
