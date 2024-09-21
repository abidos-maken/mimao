from PyQt6.QtWidgets import QWidget, QLabel, QFrame

class TimerUi(object):
    def setup(self, form:QWidget):
        form.setObjectName("Timer UI")

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
        self.remain_minutes = QLabel("15", form)
        self.remain_seconds = QLabel("00", form)

        self.remain_minutes.setGeometry(10,10,20,10)
        self.remain_seconds.setGeometry(35,10,10,10)