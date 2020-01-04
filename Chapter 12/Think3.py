import random
#输入为m,n。输出为个数为m,数字大小在0~n-1的有序数列,set 保证不重复。
m=20
n=100
a=set()
i=20
while i >0 :
    t=random.randint(0,100)
    if ~(t in a):
        a.add(t)
        i=i-1
a=list(a)
a.sort()