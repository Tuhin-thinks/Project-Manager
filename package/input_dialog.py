# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 318)
        MainWindow.setMinimumSize(QtCore.QSize(710, 318))
        MainWindow.setMaximumSize(QtCore.QSize(710, 318))
        MainWindow.setStyleSheet("#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.824, x2:1, y2:0.114, stop:0.215909 rgba(192, 27, 27, 250), stop:1 rgba(255, 255, 255, 255));\n"
"border: 2px solid black;\n"
"}\n"
"QLineEdit{\n"
"border: 2px dashed black;\n"
"border-radius: 5px;\n"
"padding: 2px;\n"
"font: 10pt \"NSimSun\";\n"
"color: rgb(0, 60, 182);\n"
"}\n"
"QPushButton {\n"
"background-color: rgb(0, 255, 255);\n"
"border: 4px solid white;\n"
"padding: 5px 10px;\n"
"font: 13pt \"Rage Italic\";\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(0, 0, 39);\n"
"color: rgb(255,255,255);\n"
"border: 6px solid blue;\n"
"padding: 5px 5px;\n"
"font: 12pt \"Rage Italic\";\n"
"}\n"
"QPushButton:!pressed:hover\n"
"{\n"
" background-color: rgba(255, 228, 75, 150);\n"
"border: 6px solid blue;\n"
"padding: 5px 5px;\n"
"font: 10pt \"Rage Italic\";\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_input = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lineEdit_input.setFont(font)
        self.lineEdit_input.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.gridLayout.addWidget(self.lineEdit_input, 4, 2, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.label_message = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_message.sizePolicy().hasHeightForWidth())
        self.label_message.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_message.setFont(font)
        self.label_message.setText("")
        self.label_message.setAlignment(QtCore.Qt.AlignCenter)
        self.label_message.setObjectName("label_message")
        self.gridLayout.addWidget(self.label_message, 1, 0, 1, 5)
        self.pushButton_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.gridLayout.addWidget(self.pushButton_confirm, 6, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 5)
        self.pushButton_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.gridLayout.addWidget(self.pushButton_reset, 6, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "INPUT DIALOG"))
        self.label.setText(_translate("MainWindow", "INPUT HERE:"))
        self.pushButton_confirm.setText(_translate("MainWindow", "CONFIRM"))
        self.pushButton_reset.setText(_translate("MainWindow", "RESET"))
