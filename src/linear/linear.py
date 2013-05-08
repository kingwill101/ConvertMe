from PySide.QtGui import *
from PySide.QtCore import QObject,Qt


#####################################################################################################################################################
class Linear(object):
    def linnear(self):
        #set calculation tables for Linear Measurement
        self.milesTo = {"mile":1,"Nautical mile":0.868423,"Nautical League":0.289474,"Furlong":8,"Chain":80,"rod":320,"yard":1760,"Feet":5280,"inch":63360,
                        "Km":1.609344,"Hm":16.09344,"Meter":1609.344,"Dm":16093.44,"Cm":160934.4,"Mm":1609344,"Light Second":0.00000536819
                   }
             
        self.NauticalLeagueTo = {"Nautical League":1,"mile":3.454538,"Nautical mile":3,"Furlong":27.6363,"Chain":276.363,"rod":1105.452,"yard":6079.987,"Feet":18239.96,
                                 "inch":218879.5,"Km":5.55954,"Hm":55.5954,"Meter":5559.54,"Dm":55595.4,"Cm":555954,"Mm":5559540,"Light Second":0.0000185446
                   }
             
        self.NauticalmileTo = {"Nautical mile":1,"mile":1.151513,"Nautical League":0.333333,"Furlong":9.212101,"Chain":92.12101,"rod":368.4841,"yard":2026.662,"Feet":6079.987,
                               "inch":72959.84,"Km":1.85318,"Hm":18.5318,"Meter":1853.18,"Dm":18531.8,"Cm":185318,"Mm":1853180,"Light Second":0.00000618154
                   }
             
        self.FurlongTo = {"Furlong":1,"Nautical mile":0.108553,"Nautical League":0.0361843,"mile":0.125,"Chain":10,"rod":40,"yard":220,
                          "Feet":660,"inch":7920,"Km":0.201168,"Hm":2.01168,"Meter":201.168,"Dm":2011.68,"Cm":20116.8,"Mm":201168,"Light Second":6.71024e-7
                   }
        
        self.chainTo= {"mile":0.0125,"Nautical mile":0.0108553,"Nautical League":0.00361843,"Furlong":0.1,"Chain":1,"rod":4,"yard":22,"Feet":66,
                       "inch":792,"Km":0.0201168,"Hm":0.201168,"Meter":20.1168,"Dm":201.168,"Cm":2011.68,"Mm":20116.8,"Light Second":6.71024e-8
                   }
        
        
        self.rodTo = {"mile":0.003125,"Nautical mile":0.00271382,"Nautical League":0.000904607,"Furlong":0.025,"Chain":0.25,"rod":1,"yard":5.5,
                      "Feet":16.5,"inch":198,"Km":0.0050292,"Hm":0.050292,"Meter":5.0292,"Dm":50.292,"Cm":502.92,"Mm":5029.2,"Light Second":1.67756e-8
                   }
        self.yardTo = {"mile":0.000568182,"Nautical mile":0.000493422,"Nautical League":0.000164474,"Furlong":0.00454545,"Chain":0.0454545,
                       "rod":0.181818,"yard":3,"Feet":5280,"inch":36,"Km":0.0009144,"Hm":0.009144,"Meter":0.9144,"Dm":9.144,"Cm":91.44,"Mm":914.4,
                       "Light Second":3.05011e-9
                   }        
        self.feetTo = {"mile":0.000189394,"Nautical mile":0.000164474,"Nautical League":0.0000548247,"Furlong":0.00151515,"Chain":0.0151515,"rod":0.0606061,
                       "yard":0.333333,"Feet":1,"inch":12,"Km":0.0003048,"Hm":0.003048,"Meter":0.3048,"Dm":3.048,"Cm":30.48,"Mm":304.8,"Light Second":1.0167e-9
                   }
        self.inchTo = {"mile":0.0000157828,"Nautical mile":0.0000137062,"Nautical League":0.00000456872,"Furlong":0.000126263,"Chain":0.00126263,"rod":0.00505051,
                       "yard":0.0277778,"Feet":0.0833333,"inch":1,"Km":0.0000254,"Hm":0.000254,"Meter":0.0254,"Dm":0.254,"Cm":2.54,"Mm":25.4,"Light Second":8.47253e-11
                   }
        
        self.kmTo = {"mile":0.621371,"Nautical mile":0.539613,"Nautical League":0.179871,"Furlong":4.97097,"Chain":49.7097,"rod":1093.613,"yard":0.0277778,
                     "Feet":3280.84,"inch":39370.08,"Km":1,"Hm":10,"Meter":1000,"Dm":10000,"Cm":100000,"Mm":1000000,"Light Second":0.00000333564
                   }
        
        self.hmTo = {"mile":0.0621371,"Nautical mile":0.0539613,"Nautical League":0.0179871,"Furlong":0.497097,"Chain":4.97097,"rod":19.88388,"yard":109.3613,
                     "Feet":328.084,"inch":3937.008,"Km":0.1,"Hm":1,"Meter":100,"Dm":1000,"Cm":10000,"Mm":100000,"Light Second":3.33564e-7
                   }
        self.meterTo = {"mile":0.000621371,"Nautical mile":0.000539613,"Nautical League":0.000179871,"Furlong":0.00497097,"Chain":0.0497097,"rod":0.198839,
                        "yard":1.093613,"Feet":3.28084,"inch":39.37008,"Km":0.001,"Hm":0.01,"Meter":1,"Dm":10,"Cm":100,"Mm":1000,"Light Second":3.33564e-9
                   }
        self.dmTo = {"mile":0.0000621371,"Nautical mile":0.0000539613,"Nautical League":0.0000179871,"Furlong":0.000497097,"Chain":0.00497097,"rod":0.0198839,
                     "yard":0.109361,"Feet":0.328084,"inch":3.937008,"Km":0.0001,"Hm":0.001,"Meter":0.1,"Dm":1,"Cm":10,"Mm":100,"Light Second":3.33564e-10
                   }
        self.cmTo = {"mile":0.00000621371,"Nautical mile":0.00000539613,"Nautical League":0.00000179871,"Furlong":0.0000497097,"Chain":0.000497097,"rod":0.00198839,
                     "yard":0.0109361,"Feet":0.0328084,"inch":0.393701,"Km":0.00001,"Hm":0.0001,"Meter":0.1,"Dm":0.1,"Cm":1,"Mm":10,"Light Second":3.33564e-11
                   }
        self.mmTo = {"mile":6.21371e-7,"Nautical mile":5.39613e-7,"Nautical League":1.79871e-7,"Furlong":0.00000497097,"Chain":0.0000497097,"rod":0.000198839,
                     "yard":0.00109361,"Feet":0.00328084,"inch":0.0393701,"Km":0.000001,"Hm":0.00001,"Meter":0.001,"Dm":0.01,"Cm":0.1,"Mm":1,"Light Second":3.33564e-12
                   }
        self.lightsecondTo = { "mile":186282.4,"Nautical mile":161771.9,"Nautical League":53923.97,"Furlong":1490259,"Chain":14902590,"rod":59610370,"yard":327857000,
                              "Feet":983571100,"inch":11802850000,"Km":299792.5,"Hm":2997925,"Meter":299792500,"Dm":2997925000,"Cm":29979250000,"Mm":299792500000,"Light Second":1
                   }

        self.linearWidget = QWidget(self)
        self.box1 = QComboBox()
        self.box2 = QComboBox()
        self.entry = QLineEdit()
        self.edit = QLineEdit()
        self.edit.setReadOnly(True)
        self.setWindowTitle("ConvertMe - Linear")
        
