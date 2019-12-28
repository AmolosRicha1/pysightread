# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Keysig.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialogkeysig(object):
    def setupUi(self, Dialogkeysig):
        Dialogkeysig.setObjectName("Dialogkeysig")
        Dialogkeysig.resize(458, 335)

        self.retranslateUi(Dialogkeysig)
        QtCore.QMetaObject.connectSlotsByName(Dialogkeysig)

    def retranslateUi(self, Dialogkeysig):
        _translate = QtCore.QCoreApplication.translate
        Dialogkeysig.setWindowTitle(_translate("Dialogkeysig", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialogkeysig = QtWidgets.QDialog()
    ui = Ui_Dialogkeysig()
    ui.setupUi(Dialogkeysig)
    Dialogkeysig.show()
    sys.exit(app.exec_())

