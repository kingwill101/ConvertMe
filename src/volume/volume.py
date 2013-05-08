from PySide.QtGui import *
from PySide.QtCore import QObject,Qt

#####################################################################################################################################################
class Volume(object):
    def volume(self):
        self.gallonsTo= {"gallons":1, "quarts": 4,  "pints":8, "gills":32, "cu. inches": 277.4192, "fl.oz.":160, "US fl.oz.":153.7219, "fl. drachms":1280, "US gal": 1.200913, "US pint": 9.607621,
		 "cu. yard":0.00594606, "cu. feet":0.160544, "cu. inch": 277.4194, "cu. m": 0.0045461,"litres":4.5461,"cu. dm":4.5461,"cc":4546.1, "ml": 4546.1}
		
        self.quartsTo= {"gallons":0.25, "quarts": 1,  "pints":2, "gills":8, "cu. inches": 69.3548, "fl.oz.":40, "US fl.oz.":38.43048, "fl. drachms":320, "US gal": 0.300228, "US pint": 2.401905, 
		"cu. yard":0.00148652, "cu. feet":0.0401359, "cu. inch": 69.35486, "cu. m": 0.00113653,"litres":1.136525,"cu. dm":1.136525,"cc":1136.525, "ml": 1136.525}

        self.pintsTo= {
		"gallons":0.125,"quarts": 0.5,   "pints":1, "gills":4, "cu. inches": 34.6774,"fl.oz.":20, "US fl.oz.":19.21524, "fl. drachms":160, "US gal": 0.150114, 
		"US pint": 1.200953, "cu. yard":0.000743258, "cu. feet":0.020068, "cu. inch": 34.67743, "cu. m": 0.000568263,"litres":0.568263,"cu. dm":0.568263,"cc":568.2625, "ml": 568.2625}

        self.gillTo= {
		"gallons":0.03125,"quarts": 0.125,  "pints":0.25, "gills":1, "cu. inches": 8.66935, "fl.oz.":5,  "US fl.oz.":4.80381, "fl. drachms":40, "US gal": 0.0375285, "US pint": 0.300238, 
		"cu. yard":0.000185814,  "cu. feet":0.00501699, "cu. inch": 8.669357,  "cu. m": 0.000142066, "litres":0.142066, "cu. dm":0.142066, "cc":142.0656,  "ml": 142.0656}

