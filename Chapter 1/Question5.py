##将输入的列表分两次排序，只需加个判断语句如果选取
#的数大于N/2则在第二次排序，反之第一次排序
import random
from bitarray import bitarray
#这样只占用0.75MB空间
a=bitarray(5000000)
a.setall(0)
b=[]
c=[]
d=[]
#模拟输入文件
index=random.sample(range(0,10000000),1000000)
#将输入文件分为大于5000000和小于5000000两部分
for i in range(1000000):
    if index[i] < 5000000:
        b.append(i)
for i in range(1000000):
    if index[i] > 5000000:
        c.append(i)
#开始排序
for i in range(len(b)):
        a[b[i]]=1
for i in range(len(a)):
    if a[i]==1:
        d.append(i)
a.setall(0)
#然后进行第二趟排序
for i in range(len(c)):
        a[c[i]]=1
for i in range(len(a)):
    if a[i]==1:
        d.append(i)
#最后输出的是d