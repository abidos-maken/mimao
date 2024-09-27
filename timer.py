import sys
from collections import deque
from PyQt6.QtGui import QKeyEvent
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

        self.__timer_running_status = False
        self.ui.active_btn.clicked.connect(self.__timer_status_set)

        self.origin_time = 0
        self.remaining_time = 0
        self.__timer_text_set(self.origin_time)

        self.__timer_labels_list = [self.ui.remain_minutes_ten, self.ui.remain_minutes_one, self.ui.remain_seconds_ten, self.ui.remain_seconds_one]
        self.__key_input_set_time_arr = deque([])
        self.__key_input_count = 0

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.__timecount_cb)

    def __timer_status_set(self):
        if self.__timer_running_status:
            self.timer.stop()
            self.__timer_running_status = False
            self.ui.active_btn.setText("start")
            self.remaining_time = 0
            self.__timer_text_set(self.origin_time)
        else:
            if int(self.ui.remain_seconds_ten.text()) > 5 :
                self.ui.remain_seconds_ten.setText("5")
                if self.__key_input_count == 2:
                    index = 0
                elif self.__key_input_count == 3:
                    index = 1
                else:
                    index = 2
                self.__key_input_set_time_arr[index] = 5

            self.remaining_time = 0
            self.remaining_time += int(self.__timer_labels_list[0].text()) * 600
            self.remaining_time += int(self.__timer_labels_list[1].text()) * 60
            self.remaining_time += int(self.__timer_labels_list[2].text()) * 10
            self.remaining_time += int(self.__timer_labels_list[3].text())
            self.origin_time = self.remaining_time

            self.__timer_running_status = True
            self.ui.active_btn.setText("stop")
            self.timer.start()

    def __timer_text_set(self, time):
        minutes = str(int(time / 60))
        if len(minutes) < 2:
            minutes = "0" + minutes
        seconds = str(time % 60)
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
        self.__timer_status_set()

    def __timecount_cb(self):
        if self.remaining_time == 0:
            self.__timeout_event()
        else:
            self.remaining_time -= 1
            self.__timer_text_set(self.remaining_time)

    def __key_timer_setting(self):
        for i in range(4):
            if i < self.__key_input_count :
                self.__timer_labels_list[3-i].setText(str(self.__key_input_set_time_arr[i]))
            else:
                self.__timer_labels_list[3-i].setText(str(0))

    def keyPressEvent(self, e: QKeyEvent | None):
        if not self.__timer_running_status:
            if e.key() >= Qt.Key.Key_0 and e.key() <= Qt.Key.Key_9:
                if self.__key_input_count < 4:
                    self.__key_input_set_time_arr.appendleft(e.key() - Qt.Key.Key_0)
                    self.__key_input_count += 1
            elif e.key() == Qt.Key.Key_Backspace:
                if self.__key_input_count > 0:
                    self.__key_input_count -= 1
                    self.__key_input_set_time_arr.popleft()
            else:
                return
            self.__key_timer_setting()

if __name__ == '__main__':
    app = QApplication(sys.argv) 
    timer = Timer()
    timer.show()
    app.exec()
    del timer
    sys.exit()
