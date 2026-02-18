import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                             QVBoxLayout, QHBoxLayout, QFormLayout, QGridLayout, QWidget, QLabel, QLineEdit)
from PySide6.QtWidgets import QPushButton, QComboBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

kg = "kilograms"
lb = "pounds"
cm = "centimeters"
m = "meters"
ft = "feet"
adult = "Adults 20+"
child = "Children and Teenagers (5-19)"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("P1: BMI Calculator")
        self.setGeometry(100, 100, 300, 450)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Header
        header = QLabel("Adult and Child BMI Calculator")
        header.setStyleSheet("background-color: #A52A2A; color: white; font-weight: bold; font-size: 16px; padding: 5px;")
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)
        main_layout.addSpacing(10)
        
        self.input_section = InputSection()
        main_layout.addWidget(self.input_section) 
        
       
        self.output_section = OutputSection()

        result_container = QWidget()
        result_container.setStyleSheet("background-color: #FAF0E6;")  # Linen color
        
        # result_container needs a layout to hold the output_section widget
        res_layout = QVBoxLayout(result_container)
        res_layout.setContentsMargins(0,0,0,0)
        res_layout.addWidget(self.output_section)
        
        main_layout.addWidget(result_container)

        # connect signals
        self.input_section.btn_submit.clicked.connect(lambda: self.input_section.submit_reg(self.output_section))
        self.input_section.btn_clear.clicked.connect(lambda: self.input_section.clear_form(self.output_section))


class OutputSection(QWidget):
    def __init__(self):
        super().__init__()
        # Create an internal layout for the widget
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setAlignment(Qt.AlignTop)

        self.lbl_title = QLabel("Your BMI")
        self.lbl_title.setAlignment(Qt.AlignCenter)
        self.lbl_title.setStyleSheet("color: black;")
        self.lbl_result = QLabel("0.00")
        self.lbl_result.setFont(QFont("Arial", 24, QFont.Bold))
        self.lbl_result.setStyleSheet("color: blue;")
        self.lbl_result.setAlignment(Qt.AlignCenter)
        
        self.main_layout.addSpacing(20)
        self.main_layout.addWidget(self.lbl_title)
        self.main_layout.addWidget(self.lbl_result)
        self.main_layout.addSpacing(10)

    def show_adult_table(self):
        table_widget = QWidget()
        table_layout = QGridLayout(table_widget)
        
        headers = [("BMI", 0), ("Condition", 1)]
        rows = [("< 18.5", "Thin"), ("18.5 - 25.0", "Normal"), ("25.1 - 30.0", "Overweight"), ("> 30.0", "Obese")]
        
        for text, col in headers:
            label = QLabel(text)
            label.setFont(QFont("Arial", 10, QFont.Bold))
            table_layout.addWidget(label, 0, col, Qt.AlignCenter if col == 0 else Qt.AlignLeft)
        
        for i, (bmi_range, condition) in enumerate(rows, 1):
            table_layout.addWidget(QLabel(bmi_range), i, 0, Qt.AlignCenter)
            table_layout.addWidget(QLabel(condition), i, 1)
        
        self.main_layout.addWidget(table_widget)

    def show_child_link(self):
        info_label = QLabel("For child's BMI interpretation, please click one of the following links:")
        info_label.setWordWrap(True)
        info_label.setAlignment(Qt.AlignCenter)
        info_label.setStyleSheet("color: black;")
        self.main_layout.addWidget(info_label)
        
        link_container = QWidget()
        link_layout = QHBoxLayout(link_container)
        boy_link = QLabel('<a href="https://cdn.who.int/media/docs/default-source/child-growth/growth-reference-5-19-years/bmi-for-age-(5-19-years)/cht-bmifa-boys-z-5-19years.pdf">BMI graph for BOYS</a>')
        girl_link = QLabel('<a href="https://cdn.who.int/media/docs/default-source/child-growth/growth-reference-5-19-years/bmi-for-age-(5-19-years)/cht-bmifa-girls-z-5-19years.pdf">BMI graph for GIRLS</a>')
        
        for link in [boy_link, girl_link]:
            link.setOpenExternalLinks(True)
            link_layout.addWidget(link)
            
        self.main_layout.addWidget(link_container)

    def update_results(self, bmi, age_group):
        self.clear_result()
        self.lbl_result.setText(f"{bmi:.2f}")
        if age_group == adult:
            self.show_adult_table()
        else:
            self.show_child_link()
    
    def clear_result(self):
        self.lbl_result.setText("0.00")
        while self.main_layout.count() > 3:
            item = self.main_layout.takeAt(3)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self.clear_layout(item.layout())
    
    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self.clear_layout(item.layout())

class InputSection(QWidget):
    def __init__(self):
        super().__init__()
        # Create an internal layout for the widget
        self.main_layout = QVBoxLayout(self)

        form_layout = QFormLayout()
        
        self.age_combo = QComboBox()
        self.age_combo.addItems([adult, child])
        
        self.weight_input = QLineEdit()
        self.weight_unit = QComboBox()
        self.weight_unit.addItems([kg, lb])
        weight_row = QHBoxLayout()
        weight_row.addWidget(self.weight_input)
        weight_row.addWidget(self.weight_unit)
        
        self.height_input = QLineEdit()
        self.height_unit = QComboBox()
        self.height_unit.addItems([cm, m, ft])
        height_row = QHBoxLayout()
        height_row.addWidget(self.height_input)
        height_row.addWidget(self.height_unit)
        
        form_layout.addRow("BMI age group:", self.age_combo)
        form_layout.addRow("Weight:", weight_row)
        form_layout.addRow("Height:", height_row)
        
        self.main_layout.addLayout(form_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        self.btn_clear = QPushButton("clear")
        self.btn_submit = QPushButton("Submit Registration")
        button_layout.addWidget(self.btn_clear)
        button_layout.addWidget(self.btn_submit)
        self.main_layout.addLayout(button_layout)

    def clear_form(self, output_section):
        self.weight_input.clear()
        self.height_input.clear()
        output_section.clear_result()

    def submit_reg(self, output_section):
        try:
            bmi = self.calculate_BMI()
            output_section.update_results(bmi, self.age_combo.currentText())
        except ValueError:
            pass

    def calculate_BMI(self):
        w_text = self.weight_input.text()
        h_text = self.height_input.text()
        if not w_text or not h_text: raise ValueError
        
        w = float(w_text)
        h = float(h_text)
        
        if self.weight_unit.currentText() == lb:
            w = w * 0.453592
            
        h_unit = self.height_unit.currentText()
        if h_unit == cm:
            h = h / 100
        elif h_unit == ft:
            h = h * 0.3048
            
        return w / (h * h)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()