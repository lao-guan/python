# coding:utf-8
# ex35.py 函数与分支

# 将 sys 模组导入进来,exit 功能是捕获异常  
from sys import exit

# 定义函数
def gold_room():
    print "This room is full of gold. How much do you take?"

# 接收键盘输入
    next = raw_input("> ")
# 如果 next 为 “0” 或者为 “1”，将 next 强制转为整数型并赋值给 how_much 变量
    if "0" in next or "1" in next:
        how_much = int(next)
# 否则执行函数 dead()
    else:
        dead("Man,learn to type a number.")

# 如果 how_much 变量小于 50 ， 输出语句并退出程序
    if how_much < 50:
        print "Nice, you're not greedy,you win!"
        exit(0)
# 否则执行函数 dead()
    else:
        dead("You greedy bastard!")


# 定义函数 bear_room
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

# while 循环
    while True:
        next = raw_input("> ")

# 如果 next 等于 take...执行函数 dead()
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
# 如果 next 等于 taunt ... 并且为真，输出语句，bear_move 为真
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door.You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()          #  满足条件，执行gold_room 函数
        else:
            print "I got no idea what that means."

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He,it,whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

# 如果 next 为 flee，执行函数 start()
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


# 定义函数返回值 dead（）
def dead(why):
    print why,"Good job!"
    exit(0)

# 定义函数 start（）
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

# 定义程序从 start() 开始执行
start()
