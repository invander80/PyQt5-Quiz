from ui.ui_progress import *
from startit import StartApp
from data.functions import Functions


class ProgressBar(QWidget):
    def __init__(self, parent=None):
        super(ProgressBar, self).__init__()

        self.parent = parent

###===>>>IMPORTS
        self.progress = Ui_Form()
        self.progress.setupUi(self)
        self.func = Functions(self)

        self.start = StartApp(self)

###===>>>FUNCS
        self.func.removeTitle()

        self.progressTimer = QTimer()
        self.progressTimer.timeout.connect(self.runProgress)
        self.progressTimer.start(20)

###===> VALUES
        self.COUNTER = 0

###===>>> PROGRESSBAR DURLAUF
    def runProgress(self):
        if self.COUNTER <= 100:
            self.progressRun(self.COUNTER)
            self.progress.percentLbl.setText(f"{self.COUNTER}%")
            self.COUNTER +=1
            if self.COUNTER == 100:
                self.close()
                self.start.show()

    def progressRun(self, value):
        style = """
        QFrame {
                border-radius:220px;
background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(72, 0, 255, 0), stop:{STOP_2} rgba(255, 0, 129, 255));
                }
                """
        progress = (100- value) / 100
        val1 = str(progress -0.001)
        val2 = str(progress)

        newStyle = style.replace("{STOP_1}", val1).replace("{STOP_2}", val2)
        self.progress.proggressFrm.setStyleSheet(newStyle)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    prog = ProgressBar()
    prog.show()
    app.exec()