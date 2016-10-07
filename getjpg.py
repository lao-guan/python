#!/usr/bin/python
#/coding:utf-8

import re
import urllib

#获取网页源代码
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#通过正则从“html”获得图片
def getImg(html):
    reg = r'src="(.*?\.jpg)" bdwater'
    imgre = re.compile(reg)             #编译reg
    imglist = re.findall(imgre,html)
#下载图片
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1

html = getHtml("http://tieba.baidu.com/p/3511372887")
getImg(html)    #将"html"给函数getImg
