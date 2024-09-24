import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt6.QtCore import QTimer, Qt

from ui.timer_ui import TimerUi

SET_TIMER = 300

class Timer(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(720,480)

        self.ui = TimerUi()
        self.ui.setup(self)

        self.remaining_time = 300
        self.__timer_text_set()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.__timecount_cb)
        self.timer.start()

    def __timer_text_set(self):
        minutes = str(int(self.remaining_time / 60))
        if len(minutes) < 2:
            minutes = "0" + minutes
        seconds = str(self.remaining_time % 60)
        if len(seconds) < 2:
            seconds = "0" + seconds
        self.ui.remain_minutes_ten.setText(minutes[0])
        self.ui.remain_minutes_one.setText(minutes[1])
        self.ui.remain_seconds_ten.setText(seconds[0])
        self.ui.remain_seconds_one.setText(seconds[1])

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
            self.__timer_text_set()

if __name__ == '__main__':
    app = QApplication(sys.argv) 
    timer = Timer()
    timer.show()
    app.exec()
    del timer
    sys.exit()
