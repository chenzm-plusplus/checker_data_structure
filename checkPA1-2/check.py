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


def dataMaker(inputFile, n, valuelength):
    """
        这个函数根据自己的需求一定要修改，他负责根据读入的参数来生成一个测试文件inputFile。
        在A+B问题里面,n用来控制生成的数组组数，valuelength用来控制用于乘法的长度。
    """
    with open(inputFile, "w") as f:
        f.write(str(n) + "\n")
        for datanum in range(n):
            S1 = str(random.randint(1, 9))
            S2 = str(random.randint(1, 9))
            for itr in range(valuelength - 1):
                S1 += str(random.randint(0, 9))
                S2 += str(random.randint(0, 9))
            f.write(S1 + " " + S2 + "\n")


def dataMakerForSort(inputFile, n, valuelength):
#    r = random.randint(1,n)
    with open(inputFile, "w")as f:
        f.write(str(n)+"\n")
        li = []
        for cnt in range(2):
            for datanum in range(n):
                i = str(random.randint(1,2147483647))
                if li.count(i) == 0:
                    li.append(i)
                f.write(i+" ")
            f.write("\n")
        f.write(str(valuelength)+"\n")
        for cnt in range(valuelength):
            for data in range(2):
                i = str(random.randint(1,2147483647))
                f.write(i+" ")
            f.write("\n")


if __name__=='__main__':
    while True:
        # 每组数据10个，长度为10
#        dataMakerForSort("input.txt", 200000, 200000)

        # 运行a读入input.txt输出到output1.txt,a.cpp是c++代码需要编译之后得到可执行程序a
#        t0 = time.clock()
        ta = time.time()
        os.system("./PA1_2 < input.txt >output1.txt")
#        t1 = time.clock()
        tb = time.time()
        print("right")
        print(tb - ta)
        break
        # 运行b读入input.txt输出到output1.txt,b.py是python代码通过python指令运行
#        os.system("python3 b.py < input.txt >output2.txt")
#        t2 = time.clock()
#        tc = time.time()
"""
        if checkAns("output1.txt", "output2.txt") is False:
            print("Wrong")
            break
"""
