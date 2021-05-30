import os
import random
import time


def checkAns(outputFile1, outputFile2):
    """
        该函数用于判断两个输入文件是否相同，这里采用的方式是读入两个文件的所有行，然后拼起来判断是否相同。可以根据需求修改
        outputFile1,outputFile2 分别为判断的两个文件的文件名
        函数返回布尔值
    """
    with open(outputFile1, "r") as f:
        output1 = f.readlines()
    with open(outputFile2, "r") as f:
        output2 = f.readlines()
    return "".join(output1) == "".join(output2)



def dataMaker(inputFile,n,startlength):
    with open(inputFile, "w")as f:
        f.write(str(n)+"\n")
        i,j=0,0
        for datanum in range(0,n*2):
            k=random.randint(0,1)
            s=int(2147483000/(2*n))
            t=4
            if j<i and i<n:
                if k==0:
                    i+=1
                    f.write(str(random.randint(0,t))+" "+str(random.randint(0,5000))+"\n")
                elif k==1:
                    j+=1
                    f.write(str(random.randint(0,t))+"\n")
            elif i==j:
                i += 1
                f.write(str(random.randint(0, t)) + " " + str(random.randint(0, 5000)) + "\n")
            elif i==n:
                j += 1
                f.write(str(random.randint(0, t)) + "\n")





if __name__=='__main__':
    while True:
        # 每组数据10个，长度为10
#        dataMaker("input.txt",4,3)
        # 运行a读入input.txt输出到output1.txt,a.cpp是c++代码需要编译之后得到可执行程序a
#        t0 = time.clock()
        ta = time.time()
        os.system("./PA1_4 < input.txt >output.txt")
#        t1 = time.clock()
        tb = time.time()
        print("right")
        print(tb - ta)
        os.system("./pa1_6_test < input.txt >output2.txt")
#        break
        # 运行b读入input.txt输出到output1.txt,b.py是python代码通过python指令运行
#        os.system("python3 b.py < input.txt >output2.txt")
#        t2 = time.clock()
#        tc = time.time()

        if checkAns("output.txt", "output2.txt") is False:
            print("Wrong")
            break

