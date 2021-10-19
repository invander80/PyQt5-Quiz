from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox)
import random
import json

from ui.ui_main import *
from score import Score


from data.animation import Animation
from data.stylesheet import StyleSheets
from data.functions import Functions
import collections


class MainWindow(QMainWindow):
    def __init__(self, parent):
        super(MainWindow, self).__init__()

        self.parent = parent
###===>>> IMPORTS
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.animate = Animation(self)
        self.styles = StyleSheets(self)
        self.score = Score(self)
        self.func = Functions(self)

###===>>> JSON QUIZ FILE IMPORT
        with open("quiz_questions/quiz.json", "r", encoding="utf8") as quiz:
            data = json.load(quiz)
        self.question = data["Frage"]
        self.answer = data["Antwort"]
        self.rightAnswer = data["Richtig"]

###===>>> LISTE MIT FRAGEN UND MÖGLICHEN ANTWORTEN
        self.questions = []
        for q, a in zip(self.question, self.answer):
            self.questions.append(q + a)
        print(self.questions)

        self.ransw = []  ### RANSW = RIGHT ANSWERS
        for q, ra in zip(self.question, self.rightAnswer):
            self.ransw.append(q + ra)

###===>>> LÄNGE DER RICHTIGEN ANTWORTEN (FÜR DEN SCORE)
        self.lenRansw = []
        for x in range(len(self.rightAnswer)):
            for y in range(4):
                self.lenRansw.append(self.rightAnswer[x][y])
        self.lenRansw = list(dict.fromkeys(self.lenRansw))
        self.rightLen = len(self.lenRansw) - 1

###===>>> TOOLBAR OPTIONEN
        self.ui.exitBtn.clicked.connect(self.cloesWindow)
        self.ui.minBtn.clicked.connect(self.showMinimized) ## FENSTER WIRD MINIMIERT (GRÜNER BUTTON IN DER TOOLBAR)

###===>>> TITLE BAR ENTFERNEN / SCHATTEN / FENSTER BEWEGEN
        self.func.removeTitle()
        self.setShadow()
        self.ui.appName.mouseMoveEvent = self.moveWindow

###===>>> SIZE GRIP (ALLE VIER ECKEN)
        self.gripSize = 16
        self.grips = []
        for i in range(4):
            grip = QSizeGrip(self)
            grip.resize(self.gripSize, self.gripSize)
            self.grips.append(grip)

###===>>> DIVERSES (LISTEN/BUTTONS)
        self.ui.nextBtn.clicked.connect(self.setQuest)
        self.answBtn = [self.ui.answBtn1, self.ui.answBtn2, self.ui.answBtn3, self.ui.answBtn4]
        self.check = [self.check1, self.check2, self.check3, self.check4]
        for x in range(4):
            self.answBtn[x].clicked.connect(self.check[x])

###===>>> VERSCHIEDENE WERTE
        self.rightNum = 1
        self.wrongNum = 1
        self.notAnswered = 0
        self.start = 0
        self.end = len(self.question)
        self.lockState = [True, True, True, True]


