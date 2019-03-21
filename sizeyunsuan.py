from fractions import Fraction
import random


class tree():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def chushihua(a):         #初始化这棵树
    if a.left == None and a.right == None:  # 控制分数出现几率，当前为0.3
        p = random.uniform(0, 1)
        if p < 0.7:
            a.data = Fraction(random.randint(1, 100), 1)  # 整数转化为分数形式
        else:
            a1=random.randint(1,10)
            a2=random.randint(1,10)
            if(a1>a2):
                a.data=Fraction(a2,a1)
            else:
                a.data=Fraction(a1,a2)

    else:
        if a.data == 0:
            a.data = "+"
        elif a.data == 1:
            a.data = "-"
            #if(a.left.data<a.rigth.data):
              # a.left.data , a.right.data = a.right.data , a.left.data 
            k = Fraction(1, 1)
            if a.left.data < a.right.data and type(a.left.data) != type(k) and type(a.right.data) != type(k):
                    a.left.data , a.right.data = a.right.data , a.left.data
        elif a.data == 2:
            a.data = "*"
        elif a.data == 3:
            a.data = "÷"
        chushihua(a.left)
        chushihua(a.right)


def xxbl(a):  # 先序遍历
    print(a.data, end=" ")
    if a.left != None:
        xxbl(a.left)
    if a.right != None:
        xxbl(a.right)


def zxbl(a, ds):  # 中序遍历
    if a.left != None:
        zxbl(a.left, ds)
    ds.append(a.data)
    if a.right != None:
        zxbl(a.right, ds)


def hxbl(a, w):  # 后序遍历
    if a.left != None:
        hxbl(a.left, w)
    if a.right != None:
        hxbl(a.right, w)
    w.append(a.data)


def nbls(w):  # 逆波兰式
    while len(w) > 1:
        n = len(w)
        for i in range(2, n):
            if w[i] == "*":
                w[i - 2] *= w[i - 1]
                del w[i - 1], w[i - 1]
                break
            elif w[i] == "+":
                w[i - 2] += w[i - 1]
                del w[i - 1], w[i - 1]
                break
            elif w[i] == "-":
                w[i - 2] -= w[i - 1]
                if (w[i - 2]) < 0:
                    return
                del w[i - 1], w[i - 1]
                break
            elif w[i] == "÷":
                w[i - 2] /= w[i - 1]
                del w[i - 1], w[i - 1]
                break


n = 300  # 需要n个等式
i = 0
#print("请选择需要的功能")
#print("1 出题：")
#print("2计算结果：")
#c=int(input())
#if(c==1):
while (i < n):
    w = []
    ds = []
    a0, a1, a2, a3, a4, a5, a6, a7, a8 = [tree(random.randint(0, 3)) for j in range(9)]
    a0.left, a0.right = a1, a2
    a1.left, a1.right = a3, a4
    a2.left, a2.right = a5, a6
    a3.left, a3.right = a7, a8
    a0.data = random.randint(0, 1)  # 控制 01 节点的数值，使后序遍历变成逆波兰式
    a1.data = random.randint(0, 1)
    chushihua(a0)      #递归初始化这棵树
    zxbl(a0, ds)       #中序遍历这棵树
    hxbl(a0, w)        #得到逆波兰式
    nbls(w)     #计算逆波兰式
    if(w[0]>0):
    #if ((w[0]>0 and w[0]<1) or (w[0]>1 and w[0]%1==0)):
        for j in ds:
            print(j, end="")
        #print("\n")
        print("=",w[0])
        i += 1      
#elif(c==2):
#       if (w[0]>0 and w[0]<1) or(w[0]>1 and w[0]%1==0):
#            for j in ds:
#               print(j, end="")
#               print("=", w[0])
#               i += 1
