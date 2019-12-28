#import for rtmidi usage
import random
import rtmidi as rt
from rtmidi.midiutil import open_midiinput

#imports for Gui
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QPushButton, QMainWindow, QLabel
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
import sys
import time
from gui import Ui_MainWindow
from About import Ui_Dialog
from Keysig import Ui_Dialogkeysig
from Keysign import CMaj

count=0
RandNote=random.choice(CMaj)

#start RT Midi input Thread
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
                print(message)
                if message[0][0]>140 and message[0][0]<160:
                    #print("------------------------")
                    #print("100 on")
                    self.updatedthree.emit(str(message[0][1]))
                else:
                    #print("---------------------------")
                    #print("0 off")
                    self.updatedthree.emit(str(message[0][0]))

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


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

class Dialogkeysig(QDialog, Ui_Dialogkeysig):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

#initializie Ui Communication with classes
class Logic(QMainWindow, Ui_MainWindow):
    #defined variable for exchanging Notenumber
    a=None

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.show()
        #QTimer for one Notebar
        timer=QTimer(self)
        timer.setInterval(20)
        #Connect Timer to Function
        timer.timeout.connect(self.updateTexttwoalt)
        timer.start()
        #ThreadClass which communicates with rtmidi
        self.threadclass= ThreadClass()
        self.threadclass.updatedthree.connect(self.updateTextthree)
        self.threadclass.start()

        self.ExitAction.triggered.connect(self.printTest)
        self.actionAbout.triggered.connect(self.openDialog)
        self.actionKey_signature.triggered.connect(self.openDialogKeysig)
        self.actionminimize.triggered.connect(self.showMinimized)

    def openDialog(self):
        d=Dialog(self)
        d.show()

    def openDialogKeysig(self):
        d=Dialogkeysig(self)
        d.show()


    def printTest(self):
        self.close()
    def updateTexttwoalt( self):
        #Variables counting the Qtimer
        global count
        global RandNote


        #change Position of the note
        MyLabeltwo=QLabel(self)
        MyLabeltwo.setPixmap(QPixmap('./pic/test.png'))
        Disptwo=502-count
        MyLabeltwo.setObjectName("specifictwo")
        DefiLabel=self.findChild(QLabel, "specifictwo")
        RandPos=200-8.5*(int(RandNote)-60)
        DefiLabel.move(Disptwo,RandPos)
        Position=DefiLabel.pos()
        count=count+3
        
        #recognize button presses 
        print("Rand Note"+str(RandNote))
        print("self.a" + str(self.a))
        if str(self.a)==str(RandNote):
            DefiLabel.hide()
            RandNote=random.choice(CMaj)
            RandPos=200-8.5*(int(RandNote)-60)
            Disptwo=502
            DefiLabel.move(Disptwo,RandPos)
            DefiLabel.show()
            count=0
            return 0
        #change Note
        if Position.x()> 200:
            DefiLabel.show()
        else:
            count=0
            RandNote=random.choice(CMaj)
            DefiLabel.hide()



    def updateTextthree( self, text):
        #set Variable for other funtion
        #Text is Notenumber or also 133
        print(text)
        self.a=text

        #show the pressed Note
        MyLabelthree=QLabel(self)
        MyLabelthree.setPixmap(QPixmap('./pic/test.png'))
        Dispthree=200-8.5*(int(text)-60)
        MyLabelthree.setObjectName("specific")
        self.findChild(QLabel, "specific").move(200,Dispthree)
        if int(text)==134:
            self.findChild(QLabel, "specific").hide()
        else: 
            self.findChild(QLabel, "specific").show()
        
#Does something when closed
    #def closeEvent(self, event):
    #    msgBox = QtWidgets.QMessageBox()
    #    msgBox.setIcon(QtWidgets.QMessageBox.Information)
    #    msgBox.setText("Message box pop up window")
    #    msgBox.setWindowTitle("QMessageBox Example")
    #    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
    #    msgBox.buttonClicked.connect(msgButtonClick)
    #    returnValue = msgBox.exec()
        
    #    if returnValue == QtWidgets.QMessageBox.Ok:
    #        print('OK clicked')
            

#main Part
if __name__== '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Logic(None)
    ui.showMaximized()
    sys.exit(app.exec_())

