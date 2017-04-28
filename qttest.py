#-*-coding:UTF-8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import  time
import threading
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class MyQQ(QTabWidget):
    def __init__(self, parent=None):
        super(MyQQ, self).__init__(parent)

        toolButton1 = QToolButton()
        toolButton1.setText(self.tr("gavin"))
        toolButton1.setIcon(QIcon("F:\MTKK\hdImg_1242b1da7a7909577a1fe2b6fe44030d.jpg"))
        toolButton1.setIconSize(QSize(60, 60))
        toolButton1.setAutoRaise(True)
        toolButton1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        toolButton2 = QToolButton()
        toolButton2.setText(self.tr("问题的方法"))
        toolButton2.setIcon(QIcon("F:\MTKK\urkya.jpg"))
        toolButton2.setIconSize(QSize(60, 60))
        toolButton2.setAutoRaise(True)
        toolButton2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        toolButton3 = QToolButton()
        toolButton3.setText(self.tr("为什么"))
        toolButton3.setIcon(QIcon("F:\MTKK\p8sb.jpg"))
        toolButton3.setIconSize(QSize(60, 60))
        toolButton3.setAutoRaise(True)
        toolButton3.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        groupbox1 = QGroupBox()
        vlayout1 = QVBoxLayout(groupbox1)
        vlayout1.setMargin(10)
        vlayout1.setAlignment(Qt.AlignCenter)
        vlayout1.addWidget(toolButton1)
        vlayout1.addWidget(toolButton2)
        vlayout1.addStretch()

        groupbox2 = QGroupBox()
        vlayout2 = QVBoxLayout(groupbox2)
        vlayout2.setMargin(10)
        vlayout2.setAlignment(Qt.AlignCenter)
        vlayout2.addWidget(toolButton3)
        vlayout2.addStretch()

        groupbox3 = QGroupBox()

        toolbox1 = QToolBox()
        toolbox1.addItem(groupbox1, self.tr("我的好友"))
        toolbox1.addItem(groupbox2, self.tr("同事"))
        toolbox1.addItem(groupbox3, self.tr("黑名单"))

        toolbox2 = QWidget()
        vlayout=QVBoxLayout()
        self.button=QPushButton("Press me!")
        self.button.clicked.connect(self.showDialog)
        vlayout.addWidget(self.button)
        vlayout.addStretch()
        toolbox2.setLayout(vlayout)
        self.addTab(toolbox1, self.tr("联系人"))
        self.addTab(toolbox2, self.tr("群/讨论组"))

    def showDialog(self):
         self.dialog=QProgressDialog(self)
         self.dialog.setLabelText(u"d逗我玩")
         self.dialog.setWindowModality(Qt.ApplicationModal)
         self.dialog.setAutoClose(True)
         self.dialog.open()

         t1 = threading.Thread(target=self.updatepro)
         t1.start()
    def updatepro(self):
         for i in range(10):
             if self.dialog.wasCanceled():
                 break
             self.dialog.setValue((i+1)*10)
             time.sleep(1)
         # text, ok = QInputDialog.getText(self, 'Input Dialog',
         #                                          'Enter your name:')
         # if ok:
         #     self.button.setText(text)

app = QApplication(sys.argv)
myqq = MyQQ()
myqq.setWindowTitle("QQ2012")
myqq.setWindowModality(Qt.ApplicationModal)
myqq.show()
app.exec_()