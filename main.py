#!/usr/local/bin/python3.4

import database
import tip
import func

print('''【Amino acid memorizing helper 1.1】   Author :Chemistrash
''')
while(1):
	print('''What do you want to do?
a.这个选项被去掉了,谁知道在linux怎么用python打开图片
b.看R基测三个字母的缩写
c.看三个字母的缩写测R基
d.看三个字母的缩写测中文
e.看一个字母的缩写测三个字母的缩写
f.See some tips
g.Exit''')
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
	if cho=='g':
		nothing=input()
		exit()
	else:
		print("Invalid choice")
		nothing=input()
