from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QTableWidget, QTableWidgetItem, QSpinBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
import sys

class InventoryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P1: Student scores and grades")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        input_layout = QHBoxLayout()
        