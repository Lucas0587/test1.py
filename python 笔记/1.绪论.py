import math,time,random
#绪论内容比较简单，就简要概述一下

#1、数值类型
def part_1():
    def type_num(a):
        print(a, " 的类型为：", type(a))
    type_num(1)
    type_num(2.00)
    type_num(12.3 + 4.5j)  # 复数的i用j表示
    type_num('a')
    print("")
#part_1()

#2、内置字符与函数
def part_2():
    # 2.1 绝对值运算  int取整
    print(5 + 6j, " 的模是", abs(5 + 6j), "\t取整后是", int(abs(5 + 6j)))  # 向下取整而不是四舍五入
    # 2.2 math.fsum
    print("0.1 + 0.2 + 0.3 = ", math.fsum([0.1, 0.2, 0.3]))
    # 2.3 format()
    print("π取两位小数是{:.2f},七位小数是{:.7f}".format(math.pi, math.pi))
    # 2.4 字符串
    str = "complex " * 3
    print("str为：", str, "\t其长度为：", len(str), "\t从第7个到第15个字符为：", str[6:14])
    print("str居中对齐：{0: ^40}".format(str), " & 右对齐：{0:>40}".format(str))
    # 2.5 文本进度条
    def jindutiao():
        scale = 10
        for i in range(1, scale + 1):
            print("-" * 9 * i, "*", "-" * (90 - 9 * i), "进度：{0:.0%}".format(i / 10))
            time.sleep(0.1)
    # jindutiao()
    print("")
#part_2()

#3、结构控制 函数
def part_3():
    #3.1 蒙曼卡罗法
    def CalPi():
        Dots=1000000
        hit=0
        for i in range(0,Dots):
            x,y=random.random(),random.random()
            distance=math.sqrt(x**2+y**2)
            if distance<=1:
                hit+=1
        pi=4*hit/Dots
        print("π的近似值为：{}".format(pi))
    #CalPi()
    #3.2
part_3()
