#coding:utf-8
#定义函数
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
#调用函数，给变量赋值
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

#定义变量并给两个变量赋值
print "OR,we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
#重新定义函数里的两个变量名
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

#调用函数，参数是运算
print "We can even do math inside too:"
cheese_and_crackers(10 + 20,5+6)


#调用函数，参数是变量与运算结合
print "And we can combine the two,variables and math:"
cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers + 1000)
