from ui.ui_score import *
from data.functions import Functions


class Score(QWidget):
    def __init__(self, parent):
        super(Score, self).__init__()

        self.parent = parent

        self.score = Ui_Form()
        self.score.setupUi(self)

        self.score.restartBtn.clicked.connect(self.restartQuiz)
        self.score.appName.mouseMoveEvent = self.moveWin

        self.func = Functions(self)
        self.func.removeTitle()

        self.timer = QTimer()
        self.timer.start(20)

        self.count = 0

###===>>> FUNKTIONEN ///////////////////////////////////////////////////////////////////////////////////////////////////
###===>>>COUNTER ZUR GESAMTLÄNGE DER RICHTIGEN ANTWORTEN LAUFEN LASSEN / LABEL % VOM SCORE ÄNDERN
    def countThrough(self):
        if self.count <= ((self.parent.rightNum-1) - (self.parent.wrongNum -1)) / self.parent.rightLen * 100:
            self.showProgress(self.count)
            self.score.scoreLbl.setText(f"Score\n{self.count}%")
            self.count += 1


###===>>> ANIMATION FÜR DEN SCORE (FRAME STYLESHEET WIRD GEÄNDERT)
    def showProgress(self, value):
        style = """
        QFrame {
                border-radius:135;
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, 
                stop:{STOP_1} red, stop:{STOP_2} lime);
                }
        """
        progress = (100 - value) / 100
        val1 = str(progress -0.001)
        val2 = str(progress)

        newStyle = style.replace("{STOP_1}", val1).replace("{STOP_2}", val2)

        self.score.scorePercentFrm.setStyleSheet(newStyle)

    def restartQuiz(self):
        self.close()
        self.parent.close()

###===>>> SCORE AUSGABEN
    def showScore(self):
        self.score.rightAnswerLbl.setText(str(self.parent.rightNum-1))
        self.score.wrongAnswerLbl.setText(str(self.parent.wrongNum-1))
        self.score.noAnsweredLbl.setText(str(self.parent.rightNum-1 + self.parent.wrongNum-1))
        self.score.answeredlbl.setText(str(len(self.parent.question)))
        self.score.sumRightAnswerLbl.setText(str(len(self.parent.lenRansw)-1))

    def moveWin(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()