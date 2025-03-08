# Problem: I - The Odd Challenge - https://codeforces.com/gym/589822/problem/I

t = int(input())
    
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    
    total_sum = prefix[-1]
    results = []
    for _ in range(q):
        l, r, k = map(int, input().split())
        replaced_range_old_sum = prefix[r] - prefix[l - 1]
        replaced_range_new_sum = (r - l + 1) * k
        new_sum = total_sum - replaced_range_old_sum + replaced_range_new_sum
        
        if new_sum % 2 == 1:
            results.append("YES")
        else:
            results.append("NO")

    for i in results:
        print(i)