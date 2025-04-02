# Problem: A - Free Ice Cream for the Kids - https://codeforces.com/gym/596141/problem/A

n,x = map(int, input().split())
temp = []
for _ in range(n):
    s = input()
    temp.append(s)
count = 0
me = x
for i in range(len(temp)):
    now = temp[i].split()
    
    first = now[0]
    last = int(now[-1])
    if first == "+":
         me += last
    
    if first == "-":
        if me - last < 0:
            count += 1
        else:
            me -= last     
print(me,count)
  

