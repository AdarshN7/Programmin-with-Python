# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_New(object):
    def setupUi(self, New):
        New.setObjectName("New")
        New.setWindowModality(QtCore.Qt.NonModal)
        New.resize(300, 97)
        New.setMinimumSize(QtCore.QSize(300, 97))
        New.setMaximumSize(QtCore.QSize(300, 97))
        self.label = QtWidgets.QLabel(New)
        self.label.setGeometry(QtCore.QRect(60, 10, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.new_team = QtWidgets.QLineEdit(New)
        self.new_team.setGeometry(QtCore.QRect(60, 30, 221, 20))
        self.new_team.setObjectName("new_team")
        self.label_2 = QtWidgets.QLabel(New)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 51, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../icons/new_icon.png"))
        self.label_2.setObjectName("label_2")
        self.save_bt = QtWidgets.QPushButton(New)
        self.save_bt.setGeometry(QtCore.QRect(200, 60, 75, 24))
        self.save_bt.setObjectName("save_bt")

        self.retranslateUi(New)
        QtCore.QMetaObject.connectSlotsByName(New)

    def retranslateUi(self, New):
        _translate = QtCore.QCoreApplication.translate
        New.setWindowTitle(_translate("New", "New"))
        self.label.setText(_translate("New", "Input name of  Team"))
        self.save_bt.setText(_translate("New", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    New = QtWidgets.QDialog()
    ui = Ui_New()
    ui.setupUi(New)
    New.show()
    sys.exit(app.exec_())