from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, \
    QApplication, QStackedWidget
import sys

from screens.category_screen import CategoryWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bills Manager")
        self.setGeometry(100, 100, 800, 600)

        # Main Container
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # ========== MAIN LAYOUT ========== #
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        #Main Navbar
        main_navbar = QWidget()
        main_navbar_layout = QHBoxLayout()
        main_navbar.setLayout(main_navbar_layout)
        main_navbar.setFixedHeight(90)

        #Main Navbar - buttons
        home_btn = QPushButton("Home")
        home_btn.setIcon(QIcon("icons/home.png"))
        home_btn.setIconSize(QSize(24, 24))
        home_btn.clicked.connect(self.goto_home)

        reports_btn = QPushButton("Reports")
        reports_btn.setIcon(QIcon("icons/reports.png"))
        reports_btn.setIconSize(QSize(24, 24))

        savings_btn = QPushButton("Savings")
        savings_btn.setText("Savings")
        savings_btn.setIcon(QIcon("icons/piggy.png"))
        savings_btn.setIconSize(QSize(24, 24))
        savings_btn.setFixedWidth(100)

        language_btn = QPushButton("Language")
        language_btn.setFixedWidth(100)

        main_navbar_layout.addWidget(home_btn)
        main_navbar_layout.addWidget(reports_btn)
        main_navbar_layout.addWidget(savings_btn)
        main_navbar_layout.addWidget(language_btn)

        main_layout.addWidget(main_navbar)  # Navbar

        # ========== MIDDLE LAYOUT ========== #
        middle_layout = QHBoxLayout()
        main_layout.addLayout(middle_layout)

        #Main Side Menu
        main_sideMenu = QWidget()
        main_sideMenu_layout = QVBoxLayout()
        main_sideMenu.setLayout(main_sideMenu_layout)
        main_sideMenu.setStyleSheet('background-color: #1D1E18')
        main_sideMenu.setFixedWidth(120)

        #Side Menu - buttons + labels
        title_menu_lbl = QLabel("MENU")
        title_menu_lbl.setStyleSheet('background-color: #B0C7BD')
        title_menu_lbl.setFixedHeight(20)
        title_menu_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.categories_btn = QPushButton("CATEGORIES")
        self.categories_btn.setStyleSheet('background-color: #EDF2EF')
        self.categories_btn.clicked.connect(self.goto_categories)

        history_btn = QPushButton("HISTORY")
        history_btn.setStyleSheet('background-color: #EDF2EF')

        main_sideMenu_layout.addWidget(title_menu_lbl)
        main_sideMenu_layout.addWidget(self.categories_btn)
        main_sideMenu_layout.addWidget(history_btn)

        middle_layout.addWidget(main_sideMenu)  # Side Menu on left

        # ========== CENTRAL VIEW (zmieniany ekran) ========== #
        self.central_view = QStackedWidget()
        middle_layout.addWidget(self.central_view)  # Central view

        # ========== VIEWS ========== #
        self.home_screen = HomeScreen()
        self.categories_screen = CategoryWindow()
        self.history_screen = QLabel("HISTORY SCREEN")

        self.central_view.addWidget(self.home_screen)
        self.central_view.addWidget(self.categories_screen)
        self.central_view.addWidget(self.history_screen)

        self.central_view.setCurrentWidget(self.home_screen)  # default view

    def goto_home(self):
        self.central_view.setCurrentWidget(self.home_screen)

    def goto_categories(self):
        self.central_view.setCurrentWidget(self.categories_screen)


class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Welcome to Bills Manager!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        self.setLayout(layout)

        self.setStyleSheet("""
            background-image: url('resources/Home Screen.jpg');  /* background path */
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
        """)
