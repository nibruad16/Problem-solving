# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

n , m = [int(i) for i in input().split()]
array = []
for i in range(n):
    c, t= [int(i) for i in input().split()]
    array.append(c*t)
prefix_sum = [0]
for i in range(n):
    prefix_sum.append(prefix_sum[-1]+array[i])
moment = [int(i) for i in input().split()]
 
 
j = 1
i = 0
while i < m:
    if moment[i] <= prefix_sum[j]:
        print(j)
        i+=1
    else:
        j+=1
 