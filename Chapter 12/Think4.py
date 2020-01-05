#打乱有序数组前m位顺，输出前m位，然后再排序
import random
a=list(range(0,100))
i=0
while i<20 :
    t = random.randint(0,99)
    j=a[i]
    a[i]=a[t]
    a[t]=j
    i=i+1
a=a[0:20]
a.sort()