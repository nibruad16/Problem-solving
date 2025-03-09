# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

t = int(input().strip())  

for _ in range(t):
    n, k = map(int, input().split())  
    a = list(map(int, input().split()))  
    b = list(map(int, input().split()))  

  
    indexed_a = sorted(enumerate(a), key=lambda x: x[1])  
    sorted_b = sorted(b)  

    answer = [0] * n  
    for i in range(n):
        index = indexed_a[i][0] 
        answer[index] = sorted_b[i]  

    print(" ".join(map(str, answer)))  