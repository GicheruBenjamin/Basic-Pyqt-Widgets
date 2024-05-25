import sys
from PyQt6.QtWidgets import QWidget, QApplication

app = QApplication([])
win = QWidget()
win.setObjectName("MyWindow")
win.setWindowTitle("My First App")
win.show()
with open("style.qss", "r") as f:
    app.setStyleSheet(f.read())
sys.exit(app.exec())