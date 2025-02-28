# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

new = int(input())
for _ in range(new):
    a,b = map(int,input().split())
    arr = [int(i) for i in input().split()]
    arr.sort()
    first = arr[:a]
    sec = arr[a:]

    Flag = True
    for i in range(len(first)):
        if sec[i] - first[i] < b:
            Flag = False
    if Flag:
        print("YES")
    else:
        print("NO")