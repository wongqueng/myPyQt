# -*-coding:UTF-8-*-
import sys
import re
import urllib
import requests
import threading
import os
from PyQt4 import QtCore, QtGui

def clear():
	for filename in os.listdir('C:\Python27\youmin'.decode("utf-8")):
		# print filename
		os.remove(os.path.join('C:\Python27\youmin', filename))
clear()
src = '<img class="picact".*?src="(.*?)"'
detail1 = '<img class="picact".*?<br>(.*?)</p>'
member = '<p align="center"><.*?</p>'
titlelist = []
urllist = []
img = re.compile(src)
detail = re.compile(detail1)
mem = re.compile(member)


def gethtml(url):
	# 获取网页所有源码
	r = requests.get(url)
	return r.content.replace('\n', "")


def getimg(html, s):
	# 下载图片
	global img
	try:
		memlist = re.findall(mem, html)
		inde = 0
		for i in memlist:
			# print i
			imglist = re.findall(img, i)
			titles = re.findall(detail, i.replace('&nbsp; ', '').replace('&nbsp;', ''))
			for j in imglist:
				# 下载图片
				# print j
				tit = titles[0] if len(titles) > 0 else ["A", "B", "C", "D", "E"][inde]
				inde += 1
				# print tit
				urllib.urlretrieve(j, 'C:\\Python27\\youmin\\' + str(s) + "--" + unicode(tit.decode("utf-8")) + j[-4:])
	except:

		pass


class getmy(threading.Thread):
	# 创建多线程
	def __init__(self, url, begin, end):
		threading.Thread.__init__(self)
		self.url = url
		self.begin = begin
		self.end = end

	def run(self):
		try:
			for i in range(self.begin, self.end + 1):
				s = i
				if i == 1:
					i = ''
				else:
					i = '_' + str(i)
				murl = self.url[:-6] + str(i) + self.url[-6:]
				# print murl
				getimg(gethtml(murl), s)
		except:
			pass


def getbaseurl():
	url = 'http://www.gamersky.com/ent/'  # 游民每日图片发布页
	r = requests.get(url)
	s = r.content
	urlhtm1 = '<a class="img1" target="_blank" .*?</a>'  # 寻找图片发布页网址所在的html区域
	urlhtm2 = '<a class="img2" target="_blank" .*?</a>'
	herfhtm = 'http:.*?shtml'  # 图片发布页网址
	title = '<div class="txt">(.*?)</div>'
	urs1 = re.compile(urlhtm1)
	urs2 = re.compile(urlhtm2)
	# urs=re.compile(herfhtm)
	urllist1 = re.findall(urs1, s)  # 查找所有最新图片发布页网址
	urllist2 = re.findall(urs2, s)
	divlist = urllist1 + urllist2


	for i in divlist:
		urllist.append(re.search(herfhtm, i).group())
		title1 = re.search(title, i).group(1)
		titlelist.append(unicode(title1.decode("utf-8")))


class HelloPyQt(QtGui.QWidget):
	def __init__(self, fruit, parent=None):
		super(HelloPyQt, self).__init__(parent)
		self.setWindowTitle("PyQt Test")
		self.fruit = fruit
		self.btnPress = QtGui.QPushButton("clear")
		self.fruits = QtGui.QListWidget()
		self.fruits.addItems(fruit)
		self.fruits.itemDoubleClicked.connect(self.item_double_clcik)
		layout = QtGui.QVBoxLayout()
		layout.addWidget(self.fruits)
		layout.addWidget(self.btnPress)
		self.setLayout(layout)
		self.btnPress.clicked.connect(self.btnPress_Clicked)

	def btnPress_Clicked(self):
		clear()

	def item_double_clcik(self, item):
		targeturl = urllist[self.fruits.row(item)]
		threads = []
		i = 1
		j = 5
		# 每个线程下载5页，一共下载50页
		for s in range(10):
			threads.append(getmy(targeturl, i, j))
			i += 5
			j += 5

		for t in threads:
			t.start()
		for t in threads:
			t.join()


if __name__ == '__main__':
	getbaseurl()
	app = QtGui.QApplication(sys.argv)
	mainWindow = HelloPyQt(titlelist)
	mainWindow.show()
	sys.exit(app.exec_())
