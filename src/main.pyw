from PySide.QtGui import QApplication
from  convertme import *
import sys

def main():
	app = QApplication(sys.argv)
	window = Mainwin()
	sys.exit(app.exec_())
	
	return 0

if __name__ == '__main__':
	main()
