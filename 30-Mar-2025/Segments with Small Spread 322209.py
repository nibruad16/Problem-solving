# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

import sys
from collections import deque

def count_good_segments():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    max_deque = deque()
    min_deque = deque()
    left = 0
    result = 0
    
    for right in range(n):
        current = a[right]
        
       
        while max_deque and a[max_deque[-1]] <= current:
            max_deque.pop()
        max_deque.append(right)
        
    
        while min_deque and a[min_deque[-1]] >= current:
            min_deque.pop()
        min_deque.append(right)
        

        while a[max_deque[0]] - a[min_deque[0]] > k:
            left += 1
          
            while max_deque and max_deque[0] < left:
                max_deque.popleft()
            while min_deque and min_deque[0] < left:
                min_deque.popleft()
        
   
        result += right - left + 1
    
    print(result)

count_good_segments()