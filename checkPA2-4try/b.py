n = int(input())
lis = []
limit = int(input())
for itr in range(n):
    a = input()
    a = int(a)
    lis.append(a)
lis.sort()
for itr in range(n):
    print(lis[itr])
print("Accepted")