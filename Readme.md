# Intro
Pyqt is a python framework for building GUI applications.In this repo. I share basic widgets in pyqt. Qt is a binding from c++ to python. Owned by the Qt Company.

### Important Python concepts to understand 
_**Classes and functions**_
_**Python code modules**_

# QWidget Class 
It gives you a base class for all widgets.
All widgets inherit from QWidget class.
## Properties 
1. Basic Properties:
setVisible(bool): Controls visibility (True to show, False to hide).
setEnabled(bool): Enables (True) or disables (False) user interaction.
setGeometry(int x, int y, int width, int height): Sets the position and size of the widget as a rectangle.
move(int x, int y): Moves the widget to a new top-left corner position.
resize(int width, int height): Changes the widget's size.
2. Appearance Properties:
setFont(QFont font): Sets the font used for text within the widget.
setToolTip(str tooltip): Sets the tooltip text displayed on hover.
setWhatsThis(str whatsThis): Sets the longer explanation displayed on Ctrl+hover.
setWindowOpacity(float opacity): Controls the transparency level (0.0 fully transparent, 1.0 fully opaque).
setStyleSheet(str stylesheet): Applies custom styles using Qt Style Sheets (QSS).
3. Layout Properties:
setLayout(QLayout layout): Sets the layout manager used by the widget (e.g., QVBoxLayout, QHBoxLayout, QGridLayout).
4. Accessibility Properties:
setAccessibleDescription(str description): Sets a text description for assistive technologies.
setAccessibleName(str name): Sets a name for the widget used by assistive technologies.
5. Focus Properties:
setFocusPolicy(Qt.FocusPolicy policy): Determines how the widget receives focus from the keyboard (e.g., Qt.ClickFocus, Qt.TabFocus).
Window System Integration Properties (for top-level widgets):
setWindowFlags(Qt.WindowFlags flags): Sets window-specific behavior (resizable, closable, modal, etc.).
setWindowTitle(str title): Sets the title displayed in the window's title bar.
### Note ::Additional Methods:
show(): Shows the widget on the screen.
hide(): Hides the widget.
close(): Closes the widget (if it's a top-level window).
update(): Requests the widget to repaint itself.

## QApplication class 
The QApplication class in PyQt is the foundation of your graphical user interface (GUI) application. It's the central hub that manages the application's lifecycle, event loop, and various system-wide settings. 

### Key properties of QApplication:
1. Application Initialization: It handles the initialization of your PyQt application, setting up the connection to the window system (e.g., Windows, macOS, Linux).
2. Event Loop: It provides the event loop that continuously listens for user interactions (mouse clicks, keyboard events, etc.) and dispatches those events to the appropriate widgets within your application. This ensures your application remains responsive and reacts to user actions.
3. Session Management: It manages the application session, which includes handling application-wide settings, resources, and the lifetime of your application windows.
4. Global Access: It provides access to some system-wide properties like the desktop palette, screen resolution, and font handling.

### Ways to style a widget.
## Using the Style Sheet(QSS)* :
QSS provides a powerful and flexible way to customize the appearance of your widgets using CSS-like syntax.
You can define styles for different widget types, states (hover, pressed), and even individual widgets with unique identifiers.
### Benefits:
Granular control over various aspects like fonts, colors, backgrounds, borders, margins, padding, etc.
Reusability: Create stylesheets that can be applied to multiple widgets across your application.
Readability: Style definitions are separate from your Python code, making it easier to maintain.

# Starting the application
1. Use sys.
2. Get the widgets u wanna use. 
3. Create an app.
4. Create a window(Mainwindow or Qwidget).
5. Show the window.
6. Start the event loop.


# Basic Widgets

1. QLabel: This widget is used to display text or images. It can be used to provide instructions, display messages, or show images.

2. QLineEdit: This widget is used to enter a single line of text. It can be used for entering usernames, passwords, or other short text inputs.

3. QTextEdit: This widget is used to enter multiple lines of text. It can be used for entering longer text inputs, such as comments or descriptions.

4. QPushButton: This widget is used to trigger an action when clicked. It can be used to submit forms, open dialogs, or perform other actions.

5. QCheckBox: This widget is used to select or deselect an option. It can be used to enable or disable features, or to select multiple options.

6. QRadioButton: This widget is used to select one option from a group of options. It can be used to select a single option from a set of mutually exclusive options.

7. QComboBox: This widget is used to select an option from a drop-down list. It can be used to select a single option from a list of options.

8. QSpinBox: This widget is used to select a number within a range. It can be used to select a quantity, a date, or a time.

9. QSlider: This widget is used to select a value within a range by sliding a handle. It can be used to adjust volume, brightness, or other continuous values.

10. QProgressBar: This widget is used to display the progress of an operation. It can be used to show the progress of a download, an upload, or a calculation.

11. QTabWidget: This widget is used to display multiple pages of content in a tabbed interface. It can be used to organize content into categories or sections.

12. QListWidget: This widget is used to display a list of items that can be selected. It can be used to display a list of files, a list of contacts, or a list of options.

13. QTableWidget: This widget is used to display a table of items that can be selected. It can be used to display a table of data, a spreadsheet, or a grid of options.

14. QTreeWidget: This widget is used to display a tree of items that can be expanded and collapsed. It can be used to display a file system, a hierarchy of options, or a list of categories and subcategories.

15. QDial: This widget is used to select a value within a range by rotating a dial. It can be used to adjust volume, brightness, or other continuous values.

16. QMenuBar: This widget is used to display a menu bar at the top of a window. It can be used to organize actions into categories, such as File, Edit, and View.

17. QMenu: This widget is used to display a menu of actions. It can be used to display a list of options, such as Open, Save, and Quit.

18. QAction: This widget is used to represent an action that can be triggered by the user. It can be used to perform an action, such as opening a file or saving a document.

19. QToolBar: This widget is used to display a toolbar of buttons and other widgets. It can be used to provide quick access to frequently used actions.

20. QStatusBar: This widget is used to display a status bar at the bottom of a window. It can be used to display messages, such as the progress of an operation or the status of a connection.