##need to add option for inches
        self.cuInchesTo= {
		"gallons":0.00360465,"quarts": 0.0144186,   "pints":0.0288372, "gills":0.115349, "cu. inches": 1, "cu. inch": 1, "fl.oz.":0.576745,  "US fl.oz.":0.554114, "fl. drachms":4.613956, "US gal": 0.00432887,
		"US pint": 0.0346321,  "cu. yard":0.0000214335,  "cu. feet":0.000578704, "cu. m": 0.0000163871,"litres":0.0163871,"cu. dm":0.0163871, 
		"cc":16.38711, "ml": 16.38711}

        self.flOzTo= {
		"gallons":0.00625001,"quarts": 0.025,   "pints":0.05, "gills":1.733872, "cu. inches": 1, "fl.oz.":1,  "US fl.oz.":0.960763, "fl. drachms":8.000007, 
		"US gal": 0.00750571,"US pint": 0.0600477, "cu. yard":0.0000371629, "cu. feet":0.0010034, "cu. inch": 1.733873, "cu. m": 0.0000284132,"litres":0.0284132,"cu. dm":0.0284132,
		"cc":28.41315,  "ml": 28.41315}

        self.usFlOzTo= {
		"gallons":0.00650525, "quarts": 0.026021,  "pints":0.052042, "gills":0.208168, "cu. inches": 1.804682, "fl.oz.":1.04084,  "US fl.oz.":0.960763, "fl. drachms":1,
		"US gal": 0.00781224, "US pint": 0.0625,  "cu. yard":0.0000386806, "cu. feet":0.00104438,  "cu. inch": 1.804684,  "cu. m": 0.0000295735, 
		"litres":0.0295735, "cu. dm":0.0295735, "cc":29.57353,  "ml": 29.57353}

        self.flDrachmsTo= {
		"gallons":0.00078125,"quarts": 0.003125,  "pints":0.003125, "gills":0.025, "cu. inches": 0.216734, "fl.oz.":0.125,  "US fl.oz.":0.120095, "fl. drachms":1, "US gal": 0.000938213,
		"US pint": 0.00750595,"cu. yard":0.00000464536,  "cu. feet":0.000125425,  "cu. inch": 0.216734,  "cu. m": 0.00000355164, "litres":0.00355164, "cu. dm":0.00355164, "cc":3.551641,  "ml": 3.551641}

        self.usGalTo= {"gallons":0.8327, "quarts": 3.3308,   "pints":6.6616, "gills":26.6464, "cu. inches": 231.007, "fl.oz.":133.232,  "US fl.oz.":128.0042, "fl. drachms":1065.856, "US gal": 1,
		"US pint": 8.000266, "cu. yard":0.00495129, "cu. feet":0.133685, "cu. inch": 231.0072, "cu. m": 0.00378554,"litres":3.785537,"cu. dm":3.785537,"cc":3785.537, "ml": 3785.537}

        self.usPintTo= {"gallons":0.100007, "quarts": 0.400026, "pints":0.800053, "gills":3.200211, "US gall":0, "US gal": 0,
		"cu. inches": 27.74375,"fl.oz.":16.00106, "US fl.oz.":15.37321, "fl. drachms":128.0084,  "US pint": 0.960825, "cu. yard":0.000594645,  "cu. feet":0.0160554,  "cu. inch": 27.74377,  "cu. m": 0.00045464, "litres":0.45464, "cu. dm":0.45464, "cc":454.64, 
		"ml": 454.64}

        self.cuYardTo= {"gallons":168.1786, "quarts": 672.7142,   "pints":1345.428, "gills":5381.714, "cu. inches": 46655.96, "fl.oz.":26908.57,  "US fl.oz.":25852.73, "fl. drachms":215268.6, "US gal": 201.9678,
		"US pint": 1615.796,"cu. yard":1,  "cu. feet":27, "cu. inch": 27.74377,  "cu. m": 0.764557, "litres":764.5565, "cu. dm":764.5565, "cc":764556.5,  "ml": 764556.5}

        self.cuFeetTo= {"gallons":6.228835,"quarts": 24.91534,   "pints": 49.83068, "gills":199.3227, "cu. inches": 1727.999, "fl.oz.":996.6137,  "US fl.oz.":25852.73, 
		"fl. drachms":7972.909, "US gal": 7.480288, "US pint": 59.84429,  "cu. yard": 0.037037,  "cu. feet":1,  "cu. inch": 1728,  "cu. m": 0.0283169, "litres":28.31691, "cu. dm":28.31691, "cc":28316.91,  "ml": 28316.91}


        self.cuInchTo= {"gallons":0.00360465, "quarts": 0.0144186,   "pints": 0.0288372, "gills": 0.115349, "cu. inches": 0.999999158, "fl.oz.": 0.576744,  "US fl.oz.": 0.554114, "fl. drachms": 4.613952, 
		"US gal": 0.00432887,"US pint": 0.0346321, "cu. yard": 0.0000214335, "cu. feet":0.000578704,  "cu. inch": 1,  "cu. m": 0.0000163871,"litres": 0.0163871, "cu. dm": 0.0163871, "cc": 16.3871,  "ml": 16.3871}
		
####needs to be checked, possible mix up of dictionary names
        self.cuMTo= {"gallons":219.9688, "quarts": 879.8751,  "pints": 1759.75, "gills": 7039, "cu. inches": 61023.56,"fl.oz.": 35195, "US fl.oz.": 33814.02, "fl. drachms": 281560, "US gal": 264.1633, "US pint": 2113.376,  "cu. yard": 1.307948,  "cu. feet": 35.31459,  "cu. inch": 61023.61,  "cu. m": 1, "litres": 1000,"cu. dm": 1000,"cc": 1000000, "ml": 1000000}

        self.litresTo= {
		"gallons":0.219969, "quarts": 0.879875,   "pints": 1.75975, "gills": 7.039, "cu. inches": 61.02356, "fl.oz.": 35.195,  "US fl.oz.": 33.81402, 
		"fl. drachms": 281.56, "US gal": 0.264163, "US pint": 2.113376,  "cu. yard": 0.00130795,  "cu. feet": 0.0353146, "cu. inch": 61.02361, 
		"cu. m": 0.001,"litres": 1,"cu. dm": 1,"cc": 1000, "ml": 1000}

        self.cuDmTo= {"gallons":0.219969, "quarts": 0.879875,   "pints": 1.7595, "gills": 7.039, "cu. inches": 61.02356, "fl.oz.": 35.195,  "US fl.oz.":33.81402, "fl. drachms": 281.56, "US gal": 0.264163, "US pint": 2.113376,  "cu. yard": 0.00130795, 
		"cu. feet": 0.0353146,  "cu. inch": 61.02361,  "cu. m": 0.001, "litres": 1, "cu. dm": 1,"cc": 1000, "ml": 1000}

        self.ccTo= {
		"gallons":0.000219969, "quarts": 0.000879875,  "pints": 0.00175975, "gills": 0.007039, "cu. inches": 0.0610236,"fl.oz.": 0.035195, "US fl.oz.": 0.033814, "fl. drachms": 0.28156, "US gal": 0.000264163,"US pint": 0.00211338, 
		"cu. yard": 0.00000130795, "cu. feet": 0.0000353146, "cu. inch": 0.0610236,  "cu. m": 0.000001,"litres": 0.001,"cu. dm": 0.001,"cc": 1, "ml": 1}
