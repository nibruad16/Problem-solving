x = int(input())
for _ in range(x):
    y = int(input())
    lst = [int(i) for i in input().split()]
    pos=[]
    neg=[]
    c=0
    for i in range(x):
        if lst[i]<0:
            neg.append(lst[i])
            if pos!=[]:
                c+=max(pos)
                pos=[]
        if lst[i]>0:
            pos.append(lst[i])
            if neg!=[]:
                c+=max(neg)
                neg=[]
    if pos==[]:
        c+=max(neg)
    else:
        c+=max(pos)
    print(c)
    
