#根据Question9_2_1改造Question9_1
#缺点是每次需要执行一次判断，遍历一次数组b
import numpy as np
#模拟题目中的数组
data=list(np.random.randint(0,100,size=20))
#to数组记录访问data[i]的索引i
to=['c']
# fromx记录访问data[i]的索引i 存在to数组的哪个位置
fromx=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#top记录最近一次访问data[i]的索引i存在to数组里的位置
top=0
#模拟访问数组item的次序
index=[5,0,4,1,3,8,15,6,13,5,4,6,15]
for i in index:
    #首先判断是否访问过
    # if (fromx[i]<top)%(to[fromx[i]]==i) :
    #     # 访问过
    #     pass

    if fromx[i]==0:
        #没访问过
        to.append(i)
        top=top+1
        fromx[i]==len(to)-1
        data[i]=0
    #该干嘛干嘛
print(data,fromx,to,top,index)