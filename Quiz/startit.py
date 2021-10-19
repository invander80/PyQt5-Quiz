from ui.ui_start import *
from quiz import *
from data.animation import Animation
from data.functions import Functions

class StartApp(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.start = Ui_Form()
        self.start.setupUi(self)
        self.mw = MainWindow(self)
        self._anim = Animation(self)
        self.func = Functions(self)

        self.start.exitBtn.clicked.connect(self.close)
        self.start.minBtn.clicked.connect(self.showMinimized)
        self.start.startBtn.clicked.connect(self.openWin)
        self.showQuestNum()
        self.start.appName.mouseMoveEvent = self.moveWin
        self.func.removeTitle()
        self.setShadow()
 #       self._anim.animateStartBtn()

### FUNKTIONEN /////////////////////////////////////////////////////////////////////////////////////////////////////////
    ###===>>> MAIN ÖFFNEN
    def openWin(self):
        self.close()
        self.mw.setQuest()
        self.mw.show()

    ###===>>> FENSTER BEWEGEN (ÜBER DAS LABEL IN DER TOOLBAR)
    def moveWin(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    ###===>>> TITLE BAR ENTFERNEN
    def setShadow(self):
        self.bshadow = QGraphicsDropShadowEffect()
        self.bshadow.setBlurRadius(50)
        self.bshadow.setXOffset(0)
        self.bshadow.setYOffset(0)
        self.bshadow.setColor(QColor("#1e2124"))
        self.start.startBtn.setGraphicsEffect(self.bshadow)

    ###===>>> ANZEIGEN WIEVIELE FRAGEN SICH IN DER JSON FILE BEFINDEN
    def showQuestNum(self):
        self.start.label.setText("Anzahl der Fragen " + str(len(self.mw.question)))







