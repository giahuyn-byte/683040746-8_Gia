import json
import pandas as pd
import pyqtgraph as pg
import numpy as np

from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

# ══════════════════════════════════════════════════════════════════════════
#  CONSTANTS - do not change
# ══════════════════════════════════════════════════════════════════════════

REQUIRED_COLS = {"date", "city", "temp_c", "humidity", "rainfall_mm", "condition"}
CONDITIONS    = ["Sunny", "Cloudy", "Rainy", "Stormy"]
CITIES        = ["Bangkok", "Chiang Mai", "Phuket"]


# ══════════════════════════════════════════════════════════════════════════
#  YOUR WORK — complete the 6 functions below
# ══════════════════════════════════════════════════════════════════════════

def read_csv(path: str) -> pd.DataFrame:
    """
    To do 1 — Read a CSV file and return a clean DataFrame.

    """

    df = pd.read_csv(path)

    if df.empty:
        raise ValueError("No CSV Fill")
    
    missing = REQUIRED_COLS - set(df.columns)

    if missing:
        raise ValueError(f"No Fill colum: {missing}")

    return df


def read_json(path: str) -> pd.DataFrame:
    """
    To do 2 — Read a JSON file and return a DataFrame.
    """
    df = pd.read_json(path)

    if df.empty:
        raise ValueError("No JSON Fill")

    missing = REQUIRED_COLS - set(df.columns)
    if missing:
        raise ValueError(f"No Fill colum: {missing}")
    
    return df


def write_csv(df: pd.DataFrame, path: str) -> None:
    """
    To do 3 — Save a DataFrame to a CSV file.
    """
    if df.empty:
        raise ValueError("No data")

    try:
        df.to_csv(path, index=False)
    except Exception as e:
        raise IOError(f"Cannot Save Fill: {e}")


def write_json(df: pd.DataFrame, path: str) -> None:
    """
    To do 4 — Save a DataFrame to a JSON file.
    """
    if df.empty:
        raise ValueError("No data")

    try:
        df.to_json(path, orient="records", indent=2, force_ascii=False)
    except Exception as e:
        raise IOError(f"Cannot Save Fill: {e}")
    

def build_stats(df: pd.DataFrame) -> QTableWidget:
    """
    To do 5 — Return a summary string shown in the Statistics panel.
    """
    if df.empty:
        raise ValueError("No data")

    missing = REQUIRED_COLS - set(df.columns)
    if missing:
        raise ValueError(f"No Fill colum: {missing}")
    
    # คำนวณสถิติแต่ละเมือง
    cities = df["city"].unique()
    rows = ["# Records", "avg_temp", "max_temp", "min_temp", "total_rain", "avg_humidity"]

    table = QTableWidget(len(rows), len(cities) + 1)  # +1 สำหรับคอลัมน์ชื่อ stat

    # ตั้งค่า header
    table.setHorizontalHeaderLabels(["city"] + list(cities))
    table.verticalHeader().setVisible(False)

    header_font = QFont()
    header_font.setBold(True)
    table.horizontalHeader().setFont(header_font)

    # ใส่ชื่อ stat ในคอลัมน์แรก
    for ri, row_name in enumerate(rows):
        item = QTableWidgetItem(row_name)
        item.setFont(header_font)
        item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        table.setItem(ri, 0, item)

    # ใส่ค่าสถิติแต่ละเมือง
    for ci, city in enumerate(cities):
        city_df = df[df["city"] == city]

        stats = [
            str(len(city_df)),                                   # # Records
            f"{city_df['temp_c'].mean():.1f}",                   # avg_temp
            f"{city_df['temp_c'].max():.1f}",                    # max_temp
            f"{city_df['temp_c'].min():.1f}",                    # min_temp
            f"{city_df['rainfall_mm'].sum():.1f}",               # total_rain
            f"{city_df['humidity'].mean():.1f}",                 # avg_humidity
        ]

        for ri, val in enumerate(stats):
            item = QTableWidgetItem(val)
            item.setTextAlignment(Qt.AlignCenter)
            table.setItem(ri, ci + 1, item)

    table.resizeColumnsToContents()
    return table



def show_chart(df: pd.DataFrame, chart_type: str) -> pg.PlotWidget:
    """
    To do 6 — Draw a Rainfall Histogram chart using pyqtgraph and return a PlotWidget.
    """
    if df.empty:
        raise ValueError("ไม่มีข้อมูลให้วาดกราฟ")

    if "rainfall_mm" not in df.columns:
        raise ValueError("ไม่พบคอลัมน์ rainfall_mm")

    # คำนวณ histogram
    rain_data = df["rainfall_mm"].dropna().values
    counts, bin_edges = np.histogram(rain_data, bins=10)

    # สร้าง PlotWidget
    plot = pg.PlotWidget()
    plot.setBackground("w")
    plot.setTitle("Rainfall Histogram", color="k", size="12pt")
    plot.setLabel("left",   "Frequency")
    plot.setLabel("bottom", "Rainfall (mm)")

    # วาด bar chart จาก histogram
    bar_item = pg.BarGraphItem(
        x=bin_edges[:-1],
        height=counts,
        width=(bin_edges[1] - bin_edges[0]) * 0.9,
        brush=pg.mkBrush(100, 149, 237, 200),   # cornflower blue
        pen=pg.mkPen("w", width=1),
    )
    plot.addItem(bar_item)

    return plot