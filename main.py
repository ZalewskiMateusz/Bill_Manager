import sys
from PyQt6.QtWidgets import QApplication
from screens.home_screen import HomeScreen

app = QApplication(sys.argv)
window = HomeScreen()
window.show()
sys.exit(app.exec())