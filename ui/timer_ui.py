from PyQt6.QtWidgets import QWidget, QLabel

class TimerUi(object):
    def setup(self, form:QWidget):
        form.setObjectName("Timer UI")

        self.remain_minutes = QLabel("15", form)
        self.remain_seconds = QLabel("00", form)

        self.remain_minutes.setGeometry(10,10,20,10)
        self.remain_seconds.setGeometry(35,10,10,10)