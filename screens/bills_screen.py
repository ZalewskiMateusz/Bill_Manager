from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtWidgets import QMessageBox, QLineEdit, QPushButton, QCheckBox, QLabel, QHBoxLayout, QWidget, QVBoxLayout, \
    QMainWindow


class HomeScreen(QMainWindow):
    """
       The main window of the Bills Manager application.

       This class creates the main UI layout, including:
       - A navbar with input and button to add payments.
       - A central body area that displays all payment entries.
       - A summary section showing total amount.

       Attributes:
           payment_count (int): Counter to alternate row colors for payments.
           payment_textbox (QLineEdit): Input field to enter payment name.
           body_layout (QVBoxLayout): Layout to hold all payment entries.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bills Manager")
        self.setGeometry(100, 100, 800, 600)

        self.payment_count = 0

        # Main Container
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main Layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # NAVBAR
        navbar = QWidget()
        navbar_layout = QHBoxLayout()
        navbar.setLayout(navbar_layout)
        navbar.setStyleSheet('background-color: darkGray')

        # NAVBAR ELEMENTS
        title_label = QLabel("Bill Manager")

        self.payment_textbox = QLineEdit()
        self.payment_textbox.setPlaceholderText("Add new payment...")

        add_payment_button = QPushButton("Add Payment")
        add_payment_button.clicked.connect(self.add_payment)

        navbar_layout.addWidget(title_label)
        navbar_layout.addWidget(self.payment_textbox)
        navbar_layout.addWidget(add_payment_button)

        # BODY
        self.body = QWidget()
        self.body_layout = QVBoxLayout()
        self.body.setLayout(self.body_layout)

        # SUMMARY
        sum_section = QWidget()
        sum_section_layout = QHBoxLayout()
        sum_section.setLayout(sum_section_layout)
        sum_section.setStyleSheet('background-color: gray')



        self.sum_lbl = QLabel('Summary to pay: 0,00 zł')
        sum_section_layout.addWidget(self.sum_lbl)

        # Add NAVBAR and Body to main_layout
        main_layout.addWidget(navbar)
        main_layout.addWidget(self.body)
        main_layout.addWidget(sum_section)

    def add_payment(self):
        """
        Adds a new payment entry to the main view.

        This method retrieves the text from the input field (self.payment_textbox),
        and if it is not empty, creates a new horizontal layout with:
            - a label showing the payment description,
            - an input field for entering the payment amount,
            - a checkbox, with default true value, to validate if current payment is needed
            - a button for editing the entry (placeholder for future functionality),
            - a del button to delete whole current payment section.

        The created layout is added to the vertical body layout that holds all payment entries.
        After the entry is added, the input field is cleared.
        """
        text = self.payment_textbox.text()
        if text.strip():

            payment = Payment(text)

            if self.payment_count % 2 == 0:
                payment.setStyleSheet("background-color: #f9f9f9;")
            else:
                payment.setStyleSheet("background-color: #e6e6e6;")

            self.body_layout.addWidget(payment)

            self.payment_textbox.clear()
            self.payment_count += 1

            payment.connect_signals(self.calculate_summary)

    def calculate_summary(self):
        """
        Calculates the total sum from all Payment widgets
        that are checked with 'Add to summary' checkbox.
        """
        total = 0.00

        for i in range(self.body_layout.count()):
            payment_widget = self.body_layout.itemAt(i).widget()

            if isinstance(payment_widget, Payment):
                if payment_widget.val_payment_cbox.isChecked():
                    text = payment_widget.payment_amount.text().replace(',', '.')
                    try:
                        value = float(text)
                        total += value
                        self.sum_lbl.setText(
                            f"Summary to pay: {total:,.2f} zł".replace(",", "X").replace(".", ",").replace("X", "."))
                    except ValueError:
                        pass  # ignore invalid entries (e.g. empty or incorrect format)




class Payment(QWidget):
    """
    Represents a single payment entry in the Bills Manager UI.

    Components:
        - Label: shows the name/description of the payment.
        - LineEdit: input for entering the payment amount.
        - QCheckBox: allows toggling inclusion in summary.
        - QPushButton (Edit): placeholder for future editing functionality.
        - QPushButton (Delete): placeholder for future deletion functionality.
    """
    def __init__(self, name: str):
        super().__init__()

        self.payment_layout = QHBoxLayout()
        self.setLayout(self.payment_layout)
        self.setFixedHeight(45)

        self.name = name

        # label with payment description
        self.label = QLabel(name)
        self.label.setStyleSheet("padding: 5px; border: 1px solid gray;")

        # texbox for pay amount
        self.payment_amount = QLineEdit()
        self.payment_amount.setPlaceholderText('0,00')
        self.payment_amount.setFixedWidth(80)

        validator = QDoubleValidator(0.00, 999999.99, 2) #min, max, precision
        validator.setNotation(QDoubleValidator.Notation.StandardNotation)
        self.payment_amount.setValidator(validator)

        # validate checkbox
        self.val_payment_cbox = QCheckBox('Add to summary')
        self.val_payment_cbox.setFixedWidth(180)
        self.val_payment_cbox.setChecked(True)

        # EDIT
        self.edit_button = QPushButton('Edit')
        self.edit_button.setFixedWidth(90)

        self.edit_button.clicked.connect(self.edit_payment)


        # DELETE
        self.del_button = QPushButton('Delete')
        self.del_button.setFixedWidth(90)
        self.del_button.clicked.connect(self.del_payment)

        # Add elements to payment layout
        self.payment_layout.addWidget(self.label)
        self.payment_layout.addWidget(self.payment_amount)
        self.payment_layout.addWidget(self.val_payment_cbox)
        self.payment_layout.addWidget(self.edit_button)
        self.payment_layout.addWidget(self.del_button)

    def edit_payment(self):
        """
        Allows editing the payment name.

        Hides the label and replaces it with a QLineEdit.
        When Enter is pressed, saves the new name.
        """
        self.name_input = QLineEdit(self.label.text())
        self.payment_layout.removeWidget(self.label)
        self.label.hide()

        self.payment_layout.insertWidget(0, self.name_input)
        self.name_input.setFocus()
        self.name_input.returnPressed.connect(self.save_edit)

    def save_edit(self):
        """
        Saves the new name entered in the QLineEdit,
        updates the label, and restores the UI.
        """
        new_name = self.name_input.text()
        self.name = new_name
        self.label.setText(new_name)

        self.payment_layout.removeWidget(self.name_input)
        self.name_input.deleteLater()

        self.payment_layout.insertWidget(0, self.label)
        self.label.show()

    def del_payment(self):
        """
        Asks for confirmation and deletes the current payment widget
        if user confirms the action.
        """
        reply = QMessageBox.question(self, 'Delete Payment',
                                     f"Are you sure you want to delete '{self.label.text()}'?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            parent = self.parent()
            self.setParent(None)
            self.deleteLater()
            if hasattr(parent, 'calculate_summary'):
                parent.calculate_summary()

    def connect_signals(self, callback):
        self.payment_amount.textChanged.connect(callback)
        self.val_payment_cbox.stateChanged.connect(callback)

