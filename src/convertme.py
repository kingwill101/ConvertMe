from PySide.QtGui import *
from PySide.QtCore import QObject,Qt,QFile
from linear.linear import Linear
from volume.volume import Volume
from area.area import Area
from pythogarus import Pythogarus
from PySide.QtUiTools import *
import sys

class Mainwin(QMainWindow , Linear, Area, Volume, Pythogarus):
    def __init__(self):
        super(Mainwin, self).__init__()
        
        menu = self.menuBar()
        statusbar = self.statusBar()
        self.firstWidget = QWidget(self)
      

        
        layout =QVBoxLayout(self.firstWidget)
        self.label4 = QLabel("<center><p style = color:red;>Please go to the Convert Type Menu<br> and select the type of conversion<br> you want to do</p></center>")
      
        
        closeAction = QAction("Quit", self)
        closeAction.triggered.connect(self.close)
        closeAction.setStatusTip("Quit")
        closeAction.setIcon(QIcon("img/close.png"))
        
        linearAction = QAction("Linear", self)
        linearAction.triggered.connect(self.linearClass)
        linearAction.setStatusTip("Linear Conversions")
        linearAction.setIcon(QIcon("img/linear.png"))
        
        volumeAction = QAction("Volume", self)
        volumeAction.triggered.connect(self.volumeClass)
        volumeAction.setShortcut("Ctrl + v")
        volumeAction.setStatusTip("Volumetric Conversions")
        
        
        areaAction = QAction("Area", self)
        areaAction.triggered.connect(self.areaClass)
        areaAction.setStatusTip("Area Conversions")
        aboutAction = QAction("About", self)
        aboutAction.setIcon(QIcon("img/about.png"))
        aboutAction.triggered.connect(self.About)
        
        PythogarusAction = QAction("Pythogarus Theorem", self)
        PythogarusAction.setStatusTip("Pythogarus Theorem")
        PythogarusAction.triggered.connect(self.gui)
        
        
        fileMenu = menu.addMenu("File")
        fileMenu.addAction(closeAction)
        
        AlgebraMenu = menu.addMenu("Algebra")
        AlgebraMenu.addAction(PythogarusAction)
        
        ConvertMenu = menu.addMenu("Convert Type")
        ConvertMenu.addAction(linearAction)
        ConvertMenu.addAction(areaAction)
        ConvertMenu.addAction(volumeAction)
        
        helpMenu = menu.addMenu("&Help")
        aboutMenu = menu.addMenu("&About")
        aboutMenu.addAction(aboutAction)
        
        self.setWindowIcon(QIcon("img/pic_balance.png") )
        self.setWindowTitle("ConvertMe")
        self.resize(300,300)
        self.setMaximumHeight(300)
        self.setMaximumWidth(300)
        self.setCentralWidget(self.firstWidget)
        self.setLayout(layout)
        self.show()
        
        
        
        
    def linearClass(self):
        self.linnear()
    def volumeClass(self):
        self.volume()
    def areaClass(self):
        self.area()
    def Help(self):
        pass
    def About(self):
		QMessageBox.about(self, "About ConverMe",
                """<p>Author: Glenford Williams<br>
                                License: GPL V2<br>
				contact: glenford.williams@samsharpe.edu.jm<br>
					version: .5<br>
					<br>
					About Convertme<br>
					##############################################################<br>

                                        A simple tool for handling various mathematical functions including unit
                                        conversions and Algebra related stuff like Pythogarus Theorem<br>
					</p>
					""")
      
