#coding:utf-8

#引用sys模块里的argv
from sys import argv
#把argv中的东西解包，将所有的参数依次赋给左边变量名
script,filename = argv
#打开文件并赋给变量txt
txt = open(filename)
#格式化字符串并输出
print "Here's your file %r:" % filename
#输出查看到的文件内容
print txt.read()

print txt.close()
#打印一行字符串
#print "Type the filename again:"
#从屏幕上接收字符，并有个提示符“>”
#file_again = raw_input("> ")
#再次打开文件并赋给变量
#txt_again = open(file_again)
#输出查看到的文件内容
#print txt_again.read()

#print txt_again.close()
