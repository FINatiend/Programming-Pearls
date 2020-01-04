from bitarray import bitarray
import random
#假设n为100，m为20
n = 100
m =20
a=bitarray(100)
a.setall(0)
b=[]
#辅助数据结构为位序列，代表0-99这100个数是否被选过
#a[0]=1，表示被选过，a[0]=0表示未被选过,初始都为0
while m>0:
    #如果提供的随机数没有确定的范围，则可以通过取余数操作进行限制
    i=random.randint(0,99)
    if a[i]==0:
        a[i]=1
        b.append(i)
        m=m-1
#使用排序算法将序列有序
b.sort()
#print(b)