### FUNKTIONEN /////////////////////////////////////////////////////////////////////////////////////////////////////////
    ###===>>> ANZEIGEN DER FRAGEN UND ANTWORTEN
    def setQuest(self):
        self.lockState = [True, True, True, True]
        if self.end > self.start:
            self.rnd = random.randint(0, len(self.questions) - 1)

            self.righAnswer = []
            for x in range(1, 5):
                self.righAnswer.append(self.ransw[self.rnd][x])

            self.answers = []
            for x in range(1, 5):
                self.answers.append(self.questions[self.rnd][x])

            self.ui.questionLbl.setText(self.questions[self.rnd][0])

            for i, x in enumerate(range(4), 1):
                self.answBtn[x].setText(self.questions[self.rnd][i])
                self.answBtn[x].setStyleSheet(self.styles.setStyleDefault)

            self.animate.animateText()
            self.animate.animateButton()

            self.questions.pop(self.rnd)
            self.ransw.pop(self.rnd)

            self.start += 1
        else:
            self.score.show()
            self.score.showScore()
            self.score.timer.timeout.connect(self.score.countThrough)
            self.ui.nextBtn.hide()
            for b in self.answBtn:
                b.setDisabled(True)

    ###===>>> ANTWORTEN GEGENPRÜFEN
    def check1(self):
        if self.lockState[0]:
            if self.righAnswer[0] == self.answers[0]:
                self.ui.answBtn1.setStyleSheet(self.styles.scoreRight)      ###===>>> STYLESHEET ÄNDERN WENN RICHTIG
                self.ui.label_4.setText(str(self.rightNum))
                self.rightNum += 1
                self.lockState[0] = False
            else:
                self.ui.answBtn1.setStyleSheet(self.styles.scoreWrong)
                self.ui.label_5.setText(str(self.wrongNum))
                self.wrongNum += 1
                self.lockState[0] = False

    def check2(self):
        if self.lockState[1]:
            if self.righAnswer[1] == self.answers[1]:
                self.ui.answBtn2.setStyleSheet(self.styles.scoreRight)      ###===>>> STYLESHEET ÄNDERN WENN RICHTIG
                self.ui.label_4.setText(str(self.rightNum))
                self.rightNum += 1
                self.lockState[1] = False
            else:
                self.ui.answBtn2.setStyleSheet(self.styles.scoreWrong)
                self.ui.label_5.setText(str(self.wrongNum))
                self.wrongNum += 1
                self.lockState[1] = False

    def check3(self):
        if self.lockState[2]:
            if self.righAnswer[2] == self.answers[2]:
                self.ui.answBtn3.setStyleSheet(self.styles.scoreRight)      ###===>>> STYLESHEET ÄNDERN WENN RICHTIG
                self.ui.label_4.setText(str(self.rightNum))
                self.rightNum += 1
                self.lockState[2] = False
            else:
                self.ui.answBtn3.setStyleSheet(self.styles.scoreWrong)
                self.ui.label_5.setText(str(self.wrongNum))
                self.wrongNum += 1
                self.lockState[2] = False

    def check4(self):
        if self.lockState[3]:
            if self.righAnswer[3] == self.answers[3]:
                self.ui.answBtn4.setStyleSheet(self.styles.scoreRight)      ###===>>> STYLESHEET ÄNDERN WENN RICHTIG
                self.ui.label_4.setText(str(self.rightNum))
                self.rightNum += 1
                self.lockState[3] = False
            else:
                self.ui.answBtn4.setStyleSheet(self.styles.scoreWrong)
                self.ui.label_5.setText(str(self.wrongNum))
                self.wrongNum += 1
                self.lockState[3] = False


    ###===>>> RESIZE GRIP
    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        rect = self.rect()
        self.grips[1].move(rect.right() - self.gripSize, 0)
        self.grips[2].move(
            rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        self.grips[3].move(0, rect.bottom() - self.gripSize)

    ###===>>> FENSTER BEWEGEN
    def moveWindow(self, event):
        ## BEI LINKSCLICK AUF DIE TOOLBAR
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


    ###===>>> PROGRAMM BEENDEN FUNC() / QDIALOG
    def cloesWindow(self):
        ## MESSAGE BOX ABFRAGE
        msg = QMessageBox.question(self, "Programm Beenden?", "Bist du sicher? Das Programm wird geschlossen",
                                   QMessageBox.No | QMessageBox.Yes)
        ## WENN JA GEDRÜCKT WIRD, WIRD DAS PROGRAMM BEENDET
        if msg == QMessageBox.Yes:
            self.close()
            self.score.close()

###===>>> SCHATTEN HINZUFÜGEN
    def setShadow(self):
        ###===>>>ANTWORT BUTTON 1
        self.b1shadow = QGraphicsDropShadowEffect()
        self.b1shadow.setBlurRadius(10)
        self.b1shadow.setXOffset(0)
        self.b1shadow.setYOffset(0)
        self.b1shadow.setColor(QColor("#1e2124"))
        self.ui.answBtn1.setGraphicsEffect(self.b1shadow)

        ###===>>>ANTWORT BUTTON 1
        self.b2shadow = QGraphicsDropShadowEffect()
        self.b2shadow.setBlurRadius(10)
        self.b2shadow.setXOffset(0)
        self.b2shadow.setYOffset(0)
        self.b2shadow.setColor(QColor("#1e2124"))
        self.ui.answBtn2.setGraphicsEffect(self.b2shadow)

        ###===>>>ANTWORT BUTTON 1
        self.b3shadow = QGraphicsDropShadowEffect()
        self.b3shadow.setBlurRadius(10)
        self.b3shadow.setXOffset(0)
        self.b3shadow.setYOffset(0)
        self.b3shadow.setColor(QColor("#1e2124"))
        self.ui.answBtn3.setGraphicsEffect(self.b3shadow)

        self.b4shadow = QGraphicsDropShadowEffect()
        self.b4shadow.setBlurRadius(10)
        self.b4shadow.setXOffset(0)
        self.b4shadow.setYOffset(0)
        self.b4shadow.setColor(QColor("#1e2124"))
        self.ui.answBtn4.setGraphicsEffect(self.b4shadow)
