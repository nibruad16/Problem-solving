# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

def solve():
    s = input()
    t = input()
    p = input()

   
    s_ptr = 0
    t_ptr = 0
    while t_ptr < len(t) and s_ptr < len(s):
        if s[s_ptr] == t[t_ptr]:
            s_ptr += 1
        t_ptr += 1

    if s_ptr != len(s):
        print("NO")
        return

    p_counts = {}
    for char in p:
        p_counts[char] = p_counts.get(char, 0) + 1

    t_diff_counts = {}
    t_ptr = 0
    s_ptr = 0
    while t_ptr < len(t):
        if s_ptr < len(s) and s[s_ptr] == t[t_ptr]:
            s_ptr+=1
        else:
            t_diff_counts[t[t_ptr]] = t_diff_counts.get(t[t_ptr], 0) + 1
        t_ptr += 1

    for char, count in t_diff_counts.items():
        if p_counts.get(char, 0) < count:
            print("NO")
            return

    print("YES")

q = int(input())
for _ in range(q):
    solve()