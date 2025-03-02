# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

x = int(input())
for _ in range(x):
    n = int(input())
    r = [int(i) for i  in input().split()]
    m = int(input())
    b = [int(i) for i  in input().split()]

    presum = []
    cum = []
   

    presum.append(r[0])
    for i in range(1,len(r)):
        presum.append(presum[i-1]+r[i])
    presum.append(0)

    cum.append(b[0])
    for i in range(1,len(b)):
        cum.append(cum[i-1]+b[i])
    cum.append(0)

    print(max(cum) + max(presum))
        
    
