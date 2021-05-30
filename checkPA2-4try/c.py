import random

lists = []

n = int(input())

for i in range(n):
    lists.append(i)
print(list)

for i in range(n-1, -1, -1):
    cnt = random.randint(0, i)
    lists.remove(lists[cnt])
    print(lists)