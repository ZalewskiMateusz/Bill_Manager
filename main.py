import sys
from PyQt6.QtWidgets import QApplication
from screens.home_screen import MainWindow
from screens.category_screen import CategoryWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())