import time
import os


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


if __name__=='__main__':
    while True:
        # 每组数据10个，长度为10
#        print("have made")
        # 运行a读入input.txt输出到output1.txt,a.cpp是c++代码需要编译之后得到可执行程序a
#        t0 = time.clock()
        ta = time.time()
        os.system("./PA2_3 < input.txt >output1.txt")
#        t1 = time.clock()
        tb = time.time()
        print(tb - ta)
        print("right")
        # 运行b读入input.txt输出到output1.txt,b.py是python代码通过python指令运行
#        os.system("python3 c.py < input.txt >output2.txt")
#        t2 = time.clock()
#        tc = time.time()

        if checkAns("output1.txt", "output2.txt") is False:
            print("Wrong")
            break

#        print("right")