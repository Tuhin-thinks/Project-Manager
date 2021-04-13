# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_ideas.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(748, 519)
        MainWindow.setMinimumSize(QtCore.QSize(748, 519))
        MainWindow.setMaximumSize(QtCore.QSize(748, 519))
        MainWindow.setStyleSheet("QLabel{\n"
"font: 13pt \"URW Gothic L\";\n"
"}\n"
"\n"
"QPushButton{\n"
"border: 2px solid black;\n"
"border-radius: 5px 5px;\n"
"padding: 5px 10px;\n"
"background-color: rgb(211, 215, 207);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed{\n"
"background-color: rgb(46, 52, 54);\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"QLineEdit{\n"
"border: 1px solid black;\n"
"border-radius: 2px 2px;\n"
"}\n"
"QPushbutton:pressed{\n"
"border: 1px solid black;\n"
"border-radius: 3px 5px;\n"
"padding: 3px 7px;\n"
"background-color: rgb(211, 215, 207);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 4, 1, 1, 1)
        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout.addWidget(self.pushButton_cancel, 4, 2, 1, 1)
        self.textEdit_details = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_details.setObjectName("textEdit_details")
        self.gridLayout.addWidget(self.textEdit_details, 3, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_projectname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_projectname.setStyleSheet("padding: 2px 8px;")
        self.lineEdit_projectname.setInputMask("")
        self.lineEdit_projectname.setObjectName("lineEdit_projectname")
        self.horizontalLayout.addWidget(self.lineEdit_projectname)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_completestatus = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_completestatus.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_completestatus.setObjectName("comboBox_completestatus")
        self.comboBox_completestatus.addItem("")
        self.comboBox_completestatus.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_completestatus)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_projectname, self.comboBox_completestatus)
        MainWindow.setTabOrder(self.comboBox_completestatus, self.textEdit_details)
        MainWindow.setTabOrder(self.textEdit_details, self.pushButton_add)
        MainWindow.setTabOrder(self.pushButton_add, self.pushButton_cancel)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Idea Details"))
        self.pushButton_add.setText(_translate("MainWindow", "Add"))
        self.pushButton_cancel.setText(_translate("MainWindow", "Cancel"))
        self.label.setText(_translate("MainWindow", "Give Your Idea A Call-Name:"))
        self.lineEdit_projectname.setPlaceholderText(_translate("MainWindow", "In Short(under 30 characters),ex.: "
                                                                              "File Manager, Document Viewer"))
        self.label_2.setText(_translate("MainWindow", "Set Complete Status:"))
        self.comboBox_completestatus.setItemText(0, _translate("MainWindow", "pending"))
        self.comboBox_completestatus.setItemText(1, _translate("MainWindow", "complete"))
