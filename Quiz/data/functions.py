from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Functions:
    def __init__(self, parent):
        super(Functions, self).__init__()

        self.parent = parent

    ###
    def removeTitle(self):
        self.parent.setWindowFlag(Qt.FramelessWindowHint)
        self.parent.setAttribute(Qt.WA_TranslucentBackground)

        ###===>>>HAUPTFENSTER SCHATTEN SETZEN
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(20)
        self.shadow.setYOffset(0)
        self.shadow.setXOffset(0)
        self.shadow.setColor(QColor("#ade8ff"))
        self.parent.setGraphicsEffect(self.shadow)

