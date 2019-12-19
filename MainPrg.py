#import for rtmidi usage
import rtmidi as rt
from rtmidi.midiutil import open_midiinput

#imports for Gui
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QPushButton, QMainWindow, QLabel 
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
import sys
from gui import Ui_MainWindow
import time

#import Thread Function
#import rtinput
counter=0

#start RT Midi input
class ThreadClass(QThread,Ui_MainWindow ):
    updatedthree=QtCore.pyqtSignal(str)
    def __init__(self, *args,**kwargs):
        super(ThreadClass,self).__init__()
        self.args=args
        self.kwargs=kwargs
    @pyqtSlot()
    def run(self):
        #open Midi-Port for input
        mi, port_name=open_midiinput(port=None, api=0, use_virtual=True, interactive=True, client_name=None, port_name=None)
        #read input
        while True:
            message=mi.get_message()
            if message:
                print("Start --------------------")
                print(message)
                if message[0][0]>140 and message[0][0]<150:
                    print("------------------------")
                    print("100 on")
                    self.updatedthree.emit(str(message[0][1]))
                else:
                    print("---------------------------")
                    print("0 off")
                    self.updatedthree.emit(str(message[0][0]))



#move one note vertically
class Threadclasstwo(QThread,Ui_MainWindow):
    updated=QtCore.pyqtSignal(str)
    def run (self):
        for i in range(100):
            self.updated.emit(str(i))
            time.sleep(0.1)

#move one note vertically
class Threadclassthree(QThread,Ui_MainWindow):
    updatedtwo=QtCore.pyqtSignal(str)
    def run (self):
        for i in range(100):
            self.updatedtwo.emit(str(i))
            time.sleep(0.05)

#Button Clicked Funktion
def msgButtonClick():
    print("Button clicked is:")

#initializie Ui Communication with classes
class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.show()
        self.threadclass= ThreadClass()
        self.threadclass.updatedthree.connect(self.updateTextthree)
        self.threadclass.start()
        self.threadclasstwo= Threadclasstwo(self)
        self.threadclasstwo.updated.connect(self.updateText)
        self.threadclasstwo.start()

        self.threadclassthree= Threadclassthree(self)
        self.threadclassthree.updatedtwo.connect(self.updateTexttwo)
        self.threadclassthree.start()

#Displaying note and move it
    def updateTexttwo( self, text) :
        print("Displacement"+text)
        MyLabeltwo=QLabel(self)
        MyLabeltwo.setPixmap(QPixmap('./pic/test.png'))
        Disptwo=302-3*(int(text))
        #MyLabel.setGeometry(200,Disp,20,20)
        MyLabeltwo.move(Disptwo,200)
        MyLabeltwo.show()

#Displaying a note and move it
    def updateText( self, text) :
        print()
        #MyLabel=QLabel(self)
        #MyLabel.setPixmap(QPixmap('./pic/test.png'))
        #Disp=302-29*int(text)
        #MyLabel.setGeometry(200,Disp,20,20)
        #MyLabel.move(200,Disp)
        #MyLabel.show()
    #class NewLabel(QLabel):
    #    def __init__(self, parent=None):
    #       QLabel.__init__(self, parent)
    #    def hideMe(self):
    #        self.show()
    #        QTimer.singleShot(1000, self.showMe)
    #    def showMe(self):
    #        self.hide()
    #        self.move(self.pos())
    #        if int(text)>0:
    #            print("show")
    #            self.show()
    #        else:   
    #            print("jaaa")
    #            self.hide()



    def updateTextthree( self, text):
    #    NewLabel.hideMe()
        print("Text"+text)
        print("Pressed Note number: " + text)
        MyLabelthree=QLabel(self)
        MyLabelthree.setPixmap(QPixmap('./pic/test.png'))
        Dispthree=200-8.5*(int(text)-60)
        #MyLabel.setGeometry(200,Disp,20,20)
        #some ugly written code
        #MyLabelthree.move(200,Dispthree)
        MyLabelthree.setObjectName("specific")
        self.findChild(QLabel, "specific").move(200,Dispthree)
        if int(text)==128:
            print("000000000000000000000")
            self.findChild(QLabel, "specific").hide()
            #MyLabelthree.hide()
        else: 
            print("xxxxxxxxxxxxxxxxxxxxxxx")
            self.findChild(QLabel, "specific").show()
            #MyLabelthree.show()
        
#Does something when closed
    def closeEvent(self, event):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText("Message box pop up window")
        msgBox.setWindowTitle("QMessageBox Example")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msgBox.buttonClicked.connect(msgButtonClick)
        returnValue = msgBox.exec()
        
        if returnValue == QtWidgets.QMessageBox.Ok:
            print('OK clicked')
            

#main Part
if __name__== '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Logic(None)
    ui.showMaximized()
    sys.exit(app.exec_())

