# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hand.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys

from PyQt5.QtGui import QFontDatabase
from matplotlib.font_manager import FontProperties
class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(MainWindow)
        self.textBrowser.setGeometry(QtCore.QRect(340, 200, 1500, 100))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet(
            '''QTextBrowser{background:rgb(255, 255, 255, 250);border-radius:10px;font-family:font;color:black;font-size:25px;}QTextBrowser:hover\n
            {background:rgb(255, 255, 255, 250);}''')

        self.labelcamera = QtWidgets.QLabel(MainWindow)
        self.labelcamera.setGeometry(QtCore.QRect(340, 355, 1500, 620))
        self.labelcamera.setPixmap(QtGui.QPixmap("assets/white.jpg"))
        self.labelcamera.setScaledContents(True)
        self.labelcamera.setObjectName("camera")
        self.label_title = QtWidgets.QLabel(MainWindow)
        self.label_title.setGeometry(QtCore.QRect(440, 50, 400, 90))
        self.label_title.setStyleSheet("font-family:华文行楷;\n"
                                    "color:black;\n"
                                    "font-size:50px;")
        self.label_title.setObjectName("label_title")
        self.pushButton_point = QtWidgets.QPushButton(MainWindow)
        self.pushButton_point.setGeometry(QtCore.QRect(70, 440,210, 80))
        self.pushButton_point.setStyleSheet(
            '''QPushButton{background:rgb(255, 255, 255, 60);border-radius:5px;font-family:华文行楷;color:black;font-size:30px;}QPushButton:hover\n
            {background:rgb(255, 255, 255, 250);}''')
        self.pushButton_point.setObjectName("pushButton_point")
        self.pushButton_number = QtWidgets.QPushButton(MainWindow)
        self.pushButton_number.setGeometry(QtCore.QRect(70, 260, 210, 80))
        self.pushButton_number.setStyleSheet(
            '''QPushButton{background:rgb(255, 255, 255, 60);border-radius:5px;font-family:华文行楷;color:black;font-size:30px;}QPushButton:hover\n
            {background:rgb(255, 255, 255, 250);}''')
        self.pushButton_number.setObjectName("pushButton_number")
        self.pushButton_stop = QtWidgets.QPushButton(MainWindow)
        self.pushButton_stop.setGeometry(QtCore.QRect(70, 530, 210, 80))
        self.pushButton_stop.setStyleSheet(
            '''QPushButton{background:rgb(255, 255, 255, 60);border-radius:5px;font-family:华文行楷;color:black;font-size:30px;}QPushButton:hover\n
            {background:rgb(255, 255, 255, 250);}''')
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.pushButton_clean = QtWidgets.QPushButton(MainWindow)
        self.pushButton_clean.setGeometry(QtCore.QRect(70, 620, 210, 80))
        self.pushButton_clean.setStyleSheet(
            '''QPushButton{background:rgb(255, 255, 255, 60);border-radius:5px;font-family:华文行楷;color:black;font-size:30px;}QPushButton:hover\n
            {background:rgb(255, 255, 255, 250);}''')
        self.pushButton_clean.setObjectName("pushButton_clean")
        self.pushButton_video = QtWidgets.QPushButton(MainWindow)
        self.pushButton_video.setGeometry(QtCore.QRect(70, 350, 210, 80))
        self.pushButton_video.setStyleSheet(
            '''QPushButton{background:rgb(255, 255, 255, 60);border-radius:5px;font-family:华文行楷;color:black;font-size:30px;}QPushButton:hover\n
            {background:rgb(255, 255, 255, 250);}''')
        self.pushButton_video.setObjectName("pushButton_video")
        self.label_out = QtWidgets.QLabel(MainWindow)
        self.label_out.setGeometry(QtCore.QRect(350, 155, 200, 40))
        self.label_out.setStyleSheet("font-family:华文行楷;\n"
                                    "color:black;\n"
                                    "font-size:40px;")
        self.label_out.setText("")
        self.label_out.setPixmap(QtGui.QPixmap("Picture/1.png"))
        self.label_out.setScaledContents(True)
        self.label_out.setObjectName("label_out")
        self.label_cam = QtWidgets.QLabel(MainWindow)
        self.label_cam.setGeometry(QtCore.QRect(350, 315, 200, 40))
        self.label_cam.setStyleSheet("font-family:华文行楷;\n"
                                     "color:black;\n"
                                     "font-size:40px;")
        self.label_cam.setText("")
        self.label_cam.setPixmap(QtGui.QPixmap("Picture/1.png"))
        self.label_cam.setScaledContents(True)
        self.label_cam.setObjectName("label_cam")
        self.pushButton_readme = QtWidgets.QPushButton(MainWindow)
        self.pushButton_readme.setGeometry(QtCore.QRect(70, 170, 210, 80))
        self.pushButton_readme.setStyleSheet(
            '''QPushButton{background:rgb(255, 255, 255, 60);border-radius:5px;font-family:华文行楷;color:black;font-size:30px;}QPushButton:hover\n
            {background:rgb(255, 255, 255, 250);}''')
        self.pushButton_readme.setObjectName("pushButton_readme")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "健身计数应用"))
        self.label_title.setText(_translate("Form", "健身计数应用"))
        self.pushButton_point.setText(_translate("Form", "关键点检测"))
        self.pushButton_number.setText(_translate("Form", "实时健身计数"))
        self.label_out.setText(_translate("Form", "输出信息"))
        self.label_cam.setText(_translate("Form", "实时监测"))
        self.pushButton_stop.setText(_translate("Form", "停止检测"))
        self.pushButton_clean.setText(_translate("Form", "清空输出"))
        self.pushButton_readme.setText(_translate("Form", "使用说明"))
        self.pushButton_video.setText(_translate("Form", "视频健身计数"))

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = e.globalPos() - self.pos()
            e.accept()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = False

    def mouseMoveEvent(self, e):
        try:
            if Qt.LeftButton and self.m_drag:
                self.move(e.globalPos() - self.m_DragPosition)
                e.accept()
        except:
            print("错误代码:000x0")


    def printstr(self, mypstr):
        ###自定义类print函数,借用c语言 printf Mypstr：是待显示的字符串###
        self.textBrowser.append(mypstr)  #在指定的区域显示提示信息
        self.cursot = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursot.End)



