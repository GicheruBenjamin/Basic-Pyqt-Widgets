import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QCheckBox, QRadioButton, QComboBox, QSpinBox, QSlider, QProgressBar, QTabWidget, QListWidget, QTableWidget, QTreeWidget, QDial, QMenuBar, QMenu, QAction, QToolBar, QStatusBar

app = QApplication(sys.argv)

widget = QWidget()
widget.setWindowTitle('Basic Widgets Demo')
widget.resize(800, 600)

label = QLabel('This is a label.', widget)
label.move(10, 10)

line_edit = QLineEdit('This is a line edit.', widget)
line_edit.move(10, 40)

text_edit = QTextEdit('This is a text edit.', widget)
text_edit.move(10, 80)

push_button = QPushButton('This is a push button.', widget)
push_button.move(10, 120)

check_box = QCheckBox('This is a check box.', widget)
check_box.move(10, 160)

radio_button = QRadioButton('This is a radio button.', widget)
radio_button.move(10, 200)

combo_box = QComboBox(widget)
combo_box.addItems(['Item 1', 'Item 2', 'Item 3'])
combo_box.move(10, 240)

spin_box = QSpinBox(widget)
spin_box.setValue(50)
spin_box.move(10, 280)

from PyQt6.QtWidgets import QSlider
from PyQt6.QtCore import Qt

slider = QSlider(Qt.Horizontal, widget)
slider.setValue(50)
slider.move(10, 320)

progress_bar = QProgressBar(widget)
progress_bar.setValue(50)
progress_bar.move(10, 360)

tab_widget = QTabWidget(widget)
tab_widget.addTab(QWidget(), 'Tab 1')
tab_widget.addTab(QWidget(), 'Tab 2')
tab_widget.move(10, 400)

list_widget = QListWidget(widget)
list_widget.addItems(['Item 1', 'Item 2', 'Item 3'])
list_widget.move(10, 440)

table_widget = QTableWidget(3, 3, widget)
table_widget.move(10, 480)

tree_widget = QTreeWidget(widget)
tree_widget.setHeaderLabels(['Column 1', 'Column 2'])
from PyQt5.QtWidgets import QTreeWidgetItem

tree_widget.addTopLevelItem(QTreeWidgetItem(['Item 1', 'Item 2']))
tree_widget.move(10, 520)

dial = QDial(widget)
dial.setValue(50)
dial.move(10, 560)

menu_bar = QMenuBar(widget)
file_menu = menu_bar.addMenu('File')
edit_menu = menu_bar.addMenu('Edit')
view_menu = menu_bar.addMenu('View')
menu_bar.move(10, 600)

action = QAction('Action', widget)
file_menu.addAction(action)

tool_bar = QToolBar(widget)
tool_bar.addAction(action)
tool_bar.move(10, 640)

status_bar = QStatusBar(widget)
status_bar.showMessage('This is a status bar.')
status_bar.move(10, 680)

widget.show()

sys.exit(app.exec())