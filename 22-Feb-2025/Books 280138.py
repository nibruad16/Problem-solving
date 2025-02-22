# Problem: Books - https://codeforces.com/contest/279/problem/B

def solve():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    max_books = 0
    left = 0
    current_time = 0

    for right in range(n):
        current_time += a[right]
        while current_time > t:
            current_time -= a[left]
            left += 1
        max_books = max(max_books, right - left + 1)

    print(max_books)

solve()