from bitarray import bitarray
import numpy as np
import random

# #使用range函数输出一个开始为1，步进为1，终止为10000000的排行
# #range(1,10)其实输出9个数，不包括10
# #使用list(range(1,10000000))可以转化为list类型
# a=range(1,10000000)
# #随机生成1000000个(1,10000000)范围内不重复的数字
# index=random.sample(range(1,10000000),1000000)
# #随机生成可能重复的5个从0-10的整数
# x1=np.random.randint(0,10,size=5)
# #当然也可以使用random库这样实现
# n=0
# x2=[]
# while n<5:
#     x2.append(random.randint(0,10))
#     n=n+1

'''显然本题是随机生成1000000个(1,10000000)范围内不重复的数字'''
index=random.sample(range(1,10000001),1000000)
#使用bitarray库创建位序列
#创建一个长度为1000w个bit的位序列（因为整数的范围是1000w），其值随机为1或0
a=bitarray(10000000)
#将其全部置0
a.setall(0)
#创建一个排序列表
b=[]
#将index[]中的数取出，将每个对应的位序列中的位置置1
for x in range(1000000):
    a[index[x]]=1
#检验每一位，如果为1，就输出其数据
for x in range(10000000):
    if a[x]==1:
        b.append(x)
    else:
        pass