from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QWidget, QLabel, QFrame, QGraphicsDropShadowEffect
from PyQt6.QtCore import Qt

class TimerUi(object):
    def setup(self, form:QWidget):
        form.setObjectName("Timer UI")
        form.setStyleSheet("""
                           QLabel#remain_minutes_ten {
                               background-color: white;
                               border-radius: 15px;
                               font: 95px BIG JOHN;
                           }
                           QLabel#remain_minutes_one {
                               background-color: white;
                               border-radius: 15px;
                               font: 95px BIG JOHN;
                           }
                           QLabel#remain_seconds_ten {
                               background-color: white;
                               border-radius: 15px;
                               font: 95px BIG JOHN;
                           }
                           QLabel#remain_seconds_one {
                               background-color: white;
                               border-radius: 15px;
                               font: 95px BIG JOHN;
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
        self.remain_minutes_ten.setObjectName("remain_minutes_ten")
        self.remain_minutes_ten.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.remain_minutes_ten.setGraphicsEffect(self.__create_shadow(form))
        self.remain_minutes_one = QLabel("0", form)
        self.remain_minutes_one.setObjectName("remain_minutes_one")
        self.remain_minutes_one.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.remain_minutes_one.setGraphicsEffect(self.__create_shadow(form))
        self.remain_seconds_ten = QLabel("0", form)
        self.remain_seconds_ten.setObjectName("remain_seconds_ten")
        self.remain_seconds_ten.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.remain_seconds_ten.setGraphicsEffect(self.__create_shadow(form))
        self.remain_seconds_one = QLabel("0", form)
        self.remain_seconds_one.setObjectName("remain_seconds_one")
        self.remain_seconds_one.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.remain_seconds_one.setGraphicsEffect(self.__create_shadow(form))

        self.remain_minutes_ten.setGeometry(100,130,110,130)
        self.remain_minutes_one.setGeometry(225,130,110,130)
        self.remain_seconds_ten.setGeometry(385,130,110,130)
        self.remain_seconds_one.setGeometry(510,130,110,130)

    def __create_shadow(self, form):
        shadow = QGraphicsDropShadowEffect(form)
        shadow.setBlurRadius(10)
        shadow.setOffset(3,3)
        shadow.setColor(QColor(0,0,0,160))
        return shadow