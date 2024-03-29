# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_manager.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(972, 633)
        MainWindow.setStyleSheet("#centralwidget{\n"
"border: 2px solid cyan;\n"
"background-color: white;\n"
"background-image: url(./package/images/on-computer.jpg);\n"
"background-repeat: no-repeat;\n"
"background-position: right;\n"
"background-clip: padding;\n"
"}\n"
"QTextEdit{\n"
"border:2px dot-dot-dash;\n"
"border-top-style: solid;\n"
"border-color: blue;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_is_paid = QtWidgets.QComboBox(self.frame)
        self.comboBox_is_paid.setMaximumSize(QtCore.QSize(90, 16777215))
        self.comboBox_is_paid.setObjectName("comboBox_is_paid")
        self.comboBox_is_paid.addItem("")
        self.comboBox_is_paid.addItem("")
        self.gridLayout.addWidget(self.comboBox_is_paid, 6, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 3)
        self.dateEdit_submit_date = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_submit_date.setObjectName("dateEdit_submit_date")
        self.gridLayout.addWidget(self.dateEdit_submit_date, 3, 3, 1, 1)
        self.textEdit_project_definition = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_project_definition.setFont(font)
        self.textEdit_project_definition.setStyleSheet("QTextEdit{\n"
"    background-color: rgba(255,255,255,65);\n"
"}")
        self.textEdit_project_definition.setObjectName("textEdit_project_definition")
        self.gridLayout.addWidget(self.textEdit_project_definition, 7, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_chars_display = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setItalic(True)
        self.label_chars_display.setFont(font)
        self.label_chars_display.setStyleSheet("QLabel{\n"
"    background-color: rgba(255,255,255,200);\n"
"    border: 2px solid rgba(255,255,255,100);\n"
"    border-radius: 10;\n"
"}")
        self.label_chars_display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_chars_display.setObjectName("label_chars_display")
        self.horizontalLayout.addWidget(self.label_chars_display)
        self.gridLayout.addWidget(self.frame_3, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEdit_project_name = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_project_name.setMaxLength(30)
        self.lineEdit_project_name.setObjectName("lineEdit_project_name")
        self.gridLayout.addWidget(self.lineEdit_project_name, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.comboBox_is_completed = QtWidgets.QComboBox(self.frame)
        self.comboBox_is_completed.setMaximumSize(QtCore.QSize(90, 16777215))
        self.comboBox_is_completed.setObjectName("comboBox_is_completed")
        self.comboBox_is_completed.addItem("")
        self.comboBox_is_completed.addItem("")
        self.gridLayout.addWidget(self.comboBox_is_completed, 2, 3, 1, 1)
        self.label_project_descr = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_project_descr.setFont(font)
        self.label_project_descr.setObjectName("label_project_descr")
        self.gridLayout.addWidget(self.label_project_descr, 7, 0, 1, 1)
        self.lineEdit_project_price = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_project_price.setObjectName("lineEdit_project_price")
        self.gridLayout.addWidget(self.lineEdit_project_price, 4, 3, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_price_message = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setItalic(True)
        self.label_price_message.setFont(font)
        self.label_price_message.setStyleSheet("QLabel{\n"
"    background-color: rgba(255,255,255,200);\n"
"    border: 2px solid rgba(255,255,255,100);\n"
"    border-radius: 10;\n"
"}")
        self.label_price_message.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_price_message.setObjectName("label_price_message")
        self.horizontalLayout_2.addWidget(self.label_price_message)
        self.gridLayout.addWidget(self.frame_4, 5, 3, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_addproject = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_addproject.sizePolicy().hasHeightForWidth())
        self.pushButton_addproject.setSizePolicy(sizePolicy)
        self.pushButton_addproject.setStyleSheet("QPushButton { \n"
"color: yellow; /*same as the border color*/\n"
"background-color: rgb(0, 0, 0);\n"
"border: 2px solid yellow;\n"
"border-radius: 20;\n"
"padding: 6px 10px;\n"
"font: 63 12pt \"Yrsa\";\n"
"}\n"
"QPushButton:pressed:hover{ \n"
"color: green; /*same as the border color*/\n"
"background-color: rgb(0, 0, 0);\n"
"border: 2px solid black;\n"
"border-bottom: 2px solid green;\n"
"border-radius: 20;\n"
"font: 75 16pt \"Yrsa\";\n"
"}")
        self.pushButton_addproject.setObjectName("pushButton_addproject")
        self.gridLayout_2.addWidget(self.pushButton_addproject, 0, 0, 1, 1)
        self.pushButton_editentriest = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_editentriest.setStyleSheet("QPushButton { \n"
"color: yellow; /*same as the border color*/\n"
"background-color: rgb(0, 0, 0);\n"
"border: 2px solid yellow;\n"
"border-radius: 20;\n"
"padding: 6px 10px;\n"
"font: 63 12pt \"Yrsa\";\n"
"}\n"
"QPushButton:pressed:hover{ \n"
"color: green; /*same as the border color*/\n"
"background-color: rgb(0, 0, 0);\n"
"border: 2px solid black;\n"
"border-bottom: 2px solid green;\n"
"border-radius: 20;\n"
"font: 75 16pt \"Yrsa\";\n"
"padding: 10;\n"
"}")
        self.pushButton_editentriest.setObjectName("pushButton_editentriest")
        self.gridLayout_2.addWidget(self.pushButton_editentriest, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 2, 1, 1, 1)
        self.label_header = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_header.setFont(font)
        self.label_header.setAlignment(QtCore.Qt.AlignCenter)
        self.label_header.setObjectName("label_header")
        self.gridLayout_3.addWidget(self.label_header, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 972, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setFocusPolicy(QtCore.Qt.TabFocus)
        self.menuMenu.setObjectName("menuMenu")
        self.menuAdd_Project_Ideas = QtWidgets.QMenu(self.menubar)
        self.menuAdd_Project_Ideas.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menuAdd_Project_Ideas.setObjectName("menuAdd_Project_Ideas")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionCopy_Text = QtWidgets.QAction(MainWindow)
        self.actionCopy_Text.setObjectName("actionCopy_Text")
        self.actionPaste_Text = QtWidgets.QAction(MainWindow)
        self.actionPaste_Text.setObjectName("actionPaste_Text")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClose_File = QtWidgets.QAction(MainWindow)
        self.actionClose_File.setObjectName("actionClose_File")
        self.actionDecrease_Project_Counter = QtWidgets.QAction(MainWindow)
        self.actionDecrease_Project_Counter.setObjectName("actionDecrease_Project_Counter")
        self.actionExplore = QtWidgets.QAction(MainWindow)
        self.actionExplore.setObjectName("actionExplore")
        self.actionReport = QtWidgets.QAction(MainWindow)
        self.actionReport.setObjectName("actionReport")
        self.actionNew_Idea = QtWidgets.QAction(MainWindow)
        self.actionNew_Idea.setObjectName("actionNew_Idea")
        self.actionSee_Ideas = QtWidgets.QAction(MainWindow)
        self.actionSee_Ideas.setObjectName("actionSee_Ideas")
        self.actionEdit_Ideas = QtWidgets.QAction(MainWindow)
        self.actionEdit_Ideas.setObjectName("actionEdit_Ideas")
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionClose_File)
        self.menuMenu.addAction(self.actionExplore)
        self.menuMenu.addAction(self.actionReport)
        self.menuAdd_Project_Ideas.addAction(self.actionNew_Idea)
        self.menuAdd_Project_Ideas.addAction(self.actionSee_Ideas)
        self.menuAdd_Project_Ideas.addAction(self.actionEdit_Ideas)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAdd_Project_Ideas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_project_name, self.comboBox_is_completed)
        MainWindow.setTabOrder(self.comboBox_is_completed, self.dateEdit_submit_date)
        MainWindow.setTabOrder(self.dateEdit_submit_date, self.lineEdit_project_price)
        MainWindow.setTabOrder(self.lineEdit_project_price, self.comboBox_is_paid)
        MainWindow.setTabOrder(self.comboBox_is_paid, self.textEdit_project_definition)
        MainWindow.setTabOrder(self.textEdit_project_definition, self.pushButton_addproject)
        MainWindow.setTabOrder(self.pushButton_addproject, self.pushButton_editentriest)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Project Manager-by Tuhin"))
        self.comboBox_is_paid.setItemText(0, _translate("MainWindow", "pending"))
        self.comboBox_is_paid.setItemText(1, _translate("MainWindow", "cleared"))
        self.label_4.setText(_translate("MainWindow", "Save by name (max. 30 chars):"))
        self.textEdit_project_definition.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Completed ?"))
        self.label.setText(_translate("MainWindow", "Paid ?"))
        self.label_chars_display.setText(_translate("MainWindow", "0/30 characters"))
        self.label_2.setText(_translate("MainWindow", "Submission By:"))
        self.label_5.setText(_translate("MainWindow", "Project Price:"))
        self.comboBox_is_completed.setItemText(0, _translate("MainWindow", "pending"))
        self.comboBox_is_completed.setItemText(1, _translate("MainWindow", "complete"))
        self.label_project_descr.setText(_translate("MainWindow", "Project Description:"))
        self.label_price_message.setText(_translate("MainWindow", "<html><head/><body><p>price unit: <span style=\" font-weight:600;\">USD</span>.</p></body></html>"))
        self.pushButton_addproject.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">PRESS THIS AT THE END</span></p><p><br/></p><p><span style=\" color:#000000;\">TO ADD THE PROJECT TO THE RECORDS</span></p></body></html>"))
        self.pushButton_addproject.setText(_translate("MainWindow", "Save project"))
        self.pushButton_editentriest.setToolTip(_translate("MainWindow", "<html><head/><body><p>Edit Entries in already in the database</p></body></html>"))
        self.pushButton_editentriest.setText(_translate("MainWindow", "Edit Saved Entries"))
        self.label_header.setText(_translate("MainWindow", "PROJECT MANAGEMENT SOFTWARE"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuAdd_Project_Ideas.setTitle(_translate("MainWindow", "Add Project Ideas"))
        self.actionCopy_Text.setText(_translate("MainWindow", "Copy Text"))
        self.actionPaste_Text.setText(_translate("MainWindow", "Paste Text"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose_File.setText(_translate("MainWindow", "Close File"))
        self.actionDecrease_Project_Counter.setText(_translate("MainWindow", "Decrease Project Counter"))
        self.actionExplore.setText(_translate("MainWindow", "Explore"))
        self.actionExplore.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionReport.setText(_translate("MainWindow", "Report"))
        self.actionNew_Idea.setText(_translate("MainWindow", "New Idea"))
        self.actionNew_Idea.setShortcut(_translate("MainWindow", "Ctrl+Shift+N"))
        self.actionSee_Ideas.setText(_translate("MainWindow", "See Ideas"))
        self.actionSee_Ideas.setShortcut(_translate("MainWindow", "Ctrl+Shift+V"))
        self.actionEdit_Ideas.setText(_translate("MainWindow", "Edit Ideas"))
        self.actionEdit_Ideas.setShortcut(_translate("MainWindow", "Ctrl+Shift+X"))
