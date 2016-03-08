#-*- coding:utf-8 -*-
####################################################
#
#    Author: Chuwei Luo
#    Email: luochuwei@gmail.com
#    Date: 07/03/2016
#    Usage: xml
#
####################################################

import xml.dom.minidom as xdm


#打开xml
t = xdm.parse('t1.xml')

#得到文档元素对象
root = t.documentElement
print root.nodeName
print root.nodeValue
print root.nodeType
print root.ELEMENT_NODE


maxid = root.getElementsByTagName('maxid')
mid = maxid[0]
print mid.nodeName

login = root.getElementsByTagName('login')
lg = login[0]
print lg.nodeName
#获得标签属性值
username = lg.getAttribute("username")
print username
passwd = lg.getAttribute("passwd")
print passwd

caption = root.getElementsByTagName('caption')
cp = caption[2]
print "xml have", len(caption), cp.nodeName

item = root.getElementsByTagName('item')
it = item[1]
print "xml have", len(item), it.nodeName
for i in item:
	item_id = i.getAttribute("id")
	print item_id


#获得标签对之间的数据 1
for c in caption:
	print c.firstChild.data

#获得标签对之间的数据 2
from xml.etree import ElementTree as ET
per = ET.parse('t1.xml')
p = per.findall('./login/item')

for i in p:
    for child in     i.getchildren():
        print child.tag,':',child.text


p=per.findall('./item')

for    i  in p:
    for child in     i.getchildren():
        print child.tag,':',child.text