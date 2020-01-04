import random
m=20
n=100
a=[]
#根据题意，输出序列数的大小范围是0-n
for i in range(0,100):
    #实际操作中模运算只需将随机数的范围控制到0-n，就可以覆盖模运算的所有结果
    #for i in range(0,100):保证输出的序列是有序的,m=m-1控制20个数子
    if (random.randint(0,100)%n)< m :
        a.append(i)
        m=m-1
    n=n-1
#print(a,'\n',len(a))