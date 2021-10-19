# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_scoreicyTLA.ui'
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
        Form.resize(400, 699)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainContainer = QFrame(Form)
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
        self.toolContainer.setMinimumSize(QSize(0, 30))
        self.toolContainer.setMaximumSize(QSize(16777215, 30))
        self.toolContainer.setStyleSheet(u"QFrame {\n"
"	background-color: #393e45;\n"
"}")
        self.toolContainer.setFrameShape(QFrame.StyledPanel)
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


        self.verticalLayout.addWidget(self.toolContainer)

        self.scoreContainer = QFrame(self.mainContainer)
        self.scoreContainer.setObjectName(u"scoreContainer")
        self.scoreContainer.setStyleSheet(u"QFrame {\n"
"\n"
"background-color:#303338;\n"
"border-radius:0px;\n"
"\n"
"}")
        self.scoreContainer.setFrameShape(QFrame.StyledPanel)
        self.scoreContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.scoreContainer)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.scoreFrame = QFrame(self.scoreContainer)
        self.scoreFrame.setObjectName(u"scoreFrame")
        self.scoreFrame.setFrameShape(QFrame.StyledPanel)
        self.scoreFrame.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.scoreFrame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(50, 20, 374, 304))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.scorePercentFrm = QFrame(self.frame_5)
        self.scorePercentFrm.setObjectName(u"scorePercentFrm")
        self.scorePercentFrm.setGeometry(QRect(0, 0, 270, 270))
        self.scorePercentFrm.setStyleSheet(u"QFrame {\n"
"border-radius:135;\n"
"background-color:  red;\n"
"}")
        self.scorePercentFrm.setFrameShape(QFrame.StyledPanel)
        self.scorePercentFrm.setFrameShadow(QFrame.Raised)
        self.scorePercentLbl = QLabel(self.frame_5)
        self.scorePercentLbl.setObjectName(u"scorePercentLbl")
        self.scorePercentLbl.setGeometry(QRect(10, 10, 250, 250))
        self.scorePercentLbl.setStyleSheet(u"background:none;")
        self.scorePercentLbl.setPixmap(QPixmap(u":/main/progress.png"))
        self.scorePercentLbl.setScaledContents(True)
        self.scoreLbl = QLabel(self.scoreFrame)
        self.scoreLbl.setObjectName(u"scoreLbl")
        self.scoreLbl.setGeometry(QRect(120, 110, 141, 101))
        self.scoreLbl.setStyleSheet(u"QLabel {\n"
"background:none;\n"
"	font: 700 9pt \"Unispace\";\n"
"	color: rgb(217, 236, 255);\n"
"}")
        self.scoreLbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.scoreFrame)


        self.verticalLayout.addWidget(self.scoreContainer)

        self.scoreTxtContainer = QFrame(self.mainContainer)
        self.scoreTxtContainer.setObjectName(u"scoreTxtContainer")
        self.scoreTxtContainer.setMaximumSize(QSize(378, 305))
        self.scoreTxtContainer.setStyleSheet(u"QFrame {\n"
"\n"
"background-color:#303338;\n"
"border-radius:0px;\n"
"		\n"
"}")
        self.scoreTxtContainer.setFrameShape(QFrame.StyledPanel)
        self.scoreTxtContainer.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.scoreTxtContainer)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(0, QFormLayout.LabelRole, self.verticalSpacer)

        self.label = QLabel(self.scoreTxtContainer)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"background:none;\n"
