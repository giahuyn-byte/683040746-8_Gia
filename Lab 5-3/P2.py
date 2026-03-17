import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                                QVBoxLayout, QWidget, QHBoxLayout,
                                QGridLayout, QFormLayout, QLineEdit,
                                QLabel, QPushButton, QButtonGroup,
                                QRadioButton, QDateEdit, QComboBox,
                                QCheckBox, QTextEdit, QGroupBox,
                                QMessageBox, QTableWidget, QTableWidgetItem, 
                                QSpinBox, QMenu, QMenuBar, QStatusBar, 
                                QToolBar, QColorDialog, QFrame)

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
import pyqtgraph as pg
import numpy as np

MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
PRODUCTS = ["Electronics","Clothing","Food","Others"]
COLORS = {
    "Electronics": (70, 130, 180),   # blue
    "Clothing":    (255, 140, 0),    # orange
    "Food":        (60, 179, 60),    # green
    "Others":      (220, 60, 60),    # red
}


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("683040492-3")
        self.setCentralWidget(MonthlySalesChart())
        self.setGeometry(100, 100, 1170, 700)

        self.setStyleSheet("""
            QPushButton#add {
                background-color: green;
                color: white;
                padding: 5px 10px;
            }
            QPushButton#add:hover { background-color: rgba(0, 128, 0, 0.4); }
            QPushButton#clear {
                background-color: red;
                color: white;
                min-width: 120px;
                padding: 5px;
            }
            QPushButton#clear:hover { background-color: rgba(255, 0, 0, 0.4); }
        """)

class MonthlySalesChart(QWidget):
    def __init__(self):
        super().__init__()
        self.sales_data = {}  # key: (month, product) -> sales value

        layout = QVBoxLayout()
        self.setLayout(layout)

        # ====== File input ======
        layout_input = QHBoxLayout()
        layout_input.addWidget(QLabel("File Name:"))
        self.file_input = QLineEdit()
        self.file_input.setPlaceholderText("lap5-3/sales_data.txt")
        layout_input.addWidget(self.file_input)
        import_button = QPushButton("Import Data")
        import_button.setObjectName("add")
        import_button.clicked.connect(self.import_data)
        layout_input.addWidget(import_button)
        layout_input.addStretch()

        # ====== Data input ======
        layout_data = QHBoxLayout()
        layout_data.addWidget(QLabel("Month:"))
        self.month_input = QComboBox()
        self.month_input.setPlaceholderText("Select Month")
        self.month_input.addItems(MONTHS)
        layout_data.addWidget(self.month_input)

        layout_data.addWidget(QLabel("Sales:"))
        self.sales_input = QSpinBox()
        self.sales_input.setMinimum(0)
        self.sales_input.setMaximum(999999999)
        self.sales_input.setValue(0)
        layout_data.addWidget(self.sales_input)

        layout_data.addWidget(QLabel("Product Category:"))
        self.product_input = QComboBox()
        self.product_input.setPlaceholderText("Select Product")
        self.product_input.addItems(PRODUCTS)
        layout_data.addWidget(self.product_input)

        add_button = QPushButton("Add Data")
        add_button.setObjectName("add")
        add_button.clicked.connect(self.add_data)
        layout_data.addWidget(add_button)
        layout_data.addStretch()

        # ====== Graph ======
        self.graph = pg.PlotWidget()
        self.graph.setTitle("Monthly Sales")
        self.graph.setLabel("left", "Sales Amount")
        self.graph.setLabel("bottom", "Month")
        self.graph.getViewBox().setLimits(yMin=0)
        self.graph.setXRange(-0.5, 11.5)  # ← แสดงทุกเดือน Jan–Dec
        self.graph.setYRange(0, 250000) # ตั้งค่าเริ่มต้นให้ Y แสดง 0–250000 เพื่อให้เห็นสเกลชัดเจน
        self.graph.getViewBox().setLimits(xMin=-0.5, xMax=11.5) # ← ล็อก X ไม่ให้เลื่อน
        self.graph.showGrid(x=True, y=True, alpha=0.3) # Add grid with some transparency
        self.graph.getViewBox().setLimits(yMin=0)  # Prevent zooming below 0 on y-axis
        
        self.graph.setMouseEnabled(x=False, y=True) # ← zoom ได้แค่แกน Y

        # Set x-axis ticks to month names
        ax = self.graph.getAxis('bottom')
        ticks = [(i, m) for i, m in enumerate(MONTHS)]
        ax.setTicks([ticks])

        # Legend
        self.graph.addLegend(offset=(10, 10))
        for product in PRODUCTS:
            color = COLORS[product]
            dummy = pg.BarGraphItem(x=[], height=[], width=0.15,
                                    brush=pg.mkBrush(*color, 200),
                                    pen=pg.mkPen(*color),
                                    name=product)
            self.graph.addItem(dummy)

        # ====== Clear Button ======
        layout_button = QHBoxLayout()
        clear_button = QPushButton("Clear Chart")
        clear_button.setObjectName("clear")
        clear_button.setFont(QFont("Arial", 14, QFont.Bold))
        clear_button.clicked.connect(self.clear)
        layout_button.addWidget(clear_button)

        layout.addLayout(layout_input)
        layout.addLayout(layout_data)
        layout.addWidget(self.graph)
        layout.addLayout(layout_button)

    def import_data(self):
        filename = self.file_input.text().strip() or "sales_data.txt"
        try:
            with open(filename, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = [p.strip() for p in line.split(",")]
                    if len(parts) != 3:
                        continue
                    month, product, sales_str = parts
                    if month not in MONTHS or product not in PRODUCTS:
                        continue
                    try:
                        sales = int(sales_str)
                    except ValueError:
                        continue
                    self.sales_data[(month, product)] = sales
            self.update_chart()
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", f"File '{filename}' not found.")

    def add_data(self):
        month = self.month_input.currentText()
        product = self.product_input.currentText()
        sales = self.sales_input.value()

        if not month or not product:
            QMessageBox.warning(self, "Input Error", "Please select both month and product category.")
            return

        self.sales_data[(month, product)] = sales  # update if exists
        self.update_chart()

        self.product_input.setCurrentIndex(-1)
        self.month_input.setCurrentIndex(-1)
        self.sales_input.setValue(0)

    def clear(self):
        self.sales_data.clear()
        self.update_chart()

    def update_chart(self):
        self.graph.clear()
        # Re-add legend after clear
        self.graph.addLegend(offset=(10, 10))

        n_products = len(PRODUCTS)
        bar_width = 0.15
        group_width = bar_width * n_products

        for pi, product in enumerate(PRODUCTS):
            x_vals = []
            y_vals = []
            for mi, month in enumerate(MONTHS):
                key = (month, product)
                if key in self.sales_data:
                    x_vals.append(mi - group_width / 2 + pi * bar_width + bar_width / 2)
                    y_vals.append(self.sales_data[key])

            if x_vals:
                color = COLORS[product]
                bar = pg.BarGraphItem(
                    x=x_vals,
                    height=y_vals,
                    width=bar_width * 0.9,
                    brush=pg.mkBrush(*color, 200),
                    pen=pg.mkPen(*color),
                    name=product
                )
                self.graph.addItem(bar)
            else:
                # Add invisible item just to show in legend
                bar = pg.BarGraphItem(x=[], height=[], width=bar_width,
                                      brush=pg.mkBrush(*COLORS[product], 200),
                                      name=product)
                self.graph.addItem(bar)

        ax = self.graph.getAxis('bottom')
        ticks = [(i, m) for i, m in enumerate(MONTHS)]
        ax.setTicks([ticks])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())