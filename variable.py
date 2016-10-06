#!/usr/bin/python
# coding:utf-8


x = "i am global var"
def fun():
    global y   #强制声明全局变量
    y = 200
    global x
    x = 100
print x       #没调用函数，输出的是全局变量
#测试变量x的局部变量与全局变量
fun()
print x       # 调用函数后，输出的是强制声明的全局变量
