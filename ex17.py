#coding:utf-8
#这个还可以代码精减的

from sys import argv
#exist的功能是判断一个文件是否存在
from os.path import exists

script,from_file,to_file = argv

print "Copying from %s to %s" % (from_file,to_file)

#we could do these two on one line too,how?

#将原文件打开并赋给变量input
input = open(from_file)
#将文件读取出来赋给变量indata
indata = input.read()

print "The input file is %d bytes long" % len(indata)
#这就是exists的用法
print "Does the output file exist? %r" % exists(to_file)

print "Ready,hit RETURN to continue,CTRL -C to abort." 

raw_input()
#以写入的方式打开要拷贝的文件，会清除文件内容，如果没有此文件则创建
output = open(to_file,'w')
#开始写入
output.write(indata)
 

print "Alright,all done."

output.close()
input.close()
