# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter
x = int(input())
for _ in range(x):
    y = int(input())
    s = input()
    set_ = set()
    track = Counter(s)
    ans = 0
    for i in range(y -1):
        char = s[i]

        set_.add(s[i])
        track[char] -= 1

        if track[char] == 0:
            del track[char]
        
        temp = len(set_) + len(track)
        ans = max(ans , temp)
    print(ans)



