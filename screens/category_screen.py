from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QStackedWidget

class CategoryWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # Navbar with buttons
        mini_category_navbar = QWidget()
        mini_category_navbar_layout = QHBoxLayout()
        mini_category_navbar.setLayout(mini_category_navbar_layout)
        mini_category_navbar.setFixedHeight(50)

        all_categories_button = QPushButton("All Categories")
        all_payments_button = QPushButton("All Payments")

        mini_category_navbar_layout.addWidget(all_categories_button)
        mini_category_navbar_layout.addWidget(all_payments_button)

        layout.addWidget(mini_category_navbar)

        # Stack for views
        self.stack = QStackedWidget()
        layout.addWidget(self.stack)

        # Dummy screens
        self.all_categories_screen = self.create_dummy_view("All Categories Content")
        self.all_payments_screen = self.create_dummy_view("All Payments Content")

        self.stack.addWidget(self.all_categories_screen)
        self.stack.addWidget(self.all_payments_screen)

        # Button connections
        all_categories_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.all_categories_screen))
        all_payments_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.all_payments_screen))

    def create_dummy_view(self, text):
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel(text))
        widget.setLayout(layout)
        return widget