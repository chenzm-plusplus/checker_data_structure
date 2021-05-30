#n = int(input())
#k = int(input())
lists = []
n,k= input().split(" ")
n=int(n)
k=int(k)

for itr in range(n):
    a = input()
    a = int(a)
    lists.append(a)

#print(lists)
for itr in range(n):
    maxx=0
    st=itr
    for itrs in range(k+2):
        if itr+itrs < n:
            if maxx < (lists[itr] ^ lists[itr+itrs]):
#                print("max1 itr itrs",lists[itr] ^ lists[itrs],itr,itrs)
                maxx = lists[itr] ^ lists[itr+itrs]
                st=itr+itrs
        if itr-itrs >= 0:
            if maxx <= (lists[itr] ^ lists[itr-itrs]):
#                print("max2 ",lists[itr] ^ lists[itrs],itr,itrs)
                maxx = lists[itr] ^ lists[itr-itrs]
                st=itr-itrs
    #print(maxx,st)
    print(st)