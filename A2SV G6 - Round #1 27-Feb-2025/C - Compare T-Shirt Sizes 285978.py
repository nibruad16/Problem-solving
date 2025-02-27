# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

x = int(input())

for i in range(x):
    s1 ,s2 = map(str , input().split())
    if s1[-1] == "M" and s2[-1] == "S":
        print(">")
    elif s1[-1] == "S" and s2[-1] == "M":
        print("<")
    elif s1[-1] == "L" and s2[-1] == "M":
        print(">")
    elif  s1[-1] == "M" and s2[-1] == "L":
        print("<")
    elif s1[-1] == "M" and s2[-1] == "M":
        print("=")
    elif s1[-1] == "S" and s2[-1] == "L":
        print("<")
    elif s1[-1] == "L" and s2[-1] == "S":
        print(">")
    elif s1[-1] == "S" and s2[-1] == "S":
        s1c = s1.count("X")
        s2c = s2.count("X")
        
        if s1c > s2c:
            print("<")
        elif s1c < s2c:
            print(">")
        else:
            print("=")
    else:
        s1[-1] == "L" and s2[-1] == "L"
        s1c = s1.count("X")
        s2c = s2.count("X")
        
        if s1c > s2c:
            print(">")
        elif s1c < s2c:
            print("<")
        else:
            print("=")
    