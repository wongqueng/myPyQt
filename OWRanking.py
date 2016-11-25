#-*-coding:UTF-8-*-
import sys
import re
import requests
import webbrowser
from PyQt4 import QtCore, QtGui
baseurl="http://www.panda.tv/cate/"
owurl=baseurl+"overwatch"
lolurl=baseurl+"lol"
divreg=re.compile('<li class="video-list-item video-no-tag video-no-cate.*?</li>')
titlereg=re.compile('title="(.*?)"')
namereg=re.compile('<span class="video-nickname">(.*?)</span>')
numreg=re.compile('<span class="video-number">(.*?)</span>')
dataidreg=re.compile('data-id="(.*?)"')
r=requests.get(owurl)
r.encoding="utf-8"
divlist=re.findall(divreg,r.text.replace('\n',""))
titlels=[re.findall(titlereg,x)[0] for x in divlist]
names=[re.findall(namereg,x)[0] for x in divlist]
nums=[re.findall(numreg,x)[0] for x in divlist]
dataids=[re.findall(dataidreg,x)[0] for x in divlist]
resutls=[]

for i in range(0,len(divlist)):
	# print  resutls[i]
    resutls.append(names[i]+'__'+titlels[i]+'__'+nums[i])


class HelloPyQt(QtGui.QWidget):
	def __init__(self, titles,names,nums,dataids,resutls, parent=None):
		super(HelloPyQt, self).__init__(parent)
		self.setWindowTitle(u"熊猫TV OW专区排行")
		self.titles = titles
		self.names = names
		self.nums = nums
		self.dataids=dataids
		self.ranking=QtGui.QGridLayout()
		self.setMinimumWidth(400)
		self.setMinimumHeight(500)
		for i in range(0,min(20,len(titlels))):
			index=QtGui.QLabel(str(i+1))
			name=QtGui.QLabel(names[i])
			# title=QtGui.QPushButton(titles[i])
			num=QtGui.QLabel(nums[i])
			# title.clicked.connect(lambda: webbrowser.open_new_tab("http://www.panda.tv/" + dataids[i]))
			self.ranking.addWidget(index,i,0)
			self.ranking.addWidget(name,i,1)
			# self.ranking.addWidget(title,i,2)
			self.ranking.addWidget(num,i,2)
		self.fruits = QtGui.QListWidget()
		self.fruits.addItems(resutls[:20])
		self.fruits.itemDoubleClicked.connect(self.item_double_clcik)
		layout = QtGui.QHBoxLayout()
		# layout.addLayout(self.ranking)
		layout.addWidget(self.fruits)
		# self.ranking.itemDoubleClicked.connect(self.item_double_clcik)
		self.setLayout(layout)
	def item_double_clcik(self, item):
		print self.fruits.row(item)
		webbrowser.open_new_tab("http://www.panda.tv/"+self.dataids[self.fruits.row(item)])



if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	mainWindow = HelloPyQt(titlels,names,nums,dataids,resutls)
	mainWindow.show()
	sys.exit(app.exec_())