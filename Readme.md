## Intro
Pyqt is a python framework for building GUI applications.In this repo. I share basic widgets in pyqt. Qt is a binding from c++ to python. Owned by the Qt Company.

## Important Python concepts to understand 
Classes and functions
Python code modules

## QWidget Class 
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
## Note ::Additional Methods:
show(): Shows the widget on the screen.
hide(): Hides the widget.
close(): Closes the widget (if it's a top-level window).
update(): Requests the widget to repaint itself.

## QApplication class 
The QApplication class in PyQt is the foundation of your graphical user interface (GUI) application. It's the central hub that manages the application's lifecycle, event loop, and various system-wide settings. 

## Key properties of QApplication:
1. Application Initialization: It handles the initialization of your PyQt application, setting up the connection to the window system (e.g., Windows, macOS, Linux).
2. Event Loop: It provides the event loop that continuously listens for user interactions (mouse clicks, keyboard events, etc.) and dispatches those events to the appropriate widgets within your application. This ensures your application remains responsive and reacts to user actions.
3. Session Management: It manages the application session, which includes handling application-wide settings, resources, and the lifetime of your application windows.
4. Global Access: It provides access to some system-wide properties like the desktop palette, screen resolution, and font handling.