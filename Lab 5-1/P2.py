import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                                QVBoxLayout, QWidget, QHBoxLayout,
                                QGridLayout, QFormLayout, QLineEdit,
                                QLabel,QPushButton,QButtonGroup,
                                QRadioButton,QDateEdit,QComboBox,
                                QCheckBox,QTextEdit)

from PySide6.QtCore import Qt, QSize, QDate
from PySide6.QtGui import QPixmap, QFont


class MainWindow(QMainWindow):
    def __init__ (self):
        super().__init__()


        self.setWindowTitle("P2: Student Registration Form")
        self.setGeometry(100, 100, 400, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget) 

        title = QLabel("Student Registration Form")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        text_fullname = QLabel("Full Name:")
        text_fullname.setFont(QFont("Arial", 12))
        text_fullname.setAlignment(Qt.AlignLeft)
        layout.addWidget(text_fullname)

        fullname = QLineEdit()
        fullname.setFont(QFont("Arial", 12))
        layout.addWidget(fullname)

        text_email = QLabel("Email:")
        text_email.setFont(QFont("Arial", 12))
        text_email.setAlignment(Qt.AlignLeft)
        layout.addWidget(text_email)

        email = QLineEdit()
        email.setFont(QFont("Arial", 12))
        layout.addWidget(email)

        text_phone = QLabel("Phone:")
        text_phone.setFont(QFont("Arial", 12))
        text_phone.setAlignment(Qt.AlignLeft)
        layout.addWidget(text_phone)

        phone = QLineEdit()
        phone.setFont(QFont("Arial", 12))
        layout.addWidget(phone)

        text_date = QLabel("Date of Birth(dd/MM/yyyy):")
        text_date.setFont(QFont("Arial", 12))
        text_date.setAlignment(Qt.AlignLeft)
        layout.addWidget(text_date)
        
        date_edit = QDateEdit()
        date_edit.setCalendarPopup(True)  # Shows calendar dropdown
        date_edit.setDisplayFormat("dd/MM/yyyy")  # Format like "2/19/00"
        date_edit.setDate(QDate(2000, 1, 2000))  # Set default date
        layout.addWidget(date_edit)

        text_gender = QLabel("Gender:")
        text_gender.setFont(QFont("Arial", 12,))
        text_gender.setAlignment(Qt.AlignLeft)
        layout.addWidget(text_gender)
        # Button group ensures only one can be selected
        gender_group = QButtonGroup()
                
        radio_layout = QHBoxLayout()
        male_radio = QRadioButton("Male")
        female_radio = QRadioButton("Female")
        nonbinary_radio = QRadioButton("Non-binary")
        prefernot_radio = QRadioButton("Prefer not to say")
                
        gender_group.addButton(male_radio)
        gender_group.addButton(female_radio)
        gender_group.addButton(nonbinary_radio)
        gender_group.addButton(prefernot_radio)
                
        radio_layout.addWidget(male_radio)
        radio_layout.addWidget(female_radio)
        radio_layout.addWidget(nonbinary_radio)
        radio_layout.addWidget(prefernot_radio)

        layout.addLayout(radio_layout)

        # Add spacing between widgets
        layout.addSpacing(20)
        layout.addStretch()
    
        text_program = QLabel("Program:")
        text_program.setFont(QFont("Arial", 12))
        text_program.setAlignment(Qt.AlignLeft) 
        layout.addWidget(text_program)

        program = QComboBox()
        program.setPlaceholderText("Select your program")
        program.addItems(sorted(["Computer Engineering",
                            "Digital Media Engineering",
                            "Environmental Engineering",
                            "Electical Engineering",
                            "Semiconductor Engineering",
                            "Mechanical Engineering",
                            "Industrial Engineering",
                            "Logistic Engineering",
                            "Power Engineering",
                            "Electronic Engineering",
                            "Telecommunication Engineering",
                            "Agricultural Engineering",
                            "Civil Engineering",
                            "ARIS",
                            ]))
        program.setFont(QFont("Arial", 12))
        layout.addWidget(program)

        text_about_yourself = QLabel("Tell us a little bit about yourself:")
        text_about_yourself.setFont(QFont("Arial", 12))
        text_about_yourself.setAlignment(Qt.AlignLeft)
        layout.addWidget(text_about_yourself)

        about_yourself = QTextEdit()
        about_yourself.setFont(QFont("Arial", 12))
        about_yourself.setMaximumHeight(100)
        layout.addWidget(about_yourself)

        accept_button_group = QButtonGroup()
        accept_layout = QHBoxLayout()
        accept_radio = QCheckBox("I accept the terms and conditions")
        accept_button_group.addButton(accept_radio)
        accept_layout.addWidget(accept_radio)
        layout.addLayout(accept_layout)

        submit_button = QPushButton("Submit Registration")
        submit_button.setFont(QFont("Arial", 7))
        submit_button.setFixedSize(QSize(100, 30))
        layout.addWidget(submit_button, alignment=Qt.AlignCenter)

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()