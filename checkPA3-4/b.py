n=int(input())
l=[]
l=input().split(' ')
for itr in range(n):
    l[itr] = int(l[itr])
l.sort()
for itr in range(n):
    print(l[itr])