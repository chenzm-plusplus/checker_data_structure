n = int(input())
str1=str(input())
str2=str(input())
a, b = str1.split(" ",n-1),str2.split(" ",n-1)
c = []
d = []
for cnt in a:
    c.append(int(cnt))
for cnt in b:
    d.append(int(cnt))
c.append(0)
d.append(0)
c.sort()
d.sort()

"""for cnt in c:
    print(cnt)
for cnt in d:
    print(cnt)
"""

m=int(input())
for cnt in range(m):
    sa, sb = input().split(" ",1)
    ia=int(sa)
    ib=int(sb)
    t=0
    for data in range(len(c)):
        if ib*c[data]+ia*d[data]>=c[data]*d[data]:
            t=data
    print(t)