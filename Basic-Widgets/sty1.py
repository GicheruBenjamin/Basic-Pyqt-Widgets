import sys
from PyQt6.QtWidgets import QApplication, QWidget

app =   QApplication([])  # Create the application instance
window = QWidget()
window.setStyleSheet("background-color: red;") # Setting bg as red.
window.show()
sys.exit(app.exec())  # Start the event loop and exit when done