#coding:utf-8
#字符转义

tabby_cat = "\tI'm tabbed in."

persian_cat = "I'm split\non a line.%r" % tabby_cat

backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat

print persian_cat 
print backslash_cat
print fat_cat
