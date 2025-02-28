# Problem: A - Nth Digit in Sequence - https://codeforces.com/gym/588468/problem/A

new = int(input())
arr = [int(i) for i in range(1,1001)]
me = "".join(str(i) for i in arr)
print(me[new-1])
