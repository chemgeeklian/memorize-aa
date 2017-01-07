#!/usr/local/bin/python3.4
import os
import database
import tip
import func

print('''【背氨基酸软件1.0】   作者:不愿透漏姓名的唐班同学
说明:发现bug请及时告诉我,知道bash里运行python怎么清屏告诉我 
     因时间仓卒且本人能力有限软件界面友好度不高,代码在文件夹里,欢迎交流改进
''')
while(1):
	print('''你想干什么
a.这个选项被去掉了,谁知道在linux怎么用python打开图片
b.看R基测三个字母的缩写
c.看三个字母的缩写测R基
d.看三个字母的缩写测中文
e.看一个字母的缩写测三个字母的缩写
f.看看我总结的一点东西
g.不学了,滚''')
	cho=str(input())
	if cho=='g':exit()
	if cho=='f':
		print(tip.t)
		nothing=input()
		continue
	if cho=='b':
		func.b()
		continue
	if cho=='c':
		func.c()
		continue
	if cho=='d':
		func.d()
		continue
	if cho=='e':
		func.e()
		continue
	else:
		print("不好好学习,不跟你玩了")
		nothing=input()
		exit()
