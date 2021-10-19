# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_startVnqlLh.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resorces.bg_img

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 700)
        Form.setMinimumSize(QSize(1000, 700))
        Form.setMaximumSize(QSize(1000, 700))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.container = QFrame(Form)
        self.container.setObjectName(u"container")
        self.container.setStyleSheet(u"QFrame {\n"
"	background-color: #1e2124;\n"
"	border-radius:10px;\n"
"}")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.container)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.toolFrm = QFrame(self.container)
        self.toolFrm.setObjectName(u"toolFrm")
        self.toolFrm.setMaximumSize(QSize(16777215, 30))
        self.toolFrm.setStyleSheet(u"QFrame {\n"
"	background-color: #393e45;\n"
"}")
        self.toolFrm.setFrameShape(QFrame.StyledPanel)
        self.toolFrm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.toolFrm)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.appName = QLabel(self.toolFrm)
        self.appName.setObjectName(u"appName")
        self.appName.setMaximumSize(QSize(16777215, 30))
        self.appName.setStyleSheet(u"QLabel {\n"
"	font: 700 10pt \"Unispace\";\n"
"	color: rgb(217, 236, 255);\n"
"}")

        self.horizontalLayout_2.addWidget(self.appName)

        self.minBtn = QPushButton(self.toolFrm)
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

        self.exitBtn = QPushButton(self.toolFrm)
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


        self.verticalLayout.addWidget(self.toolFrm)

        self.mainContainer = QFrame(self.container)
        self.mainContainer.setObjectName(u"mainContainer")
        self.mainContainer.setStyleSheet(u"QFrame {\n"
"\n"
"background-color:#303338;\n"
"border-radius:0px;\n"
"	background-image: url(:/main/bg0003.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat; \n"
"\n"
"}")
        self.mainContainer.setFrameShape(QFrame.StyledPanel)
        self.mainContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.mainContainer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.startBtn = QPushButton(self.mainContainer)
        self.startBtn.setObjectName(u"startBtn")
        self.startBtn.setMinimumSize(QSize(200, 200))
        self.startBtn.setMaximumSize(QSize(200, 200))
        self.startBtn.setStyleSheet(u"QPushButton {\n"
"\n"
"background-color:#303338;\n"
"border-radius:100px;\n"
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

        self.horizontalLayout_3.addWidget(self.startBtn)


        self.verticalLayout.addWidget(self.mainContainer)

        self.statusFrm = QFrame(self.container)
        self.statusFrm.setObjectName(u"statusFrm")
        self.statusFrm.setMaximumSize(QSize(16777215, 30))
        self.statusFrm.setStyleSheet(u"QFrame {\n"
"	background-color: #393e45;\n"
"}")
        self.statusFrm.setFrameShape(QFrame.StyledPanel)
        self.statusFrm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.statusFrm)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.label = QLabel(self.statusFrm)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(170, 16777215))
        self.label.setStyleSheet(u"QLabel {\n"
"	font: 700 10pt \"Unispace\";\n"
"	color: rgb(217, 236, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout.addWidget(self.statusFrm)


        self.horizontalLayout.addWidget(self.container)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.appName.setText(QCoreApplication.translate("Form", u"QuizApp", None))
        self.minBtn.setText("")
        self.exitBtn.setText("")
        self.startBtn.setText(QCoreApplication.translate("Form", u"QUIZ Starten", None))
        self.label.setText(QCoreApplication.translate("Form", u"Anzahl der Fragen: ", None))
    # retranslateUi