######Construct Interface Look#######################
        self.edit.setMinimumHeight(40)
        self.edit.setFont(QFont('', 15))
        self.edit.setAlignment(Qt.AlignmentFlag.AlignRight)
        label1 = QLabel("From:")
        label2 = QLabel("To:")
        self.Button = QPushButton("Convert")
        self.label3 = QLabel()

        layout =QVBoxLayout(self.linearWidget)
        layout.addWidget(self.edit)
        layout.addWidget(label1)
        layout.addWidget(self.box1)
        layout.addWidget(label2)
        layout.addWidget(self.box2)
        layout.addWidget(self.entry)
        layout.addWidget(self.Button)
        layout.addWidget(self.label3)
        
        
        self.box1.addItem("")
        self.box1.addItem("Mile")
        self.box1.addItem("Nautical Mile")
        self.box1.addItem("Nautical League")
        self.box1.addItem("Furlong")
        self.box1.addItem("Chain")
        self.box1.addItem("Rod")
        self.box1.addItem("Yard")
        self.box1.addItem("Feet")
        self.box1.addItem("Inch")
        self.box1.addItem("km")
        self.box1.addItem("hm")
        self.box1.addItem("meter")
        self.box1.addItem("dm")
        self.box1.addItem("cm")
        self.box1.addItem("mm")
        self.box1.addItem("lightsecond")
        self.box2.addItems(sorted(self.milesTo.keys()))
