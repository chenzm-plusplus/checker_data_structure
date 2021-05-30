#test of merge
n = int(input())
cal = 1
list=[]
for itr in range(n):
    list.append(int(input()))
list.sort()
#print(list)
for itr in range(n-1):
    s1 = min(list)
    list.remove(s1)
    s2 = min(list)
    list.remove(s2)
    list.append(s1*s2)
    cal *= s1
    cal *= s2
#    print(list)
#    print(cal)
print(cal)
