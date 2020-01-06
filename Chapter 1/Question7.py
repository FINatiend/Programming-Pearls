from bitarray import  bitarray
import random
import numpy as np
'''如果某个数出现超过一次的话，1.4节的算法会发生只记录1次'''
#也就是说每个数的出现此数被压缩到了1。
#添加一个判断语句判断位序列的初值是否为0
a=bitarray(1000000)
a.setall(0)
input=np.random.randint(0,10,size=5)
for i in range(len(input)):
    if a[input[i]]==0:
        a[input[i]]=1
    else:
        #一个数最多出现len(input)次也就是100w次，100w可以用20bit，3个Byte
        #加上位序列的bit，一个数可以用4个Byte表示
        #空间为1MB，除以4Byte等于25w个数
        #1000w个数除以250W等于40。分40次完成。
        pass
'''当输入整数小于等于n，或者输入的数不是数值时，a[input[i]]会出错'''
#这种情况应实现检查一边输入数据是否符合要求，若不符合提示数据输入人员