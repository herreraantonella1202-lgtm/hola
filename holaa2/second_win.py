from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtWidgets import  QHBoxLayout, QLineEdit, QWidget, QLabel, QVBoxLayout, QPushButton
from inst import *
from PyQt5.QtGui import QFont
from final_win import FinalWin

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_weight, win_hegiht )
        self.move(win_x, win_y)


        

    def initUI(self):
        #Izquierda
        self.name =QLabel(txt_name)
        self.name_input = QLineEdit(txt_hintname)
        self.age =QLabel(txt_age)
        self.age_input = QLineEdit(txt_hintage)
        self.test1 =QLabel(txt_test1)
        self.starttest1 =QPushButton(txt_starttest1)
        self.hinttest1 = QLineEdit(txt_hinttest1)
        self.test2 =QLabel(txt_test2)
        self.starttest2 =QPushButton(txt_starttest2)
        self.test3 =QLabel(txt_test3)
        self.starttest3 =QPushButton(txt_starttest3)
        self.hinttest2 = QLineEdit(txt_hinttest2)
        self.hinttest3 = QLineEdit(txt_hinttest3)
        self.finalwin =QPushButton(txt_finalwin)

        #Derecha
        self.txt_timer =QLabel("00:00:00")
        self.txt_timer.setFont(QFont("Times", 40, QFont.Bold))
        self



        

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.name, alignment= Qt.AlignLeft)
        self.layout.addWidget(self.name_input, alignment= Qt.AlignLeft)
        self.layout.addWidget(self.age, alignment= Qt.AlignLeft)
        self.layout.addWidget(self.age_input, alignment= Qt.AlignLeft)
        self.layout.addWidget(self.test1, alignment= Qt.AlignLeft)
        self.layout.addWidget(self.starttest1, alignment= Qt.AlignLeft)
        self.layout.addWidget(self.hinttest1, alignment= Qt.AlignLeft)
        self.layout.addWidget(self.test2, alignment= Qt.AlignLeft)
        self.layout.addWidget(self.starttest2, alignment= Qt.AlignLeft)
        self.layout.addWidget(self.test3, alignment= Qt.AlignLeft)
        self.layout.addWidget(self.starttest3, alignment= Qt.AlignLeft)
        self.layout.addWidget(self.hinttest2, alignment= Qt.AlignLeft)
        self.layout.addWidget(self.hinttest3, alignment= Qt.AlignLeft)
        self.layout.addWidget(self.finalwin, alignment= Qt.AlignCenter)


        self.layout2 =QVBoxLayout()
        self.layout2.addWidget(self.txt_timer)

        #Lyout principal
        self.main_layout = QHBoxLayout()
        self.main_layout.addLayout(self.layout)
        self.main_layout.addLayout(self.layout2)



        self.setLayout(self.main_layout)


    def connects(self):
        self.starttest1.clicked.connect(self.time_test1)
        self.starttest2.clicked.connect(self.time_test2)
        self.starttest3.clicked.connect(self.time_test3)
        self.finalwin.clicked.connect(self.next_click)
    


    def time_test1(self):
        global time
        time = QTime(0,0,15)
        self.txt_timer.setText(time.toString("hh:mm:ss"))
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)


    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString("hh:mm:ss"))
        self.txt_timer.setStyleSheet("color: rgb(0,0.0)")
        #estilo
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    

    def time_test2(self):
        global time
        time = QTime(0,0,30)
        self.txt_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)


    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.txt_timer.setStyleSheet("color: rgb(0,0.0)")
        #estilo
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()




    def time_test3(self):
        global time
        time = QTime(0,1,0)
        self.txt_timer.setText(time.toString("hh:mm:ss"))
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)


    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) <= 59 and int(time.toString("hh:mm:ss")[6:8]) >=45:
            self.txt_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.txt_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.txt_timer.setStyleSheet("color: rgb(0,0,0)")
        #estilo
        if time.toString("hh:mm:ss") == "00:00:00":
            self.txt_timer.setStyleSheet("color: rgb(0,0,0)")
            self.timer.stop()


    def next_click(self):
        self.hide()
        self.exp = Experiment(
            self.age_input.text(),
            self.hinttest1.text(),
            self.hinttest2.text(),
            self.hinttest3.text(),
        )
        self.tw = FinalWin(self.exp)


class Experiment():
    def __init__(self, edad, test1, test2, test3):
        self.edad = int(edad)
        self.test1 = int(test1)
        self.test2 = int(test2)
        self.test3 = int(test3)





def next_click(self):
    print(self.name_input.text())
    



