#coding:utf-8

#定义函数
def break_words(stuff):
    """This functions will break up words for us."""
    words =stuff.split(' ')   #将字符串分割开并赋值给变量words
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)      #将变量words排序返回

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)       #删除list中的第一个字符串
    print word

def print_last_word(words):
    """Prints the last word after poping it off."""
    word = words.pop(-1)      #删除list中的最后一个字符串
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)   #调用break_words函数并赋值给变量words
    return sort_words(words)        #将变量words值返回给函数sort_words

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)  
    print_first_word(words)    #调用函数print_first_words
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)   #调用函数sort_sentence并赋值给words
    print_first_word(words)
    print_last_word(words)
