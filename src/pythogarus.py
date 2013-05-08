from math import *
from PySide.QtGui import *
from PySide.QtCore import *



class Pythogarus(object):
   
   def __init__(self, A = 0, B = 0, C = 0):
       
       C = sqrt(pow(A, 2) + pow(B, 2))
       B = sqrt(pow(C, 2) - pow(A, 2))
       A = sqrt(pow(C, 2) - pow(B, 2))

   def gui(self):
       widg = QWidget(self)
       validator = QIntValidator(-9999, 999999999, self)
       layout = QGridLayout(widg)
       self.la = QLabel("Side A")
       self.lb = QLabel("Side B")
       self.lc = QLabel("Side C")
       self.A = QLineEdit()
       self.A.setValidator(validator)
       self.B = QLineEdit()
       self.B.setValidator(validator)
       self.C = QLineEdit()
       self.C.setValidator(validator)
       self.answer = QPushButton("&Return")
       self.answer.setShortcut("Return")
       self.answer.clicked.connect(self.result)
       
       
       layout.addWidget(self.A, 0, 1)
       layout.addWidget(self.B, 1, 1)
       layout.addWidget(self.C, 2, 1)
       layout.addWidget(self.la, 0 , 0) 
       layout.addWidget(self.lb, 1, 0)
       layout.addWidget(self.lc, 2, 0)

       
       
       layout.addWidget(self.answer, 3, 1)
       self.setWindowTitle("Pythogarus")
       self.setCentralWidget(widg)
       
       pass   

   def result(self):
       temp = ""
       if self.A.text() != "":
          if self.B.text() != "":
             if self.C.text() == "":
                temp = sqrt(pow(float(self.A.text()), 2) + (pow(float(self.B.text()), 2)))
                self.C.setText(str(temp))
       elif self.A.text() == "":
          if self.B.text() != "":
             if self.C.text() != "":
                temp = sqrt(pow(float(self.C.text()), 2) - (pow(float(self.B.text()), 2)))
                self.A.setText(str(temp))
       if self.B.text() == "":
          temp = sqrt(pow(float(self.C.text()), 2) - (pow(float(self.A.text()), 2)))
          self.B.setText(str(temp))
      



