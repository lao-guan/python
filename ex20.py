#coding:utf-8


#还是从argv模块中调用sys
from sys import argv
#解包赋值
script,input_file=argv
#定义一个函数：打印所读取文件的内容
def print_all(f):
    print f.read()
#定义一个函数：将文件指针指向从文件头部到偏移量字节处
def rewind(f):
    f.seek(0)
#定义一个函数，第一个值直接打印出来，将第二个值每次读取文件内容的一行
def print_a_line(line_count,f):
    print line_count,f.readline()
#打开文件并赋值给变量current_file
current_file = open(input_file)
#打印输出并换行
print "First let's print the whole file:\n"
#调用函数print_all
print_all(current_file)

print "Now let's rewind,kind of like a type."
#同上
rewind(current_file)

print "Let's print three lines:"
#定义current_line并赋值为1
current_line = 1
#调用函数，更换了变量名
print_a_line(current_line,current_file)
#变量自加1
current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)
