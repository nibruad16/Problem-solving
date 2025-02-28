# Problem: B - Kidus Couldn't Sleep - https://codeforces.com/gym/589822/problem/B

n , m = [int(i) for i in input().split()]

nums=  [int(i) for i in input().split()]


prefix_sum = [0]
for i in range(n):
    prefix_sum.append(prefix_sum[-1] + nums[i])
sum_ = 0
j = 0
for i in range(m, n+1):
    sum_+=(prefix_sum[i]-prefix_sum[j])
    j+=1
print(sum_/(n-m+1))