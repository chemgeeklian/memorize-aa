#!/usr/local/bin/python3.4
import database
import random
chn=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
def b():
	chc=random.shuffle(chn)
	gra=0
	print("请打开文件夹中的'测氨基酸'图片")
	while(1):
		for i in range(0,20):
			print("对应%d号的三字母缩写:"% database.aa[chn[i]].rj)
			inp1=input()
			inp=inp1.lower()
			if inp==database.aa[chn[i]].three:
				print('正确')
				gra+=1
			else:print("错误,正确答案%s"% database.aa[chn[i]].three)
		print("你的成绩是%d分,要再来一次吗,要请输入y,不要请输入别的"% gra)
		wh=input()
		if wh=='y':
			print("哦.\n")
			gra=0
			chc=random.shuffle(chn)
		else:break
def c():
	chc=random.shuffle(chn)
	gra=0
	print("请输入你在R基图中选定的答案序号数字\n")
	while(1):
		for i in range(0,20):
			print("对应%s的序号:"% database.aa[chn[i]].three)
			try:inp=int(input())
			except ValueError:
				print("请输入数字谢谢,再不听话走好不送")
				inp=int(input())
			if inp==database.aa[chn[i]].rj:
				print('正确')
				gra+=1
			else:print("错误,正确答案%s"% database.aa[chn[i]].rj)
		print("你的成绩是%d分,要再来一次吗,要请输入y,不要请输入别的"% gra)
		wh=input()
		if wh=='y':
			print("哦.\n")
			gra=0
			chc=random.shuffle(chn)
		else:break
def d():
	chc=random.shuffle(chn)
	gra=0
	while(1):
		for i in range(0,20):
			print("请输入%s的中文名:"% database.aa[chn[i]].three)
			inp=input()
			if inp==database.aa[chn[i]].name:
				print('正确')
				gra+=1
			else:print("错误,正确答案%s"% database.aa[chn[i]].name)
		print("你的成绩是%d分,要再来一次吗,要请输入y,不要请输入别的"% gra)
		wh=input()
		if wh=='y':
			print("哦.\n")
			gra=0
			chc=random.shuffle(chn)
		else:break
def e():
	chc=random.shuffle(chn)
	gra=0
	while(1):
		for i in range(0,20):
			print("%s的三个字母的缩写:"% database.aa[chn[i]].one)
			inp1=input()
			inp=inp1.lower()
			if inp==database.aa[chn[i]].three:
				print('正确')
				gra+=1
			else:print("错误,正确答案%s"% database.aa[chn[i]].three)
		print("你的成绩是%d分,要再来一次吗,要请输入y,不要请输入别的"% gra)
		wh=input()
		if wh=='y':
			print("哦.\n")
			gra=0
			chc=random.shuffle(chn)
		else:break
