#第一章 开篇
##知识点
1. 给定题目仔细思考，可以从问题的独特性，以及从每个bit位来考虑
2. 位图数据结构
3. 多趟算法，每次完成算法的一步（合起来完成这个问题）
4. 时间-空间折中与双赢（当空间制约因素大的时候减少程序的空间需求会减少
   其运行时间）只有在原始的设计远非最佳方案时，才有可能时空双赢。
5. 设计出的程序简单
##笔记

###Python中的变量

`a='ZWY'`   
在内存中创建了一个'ZWY'的字符串；在内存中创建一个名位a的变量，并把它指向'ZWY'
###ASCII,Unicode,UTF-8编码

所谓编码方式是用一串二进制数代表生活中实际用到的文字  

|  编码方式   |                   大小                   |       特征       |        冗余        |
| :-----: | :------------------------------------: | :------------: | :--------------: |
|  ASCII  |                1个字节8bit                | 美国人发明，127个字符编入 |   2**8=256-127   |
| GB2312  |               2个字节16bit                |  中国发明，兼容ASCII  | 2**16=65536-已编字符 |
| Unicode | 2个字节16bit称为UCS-2<br>4个字节称为UCS-4或UTF-32 |    兼容全世界符号     |                  |
|  UTF-8  |               可变字节，节省空间                |    兼容全世界符号     |                  |
总结：  
内存中一般采用固定字节大小的Unicode编码  
各种存储介质中可以UTF-8编码
Python使用Unicode编码

###Python中数据类型、sys.getsizeof()  
#### **数据类型的大小**
通常来说一个int占4个字节，一个char占1个字节，一个float占4个字节但是Python中一切都是对象，因此Python中不存在float、int这些数据类型  
**int，float也是一个对像**  
```Python
import sys
a = 1
print(sys.getsizeof(a)) 
```
结果会显示a的大小为28，这是因为Python代码在运行的时候会由Python解释器执行，
具体会解释为c语言的某种结构。也就是说，Python中的一个int映射到c语言中会是
一种结构体，结构体中会包含其他信息。以下是Python中的int在c中的具体形式：
```C
struct_long{
    long ob_refcnt;引用计数
    PyTypeObeject*ob_Type;//变量类型
    size_tob_size;//实际占用打下
    long ob_digit[1];//存储的实际Python值
};
```
Python实际的值只是相应c结构中的一个属性。  
浮点除法：/ 取整：// 取与：%
#### sys.getsizeof（）函数  
sys.getsizeof()需要sys库，返回值是占用多少字节，此外还有以下特点：
* sys.getsizeof()只计算实际使用的内存大小，引用所消耗的内存大小不计算
* sys.getsizeof()只能作为计算内存大小的参考
###位运算及操作位向量
在Question2.py中
###准确进行Python位操作
在Question3.py中  
**bitarrary库**
###生成随机数

使用range函数输出一个开始为1，步进为1，终止为10000000的排行
range(1,10)其实输出9个数，不包括10。
使用list(range(1,10000000))可以转化为list类型  
`a=range(1,10000000)`  
1. 随机生成1000000个(1,10000000)范围内不重复的数字  
  `index=random.sample(range(1,10000000),1000000)`  
2. 随机生成可能重复的5个从0-10的整数
  `x1=np.random.randint(0,10,size=5)`
3. 当然也可以使用random库这样实现  
```
n=0
x2=[]
while n<5:
    x2.append(random.randint(0,10))
    n=n+1
```

