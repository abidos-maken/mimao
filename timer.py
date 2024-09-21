import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt6.QtCore import QTimer, Qt

from ui.timer_ui import TimerUi

class Timer(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300,300)

        self.ui = TimerUi()
        self.ui.setup(self)

        self.remaining_time = 900 

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.__timecount_cb)
        self.timer.start()

    def __timeout_event(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Timeout")
        msg.setText("Time is over!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        msg.exec()

    def __timecount_cb(self):
        if self.remaining_time == 0:
            self.timer.stop()
            self.__timeout_event()
        else:
            self.remaining_time -= 1
            minutes = str(int(self.remaining_time / 60))
            seconds = str(self.remaining_time % 60)
            self.ui.remain_minutes.setText(minutes)
            self.ui.remain_seconds.setText(seconds)

if __name__ == '__main__':
    app = QApplication(sys.argv) 
    timer = Timer()
    timer.show()
    app.exec()
    del timer
    sys.exit()
