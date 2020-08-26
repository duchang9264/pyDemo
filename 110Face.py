# -*- coding:utf-8 -*-

#1、一行代码实现1--100之和
i = sum(range(0, 101))
print(i)

#2、如何在一个函数内部修改全局变量
a = 4
def fn():
    global a
    a = 5
fn()
print(a)

#4、字典如何删除键和合并两个字典
dic = {'name':'duchang', 'age':18}
del dic['name']
print(dic)

dic2 = {'name': 'wangwu'}
dic.update(dic2)
print(dic)

#6、python实现列表去重的方法
list = [11,12,12,13,13,15,46]
a = set(list)
list = [x for x in a]
print(list)

#13、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
list = [1, 2, 3, 4, 5]
def fun(x):
    return x**2

res = map(fun, list)
res = [x for x in res if x > 10]
print(res)

#14、python中生成随机整数、随机小数、0--1之间小数方法
import random
import numpy as np

result = random.randint(10, 20)
res = np.random.rand(5)
ret = random.random()
print(f'正整数{result}')
print(f'5个随机小数{res}')
print(f'0-1随机小数{ret}')

#22、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
s = "ajldjlajfdljfddd"
s = set(s)
s = [x for x in s]
s.sort(reverse=False)
re = ''.join(s)
print(re)

#23、用lambda函数实现两个数相乘
sum = lambda x,y : x*y
print(sum(4, 5))

#24、字典根据键从小到大排序
dict1={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
list = sorted(dict1.items(), key=lambda i: i[0], reverse=False)
new_dict = {}
for i in list:
    new_dict[i[0]] = i[1]
print(new_dict)

#25、利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
from collections import Counter
str = 'kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h'
res = Counter(str)
print(res)

#27、filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def fn(x):
    return x%2 == 1

new_list = filter(fn, a)
new_list = [i for i in new_list]
print(f'27:{new_list}')

#28、列表推导式求列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x%2 == 1]
print(f'28:{b}')

#39、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
a = [[1,2],[3,4],[5,6]]
x = [j for i in a for j in i]
print(f'39_01:{x}')

import numpy as np
np_list = np.array(a).flatten().tolist()
print(f'39_02:{np_list}')


#53、写一个单列模式
'''
因为创建对象时__new__方法执行，并且必须return 返回实例化出来的对象所cls.__instance是否存在，
不存在的话就创建对象，存在的话就返回该对象，来保证只有一个实例对象存在（单列），打印ID，值一样，说明对象同一个
'''
class Singleton(object):
    __instance = None

    def __new__(cls, age, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

a = Singleton(18, 'dongGe')
b = Singleton(8, 'dongGe')

print(id(a))
print(id(b))

a.age = 19
print(b.age)

#54、保留两位小数
a="%.03f"%1.3355
print(a, type(a))
b = round(float(a), 2)
print(b)
