from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My First Window")

        label = QLabel("First text")
        
        self.setCentralWidget(label)

app = QApplication(sys.argv)


window = MainWindow()
window.show() #IMPORTANT!!!
app.exec()