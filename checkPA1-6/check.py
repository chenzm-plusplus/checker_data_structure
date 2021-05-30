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


def dataMakerForStart(inputFile,st):
    with open(inputFile, "w")as f:
        for datanum in range(st):
            c=str(random.randint(0,9))
            f.write(c)
        f.write("\n")

def dataMakerForInsert(inputFile, n):
    """

    :param inputFile:
    :param n: 数据的组数
    :return:
    """
    with open(inputFile, "a")as f:
  #      f.write(str(n)+"\n")
        for datanum in range(n):
            f.write("I ")
            i = random.randint(0,1)
            if i==0:
                f.write("L ")
            else:
                f.write("R ")
            c = str(random.randint(0,9))
            f.write(c)
            f.write("\n")


def dataMakerForMove(inputFile,n):
    with open(inputFile, "a")as f:
#        f.write(str(n) + "\n")
        for datanum in range(n):
            i = random.randint(0, 1)
            if i == 0:
                f.write("< ")
            else:
                f.write("> ")
            i = random.randint(0, 1)
            if i==0:
                f.write("L")
            else:
                f.write("R")
            f.write("\n")


def dataMakerForSpecialMove(inputFile,n):
    with open(inputFile, "a")as f:
#        f.write(str(n)+"\n")
        for datanum in range(n):
            f.write("< ")
            f.write("L")
            f.write("\n")


def dataMakerForReverse(inputFile,n):
    with open(inputFile, "a")as f:
        for datanum in range(n):
            f.write("R"+"\n")


def dataMakerForDelete(inputFile,n):
    with open(inputFile, "a")as f:
        for datanum in range(n):
            f.write("D ")
            i = random.randint(0, 1)
            if i == 0:
                f.write("L\n")
            else:
                f.write("R\n")


def dataMakerForShow(inputFile,n):
    with open(inputFile, "a")as f:
        for datanum in range(n):
            f.write("S\n")


def dataMaker(inputFile,n,startlength):
    dataMakerForStart(inputFile,startlength)
    with open(inputFile, "a")as f:
        f.write(str(n)+"\n")
    for cnt in range(n-1):
        i=random.randint(0,3)
        if i==0 :
            dataMakerForMove(inputFile,1)
        elif i==1:
            dataMakerForInsert(inputFile,1)
        elif i==2:
            dataMakerForReverse(inputFile,1)
        elif i==3:
            dataMakerForDelete(inputFile,1)
    dataMakerForShow(inputFile,1)


if __name__=='__main__':
    while True:
        # 每组数据10个，长度为10
#        dataMaker("input.txt",4000000,3200000)
        # 运行a读入input.txt输出到output1.txt,a.cpp是c++代码需要编译之后得到可执行程序a
#        t0 = time.clock()
        ta = time.time()
        os.system("./PA1_6 < input000000.txt >output000000.txt")
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