####needs to be checked ,possible mix up of dictionary names
        self.mlTo= {"gallons":0.000219969, "quarts": 0.000879875,  "pints": 0.00175975,"gills": 0.007039,
		"cu. inches": 0.0610236,"fl.oz.": 0.035195, "US fl.oz.": 0.033814, "fl. drachms": 0.28156, "US gal": 0.000264163,
		 "US pint": 0.00211338, "cu. yard": 0.00000130795, "cu. feet": 0.0000353146,"cu. inch": 0.0610236,"cu. m": 0.000001,
		 "litres": 0.001,"cu. dm": 0.001,"cc": 1, "ml": 1
		 }
        self.volumeWidget = QWidget(self)
        self.box1 = QComboBox()
        self.box2 = QComboBox()
        self.entry = QLineEdit()
        self.edit = QLineEdit()
        self.edit.setReadOnly(True)
        self.setWindowTitle("ConvertMe - Volume")

######Construct Interface Look#######################
        self.edit.setMinimumHeight(40)
        self.edit.setFont(QFont('', 15))
        self.edit.setAlignment(Qt.AlignmentFlag.AlignRight)
        label1 = QLabel("From:")
        label2 = QLabel("To:")
        self.Button = QPushButton("Convert")
        self.label3 = QLabel()


        layout =QVBoxLayout(self.volumeWidget)

        layout.addWidget(self.edit)
        layout.addWidget(label1)
        layout.addWidget(self.box1)
        layout.addWidget(label2)
        layout.addWidget(self.box2)
        layout.addWidget(self.entry)
        layout.addWidget(self.Button)
        layout.addWidget(self.label3)
        ls = ["","gallons", "quarts", "pints", "gills",	"cu. inches", "fl.oz.", "US fl.oz.", "fl. drachms", "US gal",
			"US pint", "cu. yard", "cu. feet","cu. inch","cu. m","litres","cu. dm","cc", "ml"]
     	
        for i in sorted(ls):
		    self.box2.addItem(i)

        for keys in ls:
           self.box1.addItem(keys)
        ###################################################

        self.entry.setValidator(QDoubleValidator(
			-999.0, 999.0, 2, self.entry))
        self.label3.setStyleSheet('''
		QLabel {color:red;}''')
        self.setLayout(layout)
        self.entry.setMaxLength(15)

        self.setCentralWidget(self.volumeWidget)
        self.box1.activated[int].connect(self.volumeChange)
        self.Button.setShortcut("Return")
    
    def volumeChange(self, index):
        """connects selected index to matching function"""
        if index == 1:
            self.Button.clicked.connect(self.gallons)
        elif index == 2:
            self.Button.clicked.connect(self.quarts)
        elif index == 3:
            self.Button.clicked.connect(self.gills)
        elif index == 4:
            self.Button.clicked.connect(self.cuInches)
        elif index == 5:
            self.Button.clicked.connect(self.flOz)
        elif index == 6:
            self.Button.clicked.connect(self.usFlOz)
        elif index == 7:
            self.Button.clicked.connect(self.flDrachms)
        elif index == 8:
            self.Button.clicked.connect(self.usGal)
        elif index == 9:
            self.Button.clicked.connect(self.usPint)
        elif index == 10:
            self.Button.clicked.connect(self.cuYard)
        elif index == 11:
            self.Button.clicked.connect(self.cuFeet)
        elif index == 12:
            self.Button.clicked.connect(self.cuInch)
        elif index == 13:
            self.Button.clicked.connect(self.cuM)
        elif index == 14:
            self.Button.clicked.connect(self.litres)
        elif index == 15:
            self.Button.clicked.connect(self.cuDm)
        elif index == 16:
            self.Button.clicked.connect(self.cc)
        elif index == 17:
            self.Button.clicked.connect(self.ml)
    
    def gallons(self):
        answer =  self.gallonsTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        
        
        
    def quarts(self):
        answer =  self.quartsTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    
    def points(self):
        answer =  self.pointsTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    
    def  gills(self):
        answer =  self.gillTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    
    def cuInches(self):
        answer =  self.cuInchesTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def flOz(self):
        answer =  self.flOzTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def usFlOz(self):
        answer =  self.usFlOzTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def flDrachms(self):
        answer =  self.flDrachmsTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    
    def usGal(self):
        answer =  self.usGalTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
        
    def usPint(self):
        answer =  self.usPintTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def cuYard(self):
        answer =  self.cuYardTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def cuFeet(self):
        answer =  self.cuFeetTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def cuInch(self):
        answer =  self.cuInchTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def cuM(self):
        answer =  self.cuMTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def litres(self):
        answer =  self.litresTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def cuDm(self):
        answer =  self.cuDmTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def cc(self):
        answer =  self.ccTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass
    def ml(self):
        answer =  self.mlTo[self.box2.currentText()] * int(self.entry.displayText())
        self.edit.setText(str(answer))
        pass

    
