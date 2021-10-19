from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox, QGraphicsOpacityEffect)
from PyQt5 import QtCore

class Animation:
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

    ###===>>> TEXT ANIMATION
    def animateText(self):
        effect = QGraphicsOpacityEffect(self.parent.ui.questionLbl)
        self.parent.ui.questionLbl.setGraphicsEffect(effect)
        self.anim = QPropertyAnimation(effect,  b"opacity")
        self.anim.setEasingCurve(QEasingCurve.Linear)
        self.anim.setStartValue(0)
        self.anim.setDuration(3500)
        self.anim.start()

    def animateStartBtn(self):
        beffect = QGraphicsOpacityEffect(self.parent.start.startBtn)
        self.parent.start.startBtn.setGraphicsEffect(beffect)
        self.bStart = QPropertyAnimation(beffect, b"opactiy")
        self.bStart.setEasingCurve(QEasingCurve.OutBounce)
        self.bStart.setStartValue(0)
        self.bStart.setDuration(2000)
        self.bStart.start()



    ###===>>> BUTTON ANIMATION
    def animateButton(self):
        a = self.parent.width() - 40

        self.bAnim = QPropertyAnimation(self.parent.ui.answBtn1, b"size")
        self.bAnim.setStartValue(QSize(0, 0))
        self.bAnim.setEndValue(QSize(a, 40))
        self.bAnim.setDuration(2000)
        self.bAnim.setEasingCurve(QEasingCurve.OutBounce)

        self.bAnim2 = QPropertyAnimation(self.parent.ui.answBtn2, b"size")
        self.bAnim2.setStartValue(QSize(4000, 0))
        self.bAnim2.setEndValue(QSize(a, 40))
        self.bAnim2.setDuration(2000)
        self.bAnim2.setEasingCurve(QEasingCurve.InOutCubic)

        self.bAnim3 = QPropertyAnimation(self.parent.ui.answBtn3, b"size")
        self.bAnim3.setStartValue(QSize(0, 0))
        self.bAnim3.setEndValue(QSize(a, 40))
        self.bAnim3.setDuration(2000)
        self.bAnim3.setEasingCurve(QEasingCurve.OutBounce)

        self.bAnim4 = QPropertyAnimation(self.parent.ui.answBtn4, b"size")
        self.bAnim4.setStartValue(QSize(4000, 0))
        self.bAnim4.setEndValue(QSize(a, 40))
        self.bAnim4.setDuration(2000)
        self.bAnim4.setEasingCurve(QEasingCurve.InOutCubic)

        self.groupAnimation = QParallelAnimationGroup()
        self.groupAnimation.addAnimation(self.bAnim)
        self.groupAnimation.addAnimation(self.bAnim2)
        self.groupAnimation.addAnimation(self.bAnim3)
        self.groupAnimation.addAnimation(self.bAnim4)

        self.groupAnimation.start()
