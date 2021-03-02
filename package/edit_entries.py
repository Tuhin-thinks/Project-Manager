# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_entries.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 526)
        MainWindow.setStyleSheet("QPushButton { \n"
"background-color:rgb(51, 153, 255); \n"
"border: 4px solid white;\n"
"padding: 6px 10px;\n"
"font: 75 12pt \"System\";\n"
"}\n"
"#centralwidget{\n"
"border: 2px solid cyan;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(153, 245, 230, 255), stop:0.09 rgba(220, 246, 236, 255), stop:0.14 rgba(150, 239, 246, 255), stop:0.187702 rgba(73, 187, 241, 255), stop:0.25 rgba(40, 151, 232, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(162, 249, 213, 237), stop:0.47 rgba(109, 168, 162, 227), stop:0.58 rgba(186, 232, 191, 232), stop:0.65 rgba(255, 255, 255, 255), stop:0.75 rgba(46, 142, 222, 255), stop:0.805 rgba(117, 187, 218, 255), stop:0.86 rgba(175, 254, 231, 255), stop:0.925566 rgba(254, 236, 244, 255), stop:1 rgba(191, 230, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(153, 245, 230, 255), stop:0.09 rgba(220, 246, 236, 255), stop:0.14 rgba(150, 239, 246, 255), stop:0.187702 rgba(73, 187, 241, 255), stop:0.25 rgba(40, 151, 232, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(162, 249, 213, 237), stop:0.47 rgba(109, 168, 162, 227), stop:0.58 rgba(186, 232, 191, 232), stop:0.65 rgba(255, 255, 255, 255), stop:0.75 rgba(46, 142, 222, 255), stop:0.805 rgba(117, 187, 218, 255), stop:0.86 rgba(175, 254, 231, 255), stop:0.925566 rgba(254, 236, 244, 255), stop:1 rgba(191, 230, 255, 255));\n"
"border: 3px solid white;\n"
"padding: 6px 10px;\n"
"font: 75 16pt \"System\";\n"
"}\n"
"\n"
"QTextEdit{\n"
"border:2px dot-dot-dash;\n"
"border-top-style: solid;\n"
"border-color: blue;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 2px solid grey;\n"
"border-radius: 2px 2px;\n"
"}\n"
"\n"
"QLabel{\n"
"font: 10pt \"MS Gothic\";\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widgetlinedit = QtWidgets.QWidget(self.centralwidget)
        self.widgetlinedit.setMinimumSize(QtCore.QSize(650, 200))
        self.widgetlinedit.setStyleSheet("border: 2px solid balck;")
        self.widgetlinedit.setObjectName("widgetlinedit")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widgetlinedit)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.lineEdit_projectname = QtWidgets.QLineEdit(self.widgetlinedit)
        self.lineEdit_projectname.setMinimumSize(QtCore.QSize(500, 0))
        self.lineEdit_projectname.setObjectName("lineEdit_projectname")
        self.gridLayout_2.addWidget(self.lineEdit_projectname, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widgetlinedit)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widgetlinedit)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_completestatus = QtWidgets.QComboBox(self.widgetlinedit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_completestatus.sizePolicy().hasHeightForWidth())
        self.comboBox_completestatus.setSizePolicy(sizePolicy)
        self.comboBox_completestatus.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_completestatus.setStyleSheet("border: 2px solid grey;\n"
"border-radius: 2px 2px;")
        self.comboBox_completestatus.setObjectName("comboBox_completestatus")
        self.comboBox_completestatus.addItem("")
        self.comboBox_completestatus.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_completestatus, 3, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widgetlinedit)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widgetlinedit)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_price = QtWidgets.QLineEdit(self.widgetlinedit)
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.gridLayout_2.addWidget(self.lineEdit_price, 1, 3, 1, 1)
        self.lineEdit_submitdate = QtWidgets.QLineEdit(self.widgetlinedit)
        self.lineEdit_submitdate.setObjectName("lineEdit_submitdate")
        self.gridLayout_2.addWidget(self.lineEdit_submitdate, 2, 3, 1, 1)
        self.comboBox_paymentstatus = QtWidgets.QComboBox(self.widgetlinedit)
        self.comboBox_paymentstatus.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_paymentstatus.setMinimumContentsLength(10)
        self.comboBox_paymentstatus.setObjectName("comboBox_paymentstatus")
        self.comboBox_paymentstatus.addItem("")
        self.comboBox_paymentstatus.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_paymentstatus, 3, 6, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widgetlinedit)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 4, 1, 1)
        self.horizontalLayout.addWidget(self.widgetlinedit)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(250, 16777215))
        self.groupBox.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_confirm = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.gridLayout.addWidget(self.pushButton_confirm, 0, 0, 1, 1)
        self.pushButton_cancel = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout.addWidget(self.pushButton_cancel, 2, 0, 1, 1)
        self.pushButton_delete = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout.addWidget(self.pushButton_delete, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.textEdit_projectdef = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_projectdef.setStyleSheet("font: 10pt \"MS PGothic\";")
        self.textEdit_projectdef.setObjectName("textEdit_projectdef")
        self.verticalLayout.addWidget(self.textEdit_projectdef)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_projectname, self.lineEdit_price)
        MainWindow.setTabOrder(self.lineEdit_price, self.lineEdit_submitdate)
        MainWindow.setTabOrder(self.lineEdit_submitdate, self.comboBox_completestatus)
        MainWindow.setTabOrder(self.comboBox_completestatus, self.textEdit_projectdef)
        MainWindow.setTabOrder(self.textEdit_projectdef, self.pushButton_confirm)
        MainWindow.setTabOrder(self.pushButton_confirm, self.pushButton_delete)
        MainWindow.setTabOrder(self.pushButton_delete, self.pushButton_cancel)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EDIT ENTRY"))
        self.label_3.setText(_translate("MainWindow", "Submit Date"))
        self.label.setText(_translate("MainWindow", "Project Name"))
        self.comboBox_completestatus.setItemText(0, _translate("MainWindow", "complete"))
        self.comboBox_completestatus.setItemText(1, _translate("MainWindow", "pending"))
        self.label_4.setText(_translate("MainWindow", "Complete Status"))
        self.label_2.setText(_translate("MainWindow", "Price"))
        self.comboBox_paymentstatus.setItemText(0, _translate("MainWindow", "Pending"))
        self.comboBox_paymentstatus.setItemText(1, _translate("MainWindow", "Cleared"))
        self.label_6.setText(_translate("MainWindow", "Payment Staus"))
        self.groupBox.setTitle(_translate("MainWindow", "Options"))
        self.pushButton_confirm.setText(_translate("MainWindow", "Confirm"))
        self.pushButton_cancel.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_delete.setText(_translate("MainWindow", "Delete"))
        self.label_5.setText(_translate("MainWindow", "Project Definition"))
