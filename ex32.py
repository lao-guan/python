#coding:utf-8

#定义三个list列表
the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

#this first kind of for-loop goes through a list
# 将 the_count 列表进行 for 循环并打印出来
for number in the_count:
    print "This is count %d" % number

#same as above
# 将 fruits 列表进行 for 循环并打印出来
for fruit in fruits:
    print "A fruit of type: %s" % fruit

#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it
# 将 change 列表进行 for 循环并打印出来
for i in change:
    print "I got %r" % i

# we can also build lists,first start with an empty one
#定义一个空 list
elements = []

# then use the range function to do 0 to 5 counts
# 使用 range 进行 0 到 5 的循环
for i in range(0,6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    # 将 0 到 5 依次自增到 elements list中
    elements.append(i)

# now we can print them out too
# 将 elements 进行for循环
for i in elements:
    print "Element was: %d" % i
elements = range(0,6)
print elements
