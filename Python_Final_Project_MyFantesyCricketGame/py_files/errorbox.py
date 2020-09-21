# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'errorbox.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_error_box(object):
    def setupUi(self, error_box):
        error_box.setObjectName("error_box")
        error_box.resize(378, 101)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(error_box.sizePolicy().hasHeightForWidth())
        error_box.setSizePolicy(sizePolicy)
        error_box.setMinimumSize(QtCore.QSize(378, 101))
        error_box.setMaximumSize(QtCore.QSize(378, 101))
        self.label_2 = QtWidgets.QLabel(error_box)
        self.label_2.setGeometry(QtCore.QRect(9, 9, 16, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.error_ok = QtWidgets.QPushButton(error_box)
        self.error_ok.setEnabled(True)
        self.error_ok.setGeometry(QtCore.QRect(170, 61, 72, 21))
        self.error_ok.setAutoFillBackground(False)
        self.error_ok.setStyleSheet("")
        self.error_ok.setText("OK")
        self.error_ok.setIconSize(QtCore.QSize(60, 24))
        self.error_ok.setAutoDefault(True)
        self.error_ok.setDefault(False)
        self.error_ok.setFlat(False)
        self.error_ok.setObjectName("error_ok")
        self.error_msg = QtWidgets.QLabel(error_box)
        self.error_msg.setGeometry(QtCore.QRect(70, 10, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.error_msg.setFont(font)
        self.error_msg.setTextFormat(QtCore.Qt.AutoText)
        self.error_msg.setWordWrap(False)
        self.error_msg.setIndent(0)
        self.error_msg.setObjectName("error_msg")
        self.label_3 = QtWidgets.QLabel(error_box)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 47, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(1, 0))
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_3.setPixmap(QtGui.QPixmap("../icons/crosslogo.png"))
        self.label_3.setObjectName("label_3")
        self.label_2.raise_()
        self.error_msg.raise_()
        self.label_3.raise_()
        self.error_ok.raise_()

        self.retranslateUi(error_box)
        self.error_ok.clicked.connect(self.error_msg.clear)
        self.error_ok.clicked.connect(error_box.close)
        QtCore.QMetaObject.connectSlotsByName(error_box)

    def retranslateUi(self, error_box):
        _translate = QtCore.QCoreApplication.translate
        error_box.setWindowTitle(_translate("error_box", "Error"))
        self.error_msg.setText(_translate("error_box", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    error_box = QtWidgets.QDialog()
    ui = Ui_error_box()
    ui.setupUi(error_box)
    error_box.show()
    sys.exit(app.exec_())