# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progressvncgCF.ui'
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
        Form.resize(599, 600)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainContainer = QFrame(Form)
        self.mainContainer.setObjectName(u"mainContainer")
        self.mainContainer.setFrameShape(QFrame.StyledPanel)
        self.mainContainer.setFrameShadow(QFrame.Raised)
        self.proggressFrm = QFrame(self.mainContainer)
        self.proggressFrm.setObjectName(u"proggressFrm")
        self.proggressFrm.setGeometry(QRect(70, 70, 440, 440))
        self.proggressFrm.setMaximumSize(QSize(440, 440))
        self.proggressFrm.setStyleSheet(u"")
        self.proggressFrm.setFrameShape(QFrame.StyledPanel)
        self.proggressFrm.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.mainContainer)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 90, 400, 400))
        self.label.setMinimumSize(QSize(400, 400))
        self.label.setMaximumSize(QSize(400, 400))
        self.label.setSizeIncrement(QSize(0, 0))
        self.label.setPixmap(QPixmap(u":/main/progress.png"))
        self.label.setScaledContents(True)
        self.proggressFrm_2 = QFrame(self.mainContainer)
        self.proggressFrm_2.setObjectName(u"proggressFrm_2")
        self.proggressFrm_2.setGeometry(QRect(60, 60, 460, 460))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proggressFrm_2.sizePolicy().hasHeightForWidth())
        self.proggressFrm_2.setSizePolicy(sizePolicy)
        self.proggressFrm_2.setMinimumSize(QSize(460, 460))
        self.proggressFrm_2.setMaximumSize(QSize(460, 460))
        self.proggressFrm_2.setStyleSheet(u"QFrame {\n"
"background:#303338;\n"
"border-radius:230px;\n"
"border: 10px solid black;\n"
"}")
        self.proggressFrm_2.setFrameShape(QFrame.StyledPanel)
        self.proggressFrm_2.setFrameShadow(QFrame.Raised)
        self.percentLbl = QLabel(self.mainContainer)
        self.percentLbl.setObjectName(u"percentLbl")
        self.percentLbl.setGeometry(QRect(200, 230, 191, 121))
        self.percentLbl.setStyleSheet(u"QLabel {\n"
"	font: 700 20pt \"Unispace\";\n"
"	color: rgb(217, 236, 255);\n"
"}")
        self.percentLbl.setAlignment(Qt.AlignCenter)
        self.proggressFrm_2.raise_()
        self.proggressFrm.raise_()
        self.label.raise_()
        self.percentLbl.raise_()

        self.horizontalLayout.addWidget(self.mainContainer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.percentLbl.setText(QCoreApplication.translate("Form", u"0%", None))
    # retranslateUi