#####################################################
        
        self.entry.setValidator(QDoubleValidator(
            -999.0, 999.0, 2, self.entry))
        self.label3.setStyleSheet('''
        QLabel {color:red;}''')
        self.setLayout(layout)
        self.entry.setMaxLength(15)
       
     
        self.setCentralWidget(self.linearWidget)
        self.box1.activated[int].connect(self.linearChange)
        self.Button.setShortcut("Return")
        
    def linearChange(self, index):
        """connects selected index to matching function"""
        if index == 1:
            self.Button.clicked.connect(self.Mile)
        elif index == 2:
            self.Button.clicked.connect(self.nauticalMile)
        elif index == 3:
            self.Button.clicked.connect(self.nauticalLeague)
        elif index == 4:
            self.Button.clicked.connect(self.Furlong)
        elif index == 5:
            self.Button.clicked.connect(self.chain)
        elif index == 6:
            self.Button.clicked.connect(self.rod)
        elif index == 7:
            self.Button.clicked.connect(self.yard)
        elif index == 8:
            self.Button.clicked.connect(self.Feet)
        elif index == 9:
            self.Button.clicked.connect(self.inch)
        elif index == 10:
            self.Button.clicked.connect(self.km)
        elif index == 11:
            self.Button.clicked.connect(self.hm)
        elif index == 12:
            self.Button.clicked.connect(self.meter)
        elif index == 13:
            self.Button.clicked.connect(self.dm)
        elif index == 14:
            self.Button.clicked.connect(self.cm)
        elif index == 15:
            self.Button.clicked.connect(self.mm)
        elif index == 16:
            self.Button.clicked.connect(self.lightsecond)
        
    def Mile(self):
        answer =  self.milesTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        
    def nauticalMile(self):
        answer =  self.NauticalmileTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    
    def nauticalLeague(self):
        answer =  self.NauticalLeagueTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    
    def  Furlong(self):
        answer =  self.FurlongTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    
    def chain(self):
        answer =  self.chainTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def rod(self):
        answer =  self.rodTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def yard(self):
        answer =  self.yardTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def Feet(self):
        answer =  self.feetTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    
    def inch(self):
        answer =  self.inchTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
        
    def km(self):
        answer =  self.kmTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def hm(self):
        answer =  self.hmTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def meter(self):
        answer =  self.meterTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def dm(self):
        answer =  self.dmTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def cm(self):
        answer =  self.cmTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def mm(self):
        answer =  self.mmTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def lightsecond(self):
        answer =  self.lightsecondTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
        
        
