from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from inst import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
 

        self.set_appear()
        self.initUI()
    
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_weight, win_hegiht )
        self.move(win_x, win_y)


        

    def initUI(self):
        self.res = self.result()
        self.index_txt = QLabel(txt_index + str(self.index))
        self.result_txt = QLabel(txt_workheart + str(self.res))

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.index_txt, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.result_txt, alignment=Qt.AlignCenter)

        self.setLayout(self.main_layout)
    



    def result(self):
        nivel = ""
        self.index = (4 * (self.exp.test1 + self.exp.test2 + self.exp.test3 ) - 200) / 10
        if self.exp.edad >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index >= 11 and self.index <= 14.9:
                return txt_res2
            elif self.index >= 6 and self.index <= 10.9:
                return txt_res3
            elif self.index >= 0.5 and self.index <= 5.9:
                return txt_res4
            elif self.index <= 0.4:
                return txt_res5
        elif self.exp.edad == 13 or self.exp.edad == 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index >= 12.5 and self.index <= 16.4:
                return txt_res2
            elif self.index >= 7.5 and self.index <= 12.4:
                return txt_res3
            elif self.index >= 2 and self.index <= 7.4:
                return txt_res4
            elif self.index <= 1.9:
                return txt_res5
        elif self.exp.edad == 12:
            if self.index >= 18:
                return txt_res1
            elif self.index >= 14 and self.index <= 17.9:
                return txt_res2
            elif self.index >= 9 and self.index <= 13.9:
                return txt_res3
            elif self.index >= 3.5 and self.index <= 8.9:
                return txt_res4
            elif self.index <= 3.4:
                return txt_res5
        elif self.exp.edad == 9 or self.exp.edad == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index >= 15.5 and self.index <= 19.4:
                return txt_res2
            elif self.index >= 10.5 and self.index <= 15.4:
                return txt_res3
            elif self.index >= 5 and self.index <= 10.4:
                return txt_res4
            elif self.index <= 4.9:
                return txt_res5
        elif self.exp.edad == 7 or self.exp.edad == 8:
            if self.index >= 21:
                return txt_res1
            elif self.index >= 17 and self.index <= 20.9:
                return txt_res2
            elif self.index >= 12 and self.index <= 16.9:
                return txt_res3
            elif self.index >= 6.5 and self.index <= 11.9:
                return txt_res4
            elif self.index <= 6.4:
                return txt_res5
        else:
            return "error"
  