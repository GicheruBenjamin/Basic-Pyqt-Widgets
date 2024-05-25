
import sys
from PyQt6.QtWidgets import QApplication , QWidget 

 # Create a stylesheet string
stylesheet = """
QWidget {
    background-color: lightblue;
    border: 5px solid gray;
    font-family: Arial, sans-serif;
}
"""

# Create a widget and apply the stylesheet
app = QApplication([])  # Create the application instance
widget = QWidget()
widget.setStyleSheet(stylesheet)
widget.show()
sys.exit(app.exec())  # Start the event loop and exit when done\