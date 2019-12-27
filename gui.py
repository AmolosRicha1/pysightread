# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1133, 584)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 811, 391))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 430, 80, 25))
        self.pushButton.setStyleSheet("color: rgb(186, 189, 182);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 430, 80, 25))
        self.pushButton_2.setStyleSheet("color: rgb(186, 189, 182);")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1133, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menuBar.setFont(font)
        self.menuBar.setStyleSheet("color: rgb(211, 215, 207);")
        self.menuBar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.menuBar.setObjectName("menuBar")
        self.menuDatai = QtWidgets.QMenu(self.menuBar)
        self.menuDatai.setObjectName("menuDatai")
        self.menuHelp_2 = QtWidgets.QMenu(self.menuBar)
        self.menuHelp_2.setObjectName("menuHelp_2")
        self.menuHelp_3 = QtWidgets.QMenu(self.menuBar)
        self.menuHelp_3.setObjectName("menuHelp_3")
        self.menuSetting = QtWidgets.QMenu(self.menuBar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menuBar)
        self.actionEinstellungen = QtWidgets.QAction(MainWindow)
        self.actionEinstellungen.setObjectName("actionEinstellungen")
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.actionminimize = QtWidgets.QAction(MainWindow)
        self.actionminimize.setObjectName("actionminimize")
        self.actionKey_signature = QtWidgets.QAction(MainWindow)
        self.actionKey_signature.setObjectName("actionKey_signature")
        self.actionChange_tempo = QtWidgets.QAction(MainWindow)
        self.actionChange_tempo.setObjectName("actionChange_tempo")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuDatai.addAction(self.actionEinstellungen)
        self.menuDatai.addSeparator()
        self.menuDatai.addSeparator()
        self.menuHelp_2.addAction(self.actionminimize)
        self.menuHelp_3.addAction(self.actionVersion)
        self.menuHelp_3.addAction(self.actionAbout)
        self.menuSetting.addAction(self.actionKey_signature)
        self.menuSetting.addAction(self.actionChange_tempo)
        self.menuBar.addAction(self.menuDatai.menuAction())
        self.menuBar.addAction(self.menuSetting.menuAction())
        self.menuBar.addAction(self.menuHelp_2.menuAction())
        self.menuBar.addAction(self.menuHelp_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/pic/Staff.png\"/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.menuDatai.setTitle(_translate("MainWindow", "File"))
        self.menuHelp_2.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp_3.setTitle(_translate("MainWindow", "Help"))
        self.menuSetting.setTitle(_translate("MainWindow", "Settings"))
        self.actionEinstellungen.setText(_translate("MainWindow", "Exit"))
        self.actionVersion.setText(_translate("MainWindow", "Version"))
        self.actionminimize.setText(_translate("MainWindow", "minimize"))
        self.actionKey_signature.setText(_translate("MainWindow", "Key signature"))
        self.actionChange_tempo.setText(_translate("MainWindow", "Change tempo"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

import Resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

