from PySide.QtGui import *
from PySide.QtCore import QObject,Qt

#####################################################################################################################################################
class Area(object):
    def area(self):
        self.sqMilesTo ={"sq. miles":1,"acres": 640,"sq.yards": 3097600,"sq. feet": 27878400,"sq.Km": 2.589988,"hectares": 258.9988,
                       "ares": 25899.88,"sq. m": 25899.88,"sq. dm": 258998800,"sq. cm": 258998800,"sq. mm": 2589988000000,"talangwah": 647497,
                       "ngarn": 6474.97,"rai": 1618.743}

        self.acresTo ={"sq. miles":0.0015625,"acres": 1,"sq.yards": 4840,"sq. feet": 43560,"sq.Km": 0.00404686,"hectares": 0.404686,"ares": 40.46856,
                     "sq. m": 4046.856,"sq. dm": 404685.6,"sq. mm": 4046856000,"talangwah": 1011.714,"ngarn": 10.11714,"rai": 2.529285, "sq. cm": 0}

        self.sqYardsTo ={"sq. miles":3.22831e-7,"acres": 0.000206612,"sq.yards": 1,"sq. feet": 9,"sq.Km": 8.36127e-7,"hectares": 0.0000836127,"ares": 0.00836127,
                        "sq. m": 0.836127,"sq. dm": 83.61274,"sq. cm": 8361.274,"sq. mm": 836127.4,"talangwah": 0.209032,"ngarn": 0.00209032,"rai": 0.00052258}

        self.sqFeetTo ={"sq. miles":3.58701e-8,"acres": 0.0000229568,"sq.yards": 0.111111,"sq. feet": 1,"sq.Km": 9.2903e-8,"hectares": 0.0000092903,"ares": 0.00092903,
                      "sq. m": 0.092903,"sq. dm": 9.290304,"sq. cm": 929.0304,"sq. mm": 92903.04,"talangwah": 0.0232258,"ngarn": 0.000232258,"rai": 0.0000580644}

        self.sqKmTo ={"sq. miles":0.386102,"acres": 247.1054,"sq.yards": 1195990,"sq. feet": 10763910,"sq.Km": 1,"hectares": 100,"ares": 10000,"sq. m": 1000000,"sq. dm": 100000000,
                    "sq. cm": 10000000000,"sq. mm": 999999999999.9999,"talangwah": 250000,"ngarn": 2500,"rai": 625}

        self.hectaresTo ={"sq. miles":0.00386102,"acres": 0.00386102,"sq.yards": 11959.9,"sq. feet": 107639.1,"sq.Km": 0.01,"hectares": 1,"ares": 100,"sq. m": 10000,
                        "sq. dm": 1000000,"sq. cm": 100000000,"sq. mm": 10000000000,"talangwah": 2500,"ngarn": 25,"rai": 6.25}

        self.aresTo ={"sq. miles":0.0000386102,"acres": 0.0247105,"sq.yards": 119.599,"sq. feet": 1076.391,"sq.Km": 0.0001,"hectares": 0.01,"ares": 1,"sq. m": 100,"sq. dm": 10000,
                    "sq. cm": 1000000,"sq. mm": 100000000,"talangwah": 25,"ngarn": .25,"rai": 0.0625}

        self.sqMTo ={"sq. miles":3.86102e-7,"acres": 0.000247105,"sq.yards": 1.19599,"sq. feet": 10.76391,"sq.Km": 0.000001,"hectares": 0.0001,"ares": 0.01,"sq. m": 1,"sq. dm": 100,
                    "sq. cm": 10000,"sq. mm": 1000000,"talangwah": .25,"ngarn": .0025,"rai": 0.000625}

        self.sqDmTo ={"sq. miles":3.86102e-9,"acres": 0.00000247105,"sq.yards": 1.19599,"sq. feet": 0.107639,"sq.Km": 1e-8,"hectares": 0.000001,"ares": 0.0001,"sq. m": 0.01,"sq. dm": 1,
                    "sq. cm": 10,"sq. mm": 10000,"talangwah": 0.0025,"ngarn": 0.000025,"rai": 0.00000625}

        self.sqCmTo ={"sq. miles":3.86102e-11,"acres": 2.47105e-8,"sq.yards": 0.000119599,"sq. feet": 0.00107639,"sq.Km": 1e-10,"hectares": 1e-8,"ares": 0.0001,"sq. m": 0.01,
                    "sq. dm": 0.01,"sq. cm": 1,"sq. mm": 100,"talangwah": 0.000025,"ngarn": 2.5e-7,"rai": 6.25e-8}

        self.sqMmTo ={"sq. miles":3.86102e-13,"acres": 2.47105e-10,"sq.yards": 0.00000119599,"sq. feet": 0.0000107639,"sq.Km": 1e-12,"hectares": 1e-10,"ares": 1e-8,"sq. m": 0.000001,
                    "sq. dm": 0.0001,"sq. cm": 0.01,"sq. mm": 1,"talangwah": 2.5e-7,"ngarn": 2.5e-9,"rai": 6.25e-10}

        self.talangwahTo ={"sq. miles":0.00000154441,"acres": 0.000988422,"sq.yards": 4.78396,"sq. feet": 43.05564,"sq.Km": 0.000004,"hectares": 0.0004,"ares": 0.04,"sq. m": 4,
                       "sq. dm": 400,"sq. cm": 40000,"sq. mm": 40000001,"talangwah": 1,"ngarn": 0.01,"rai": 0.0025}

        self.ngarnTo ={"sq. miles":0.000154441,"acres": 0.0988422,"sq.yards": 478.396,"sq. feet": 4305.564,"sq.Km": 0.0004,"hectares": 0.04,"ares": 4,"sq. m": 400,
                     "sq. dm": 4000,"sq. cm": 40000,"sq. mm": 4000000,"talangwah": 100,"ngarn": 1,"rai": 0.25}

