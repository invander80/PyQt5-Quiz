# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_maindzFsAC.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resorces.bg_img

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 700)
        MainWindow.setMinimumSize(QSize(1100, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainContainer = QFrame(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        self.mainContainer.setStyleSheet(u"QFrame {\n"
"	background-color: #1e2124;\n"
"	border-radius:10px;\n"
"\n"
"\n"
"}")
        self.mainContainer.setFrameShape(QFrame.StyledPanel)
        self.mainContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mainContainer)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.toolContainer = QFrame(self.mainContainer)
        self.toolContainer.setObjectName(u"toolContainer")
        self.toolContainer.setMaximumSize(QSize(16777215, 30))
        self.toolContainer.setSizeIncrement(QSize(0, 0))
        self.toolContainer.setStyleSheet(u"QFrame {\n"
"	background-color: #393e45;\n"
"}")
        self.toolContainer.setFrameShape(QFrame.NoFrame)
        self.toolContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.toolContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 1, 1, 1)
        self.appName = QLabel(self.toolContainer)
        self.appName.setObjectName(u"appName")
        self.appName.setStyleSheet(u"QLabel {\n"
"	font: 700 10pt \"Unispace\";\n"
"	color: rgb(217, 236, 255);\n"
"}")

        self.horizontalLayout_2.addWidget(self.appName)

        self.minBtn = QPushButton(self.toolContainer)
        self.minBtn.setObjectName(u"minBtn")
        self.minBtn.setMinimumSize(QSize(28, 28))
        self.minBtn.setMaximumSize(QSize(28, 28))
        self.minBtn.setStyleSheet(u"QPushButton {\n"
"\n"
"background-color:rgb(28, 255, 134);\n"
"border-radius:14px;\n"
"border: 2px solid #1e2124;\n"
"color:#d9ecff;\n"
"	font: 700 9pt \"Unispace\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(120, 255, 163);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(115, 255, 73);\n"
"	border: 2px solid #d9ecff;\n"
"}")

        self.horizontalLayout_2.addWidget(self.minBtn)

        self.exitBtn = QPushButton(self.toolContainer)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setMinimumSize(QSize(28, 28))
        self.exitBtn.setMaximumSize(QSize(28, 28))
        self.exitBtn.setStyleSheet(u"QPushButton {\n"
"\n"
"background-color:rgb(255, 96, 96);\n"
"border-radius:14px;\n"
"border: 2px solid #1e2124;\n"
"color:#d9ecff;\n"
"	font: 700 9pt \"Unispace\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 156, 156);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 61, 61);\n"
"	border: 2px solid #d9ecff;\n"
"}")

        self.horizontalLayout_2.addWidget(self.exitBtn)


        self.verticalLayout.addWidget(self.toolContainer)

        self.questContainer = QFrame(self.mainContainer)
        self.questContainer.setObjectName(u"questContainer")
        self.questContainer.setStyleSheet(u"QFrame {\n"
"\n"
"background-color:#303338;\n"
"border-radius:0px;\n"
"		\n"
"	border-image: url(:/main/bg0004.png);\n"
"\n"
"}")
        self.questContainer.setFrameShape(QFrame.NoFrame)
        self.questContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.questContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.questionLbl = QLabel(self.questContainer)
        self.questionLbl.setObjectName(u"questionLbl")
        self.questionLbl.setStyleSheet(u"QLabel {\n"
"background:none;\n"
"	font: 700 18pt \"Unispace\";\n"
"	color: rgb(217, 236, 255);\n"
"\n"
"		border-image: none;\n"
"        background-repeat: no-repeat; \n"
"\n"
"}")
        self.questionLbl.setTextFormat(Qt.AutoText)
        self.questionLbl.setScaledContents(False)
        self.questionLbl.setAlignment(Qt.AlignCenter)
        self.questionLbl.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.questionLbl)

        self.answBtn1 = QPushButton(self.questContainer)
        self.answBtn1.setObjectName(u"answBtn1")
        self.answBtn1.setMinimumSize(QSize(0, 40))
        self.answBtn1.setStyleSheet(u"QPushButton {\n"
"\n"
"background-color:#303338;\n"
"border-radius:10px;\n"
"border: 2px solid #1e2124;\n"
"color:#d9ecff;\n"
"	font: 700 9pt \"Unispace\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #393e45;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #1e2124;\n"
"	border: 2px solid #d9ecff;\n"
"}")

        self.verticalLayout_2.addWidget(self.answBtn1)

        self.answBtn2 = QPushButton(self.questContainer)
        self.answBtn2.setObjectName(u"answBtn2")
        self.answBtn2.setMinimumSize(QSize(0, 40))
        self.answBtn2.setStyleSheet(u"QPushButton {\n"
"\n"
"background-color:#303338;\n"
"border-radius:10px;\n"
"border: 2px solid #1e2124;\n"
"color:#d9ecff;\n"
"	font: 700 9pt \"Unispace\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #393e45;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #1e2124;\n"
"	border: 2px solid #d9ecff;\n"
"}")

        self.verticalLayout_2.addWidget(self.answBtn2)

        self.answBtn3 = QPushButton(self.questContainer)
        self.answBtn3.setObjectName(u"answBtn3")
        self.answBtn3.setMinimumSize(QSize(0, 40))
        self.answBtn3.setStyleSheet(u"QPushButton {\n"
"\n"
"background-color:#303338;\n"
"border-radius:10px;\n"
"border: 2px solid #1e2124;\n"
"color:#d9ecff;\n"
"	font: 700 9pt \"Unispace\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #393e45;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #1e2124;\n"
"	border: 2px solid #d9ecff;\n"
"}")

        self.verticalLayout_2.addWidget(self.answBtn3)

        self.answBtn4 = QPushButton(self.questContainer)
        self.answBtn4.setObjectName(u"answBtn4")
        self.answBtn4.setMinimumSize(QSize(0, 40))
        self.answBtn4.setStyleSheet(u"QPushButton {\n"
"\n"
"background-color:#303338;\n"
"border-radius:10px;\n"
"border: 2px solid #1e2124;\n"
"color:#d9ecff;\n"
"	font: 700 9pt \"Unispace\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #393e45;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #1e2124;\n"
"	border: 2px solid #d9ecff;\n"
"}")

        self.verticalLayout_2.addWidget(self.answBtn4)

        self.nextBtn = QPushButton(self.questContainer)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setMinimumSize(QSize(120, 40))
        self.nextBtn.setMaximumSize(QSize(120, 16777215))
        self.nextBtn.setStyleSheet(u"QPushButton {\n"
"\n"
"background-color:#303338;\n"
"border-radius:10px;\n"
"border: 2px solid #1e2124;\n"
"color:#d9ecff;\n"
"	font: 700 9pt \"Unispace\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #393e45;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #1e2124;\n"
"	border: 2px solid #d9ecff;\n"
"}")

        self.verticalLayout_2.addWidget(self.nextBtn, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.questContainer)

        self.scoreContainer = QFrame(self.mainContainer)
        self.scoreContainer.setObjectName(u"scoreContainer")
        self.scoreContainer.setMaximumSize(QSize(16777215, 30))
        self.scoreContainer.setStyleSheet(u"QFrame {\n"
"background-color: #393e45;\n"
"}")
        self.scoreContainer.setFrameShape(QFrame.NoFrame)
        self.scoreContainer.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.scoreContainer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 1, 1, 1)
        self.label = QLabel(self.scoreContainer)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(170, 16777215))
        self.label.setStyleSheet(u"QLabel {\n"
"	font: 700 10pt \"Unispace\";\n"
"	color: rgb(217, 236, 255);\n"
"}")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.scoreContainer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(150, 16777215))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font: 700 10pt \"Unispace\";\n"
"	color: rgb(217, 236, 255);\n"
"}")

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.label_2 = QLabel(self.scoreContainer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 0))
        self.label_2.setMaximumSize(QSize(150, 16777215))
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font: 700 10pt \"Unispace\";\n"
"	color: rgb(217, 236, 255);\n"
"}")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_4 = QLabel(self.scoreContainer)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(50, 16777215))
        self.label_4.setStyleSheet(u"QLabel {\n"
"	font: 700 10pt \"Unispace\";\n"
"	color: lime;\n"
"}")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.label_5 = QLabel(self.scoreContainer)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"	font: 700 10pt \"Unispace\";\n"
"	color: red;\n"
"}")

        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)


        self.verticalLayout.addWidget(self.scoreContainer)


        self.horizontalLayout.addWidget(self.mainContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.appName.setText(QCoreApplication.translate("MainWindow", u"QuizApp", None))
        self.minBtn.setText("")
        self.exitBtn.setText("")
        self.questionLbl.setText(QCoreApplication.translate("MainWindow", u"Frage", None))
        self.answBtn1.setText(QCoreApplication.translate("MainWindow", u"Antwort 1", None))
        self.answBtn2.setText(QCoreApplication.translate("MainWindow", u"Antwort 2", None))
        self.answBtn3.setText(QCoreApplication.translate("MainWindow", u"Antwort 3", None))
        self.answBtn4.setText(QCoreApplication.translate("MainWindow", u"Antwort 4", None))
        self.nextBtn.setText(QCoreApplication.translate("MainWindow", u"N\u00e4chste", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Score \u00dcberblick", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Falsche Antworten:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Richtige Antworten:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

