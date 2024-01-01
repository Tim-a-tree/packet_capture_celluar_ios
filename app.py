import sys
import os
import platform


from PyQt6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui_mainwindow import Ui_MainWindow

os.environ['QT_FONT_DPI'] = '96'

class MainWindow(QMainWindow):
    def __init__(self):
        # Initialize
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        title = 'iOS Packet Capture Tool'
        description = 'This tool is used to capture packets from iOS devices from Windows.'

        # Applying Window Title
        self.setWindowTitle(title)
        # widgets.titleRightInfo.setText(description)

        # Set Window Size
        QMainWindow.resize(self, 1280, 720)
        QMainWindow.setMinimumSize(self, 800, 600)

        # Set Font
        font = QFont()
        font.setFamily(u"Seoge UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    

    sys.exit(app.exec())

