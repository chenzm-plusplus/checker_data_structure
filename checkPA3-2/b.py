b = str(input())
print(b)
print(int(b))
for length in range(1,24):
    c = ''
    for len in range(1,length):
        print('')
string=''
for pw in range(0,31):
    string += str(1 << pw)+","
print(string)
print(1<<31)