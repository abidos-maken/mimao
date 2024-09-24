from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QWidget, QLabel, QFrame, QGraphicsDropShadowEffect, QPushButton
from PyQt6.QtCore import Qt

class TimerUi(object):
    def setup(self, form:QWidget):
        form.setObjectName("Timer UI")
        form.setStyleSheet("""
                           QLabel[group="timer_text"] {
                               background-color: white;
                               border-radius: 15px;
                               font: 95px BIG JOHN;
                           }
                           QLabel[group="collon_text"] {
                               font: 80px BIG JOHN;
                               color: white;
                           }
                           QLabel[group="decoration_text"] {
                               font: 35px BIG JOHN;
                               color: white;
                           }
                           """)

        self.image_form = QFrame(form)
        self.image_form.resize(720,480)
        self.image_form.setStyleSheet("""
                            QFrame {
                                background-image: url(images/background.jpg);
                                background-repeat: no-repeat;
                                background-position: center;
                                background-size: cover;
                            }
                           """)

        self.remain_minutes_ten = QLabel("0", form)
        self.remain_minutes_ten.setProperty("group", "timer_text")
        self.remain_minutes_ten.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.remain_minutes_ten.setGraphicsEffect(self.__create_shadow(form))
        self.remain_minutes_one = QLabel("0", form)
        self.remain_minutes_one.setProperty("group", "timer_text")
        self.remain_minutes_one.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.remain_minutes_one.setGraphicsEffect(self.__create_shadow(form))
        self.remain_seconds_ten = QLabel("0", form)
        self.remain_seconds_ten.setProperty("group", "timer_text")
        self.remain_seconds_ten.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.remain_seconds_ten.setGraphicsEffect(self.__create_shadow(form))
        self.remain_seconds_one = QLabel("0", form)
        self.remain_seconds_one.setProperty("group", "timer_text")
        self.remain_seconds_one.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.remain_seconds_one.setGraphicsEffect(self.__create_shadow(form))

        self.remain_minutes_ten.setGeometry(100,130,110,130)
        self.remain_minutes_one.setGeometry(225,130,110,130)
        self.remain_seconds_ten.setGeometry(385,130,110,130)
        self.remain_seconds_one.setGeometry(510,130,110,130)

        # NOTE :: Decoration texts
        self.collon_text = QLabel(":", form)
        self.collon_text.setProperty("group", "collon_text")
        self.collon_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.collon_text.setGraphicsEffect(self.__create_shadow(form,1,1))
        self.min_text = QLabel("min", form)
        self.min_text.setProperty("group", "decoration_text")
        self.min_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.min_text.setGraphicsEffect(self.__create_shadow(form,1,1))
        self.sec_text = QLabel("sec", form)
        self.sec_text.setProperty("group", "decoration_text")
        self.sec_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sec_text.setGraphicsEffect(self.__create_shadow(form,1,1))

        self.collon_text.setGeometry(350,120,20,110)
        self.min_text.setGeometry(155, 70, 120, 50)
        self.sec_text.setGeometry(445, 70, 120, 50)

        # NOTE :: start button
        self.active_btn = QPushButton("start", form)
        self.active_btn.setGraphicsEffect(self.__create_shadow(form))

        self.active_btn.setGeometry(260, 350, 200, 40)

    def __create_shadow(self, form, offset_x = 3, offset_y = 3):
        shadow = QGraphicsDropShadowEffect(form)
        shadow.setBlurRadius(10)
        shadow.setOffset(offset_x,offset_y)
        shadow.setColor(QColor(0,0,0,160))
        return shadow