"	font: 700 9pt \"Unispace\";\n"
"	color: rgb(217, 236, 255);\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.answeredlbl = QLabel(self.scoreTxtContainer)
        self.answeredlbl.setObjectName(u"answeredlbl")
        self.answeredlbl.setStyleSheet(u"QLabel {\n"
"background:none;\n"
"	font: 700 9pt \"Unispace\";\n"
"	color: Yellow;\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.answeredlbl)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(3, QFormLayout.LabelRole, self.verticalSpacer_2)

        self.label_5 = QLabel(self.scoreTxtContainer)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(200, 0))
        self.label_5.setMaximumSize(QSize(400, 16777215))
        self.label_5.setStyleSheet(u"QLabel {\n"
"background:none;\n"
"	font: 700 9pt \"Unispace\";\n"
"	color: rgb(217, 236, 255);\n"
"}")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.sumRightAnswerLbl = QLabel(self.scoreTxtContainer)
        self.sumRightAnswerLbl.setObjectName(u"sumRightAnswerLbl")
        self.sumRightAnswerLbl.setStyleSheet(u"QLabel {\n"
"background:none;\n"
"	font: 700 9pt \"Unispace\";\n"
"	color: rgb(85, 255, 255);\n"
"}")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.sumRightAnswerLbl)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(5, QFormLayout.LabelRole, self.verticalSpacer_3)

        self.label_2 = QLabel(self.scoreTxtContainer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"background:none;\n"
"	font: 700 9pt \"Unispace\";\n"
"	color: rgb(217, 236, 255);\n"
"}")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_2)

        self.noAnsweredLbl = QLabel(self.scoreTxtContainer)
        self.noAnsweredLbl.setObjectName(u"noAnsweredLbl")
        self.noAnsweredLbl.setStyleSheet(u"QLabel {\n"
"background:none;\n"
"	font: 700 9pt \"Unispace\";\n"
"	color: rgb(217, 236, 255);\n"
"}")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.noAnsweredLbl)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(7, QFormLayout.LabelRole, self.verticalSpacer_4)

        self.label_3 = QLabel(self.scoreTxtContainer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"background:none;\n"
"	font: 700 9pt \"Unispace\";\n"
"	color: rgb(217, 236, 255);\n"
"}")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_3)

        self.rightAnswerLbl = QLabel(self.scoreTxtContainer)
        self.rightAnswerLbl.setObjectName(u"rightAnswerLbl")
        self.rightAnswerLbl.setStyleSheet(u"QLabel {\n"
"background:none;\n"
"	font: 700 9pt \"Unispace\";\n"
"	color: lime;\n"
"}")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.rightAnswerLbl)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(9, QFormLayout.LabelRole, self.verticalSpacer_5)

        self.label_4 = QLabel(self.scoreTxtContainer)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"background:none;\n"
"	font: 700 9pt \"Unispace\";\n"
"	color: rgb(217, 236, 255);\n"
"}")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_4)

        self.wrongAnswerLbl = QLabel(self.scoreTxtContainer)
        self.wrongAnswerLbl.setObjectName(u"wrongAnswerLbl")
        self.wrongAnswerLbl.setStyleSheet(u"QLabel {\n"
"background:none;\n"
"	font: 700 9pt \"Unispace\";\n"
"	color: red;\n"
"}")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.wrongAnswerLbl)

        self.restartBtn = QPushButton(self.scoreTxtContainer)
        self.restartBtn.setObjectName(u"restartBtn")
        self.restartBtn.setMinimumSize(QSize(0, 40))
        self.restartBtn.setStyleSheet(u"QPushButton {\n"
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

        self.formLayout.setWidget(13, QFormLayout.SpanningRole, self.restartBtn)


        self.verticalLayout.addWidget(self.scoreTxtContainer)

        self.statusFm = QFrame(self.mainContainer)
        self.statusFm.setObjectName(u"statusFm")
        self.statusFm.setMaximumSize(QSize(16777215, 30))
        self.statusFm.setStyleSheet(u"QFrame {\n"
"	background-color: #393e45;\n"
"}")
        self.statusFm.setFrameShape(QFrame.StyledPanel)
        self.statusFm.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.statusFm)


        self.horizontalLayout.addWidget(self.mainContainer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.appName.setText(QCoreApplication.translate("Form", u"QuizApp Score \u00dcbersicht", None))
        self.scorePercentLbl.setText("")
        self.scoreLbl.setText(QCoreApplication.translate("Form", u"Score\n"
"0%", None))
        self.label.setText(QCoreApplication.translate("Form", u"Fragen gesamt : ", None))
        self.answeredlbl.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Richtige Antworten Gesamt : ", None))
        self.sumRightAnswerLbl.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Antworten ausgegw\u00e4hlt : ", None))
        self.noAnsweredLbl.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Richtige Antworten : ", None))
        self.rightAnswerLbl.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Falsche Antworten : ", None))
        self.wrongAnswerLbl.setText(QCoreApplication.translate("Form", u"0", None))
        self.restartBtn.setText(QCoreApplication.translate("Form", u"Beenden", None))
    # retranslateUi