######Construct Interface Look#######################
        self.areaWidget = QWidget(self)
        self.box1 = QComboBox()
        self.box2 = QComboBox()
        self.entry = QLineEdit()
        self.edit = QLineEdit()
        self.edit.setReadOnly(True)
        self.setWindowTitle("ConvertMe - Area")

        self.edit.setMinimumHeight(40)
        self.edit.setFont(QFont('', 15))
        self.edit.setAlignment(Qt.AlignmentFlag.AlignRight)

        label1 = QLabel("From:")
        label2 = QLabel("To:")
        self.Button = QPushButton("Convert")
        self.label3 = QLabel()


        layout =QVBoxLayout(self.areaWidget)
        layout.addWidget(self.edit)
        layout.addWidget(label1)
        layout.addWidget(self.box1)
        layout.addWidget(label2)
        layout.addWidget(self.box2)
        layout.addWidget(self.entry)
        layout.addWidget(self.Button)
        layout.addWidget(self.label3)

        self.box1.addItem("")
        self.box1.addItem("sq. miles")
        self.box1.addItem("acres")
        self.box1.addItem("sq.yards")
        self.box1.addItem("sq. feet")
        self.box1.addItem("sq.Km")
        self.box1.addItem("hectares")
        self.box1.addItem("ares")
        self.box1.addItem("sq. m")
        self.box1.addItem("sq. dm")
        self.box1.addItem("sq. cm")
        self.box1.addItem("sq. mm")
        self.box1.addItem("talangwah")
        self.box1.addItem("ngarn")
        #self.box1.addItem("rai")
        self.box2.addItems(sorted(self.sqMilesTo.keys()))

#####################################################

        self.entry.setValidator(QDoubleValidator(
            -999.0, 999.0, 2, self.entry))
        self.label3.setStyleSheet('''
        QLabel {color:red;}''')
        self.entry.setMaxLength(15)

        self.setLayout(layout)
        self.setCentralWidget(self.areaWidget)
        self.box1.activated[int].connect(self.areaChange)
        self.Button.setShortcut("Return")
####################################################

    def areaChange(self, index):
        """connects selected index to matching function"""
        if index == 1:
            self.Button.clicked.connect(self.sqMiles)
        elif index == 2:
            self.Button.clicked.connect(self.acres)
        elif index == 3:
            self.Button.clicked.connect(self.sqYards)
        elif index == 4:
            self.Button.clicked.connect(self.sqFeet)
        elif index == 5:
            self.Button.clicked.connect(self.sqKm)
        elif index == 6:
            self.Button.clicked.connect(self.hectares)
        elif index == 7:
            self.Button.clicked.connect(self.ares)
        elif index == 8:
            self.Button.clicked.connect(self.sqM)
        elif index == 9:
            self.Button.clicked.connect(self.sqDm)
        elif index == 10:
            self.Button.clicked.connect(self.sqCm)
        elif index == 11:
            self.Button.clicked.connect(self.sqMm)
        elif index == 12:
            self.Button.clicked.connect(self.talangwah)
        elif index == 13:
            self.Button.clicked.connect(self.ngarn)
        #elif index == 14:
        #    self.Button.clicked.connect(self.rai)


    def sqMiles(self):
        answer =  self.sqMilesTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))

    def acres(self):
        answer =  self.acresTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass

    def sqYards(self):
        answer =  self.sqYardsTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass

    def sqFeet(self):
        answer =  self.sqFeetTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def sqKm(self):
        answer =  self.sqKmTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def hectares(self):
        answer =  self.hectaresTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def ares(self):
        answer =  self.aresTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass

    def sqM(self):
        answer =  self.sqMTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass

    def sqDm(self):
        answer =  self.sqDmTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def sqCm(self):
        answer =  self.sqCmTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def sqMm(self):
        answer =  self.sqMmTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def talangwah(self):
        answer =  self.talangwahTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def ngarn(self):
        answer =  self.ngarnTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def rai(self):
        answer =  self.raiTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
