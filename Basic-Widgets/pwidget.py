
import sys
from PyQt6.QtWidgets import QApplication, QWidget


app = QApplication([])  # Create the application instance

window = QWidget()  # Create a simple widget as the main window
window.setWindowTitle("Hello World")  # Set the window title
window.show()  # Make the window visible

sys.exit(app.exec())  # Start the event loop and exit when done


