#coding:utf-8
#读写文件

#引用sys模块里的argv
from sys import argv
#解包argv中的东西，将所有参数赋给左边的变量名
script,filename =argv

print "We're going to erase %r." % filename

print "If you don't want that,hit CTRL -C (^C)."

print "If you do want that,hit RETURN."
#提示等待用户操作
raw_input("?")

print "Opening the file..."
#以写入的方式打开文件，会删除原文件内容重新写入新的内容，如果没有该文件则创建
target = open(filename,'w')

print "Truncating the file. Goodbye!"
#清空文件
target.truncate()

print "Now I'm going to ask you for three lines."
#写入内容并赋给变量名
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")


#这个是根据习题后面要求改的
fi = line1+"\n"+line2+"\n"+line3+"\n"
#思路
print type(fi)
print fi

print "I'm going to write these to the file."
#依次写入接收进来的内容
target.write(fi)
#换行
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally,we close it."
#关闭文件
target.close()
