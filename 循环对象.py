#-*- coding:utf-8 -*-

#迭代器(range(),列表，生成器)
	


#生成器（yield）

# def gen():
# 	a = 100
# 	yield a
# 	a = a * 8
# 	yield a 
# 	yield 1000

# for i in gen():
# 	print(i)


def gen():
	for i in range(4):
		yield i

G = (x for x in range(4)) #生成器表达式

for i in G:
	print(i)

#列表推导式

L = [ x for x in range(10)]


#python内存管理

a=1 
b=1
print(id(a))
print(hex(id(a)))
print(id(b))

print(a is b)

a = "good"
b = "good"
print(a is b)

a = "very good morning"
b = "very good morning"


print(a is b)

a=[]
b=[]
print(a is b)


from sys import getrefcount
a = [1, 2, 3]
print(getrefcount(a))

b = [a,a]
print(getrefcount(a))

x=[1, 2, 3]
y=[x, dict(key1=x)]
z=[y, (x, y)]

import objgraph

objgraph.show_refs([z], filename='ref_topo.png')









