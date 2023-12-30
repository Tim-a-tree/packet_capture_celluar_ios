import sys
import os
import platform


from PyQt6.QtWidgets import QApplication, QMainWindow

os.environ['QT_FONT_DPI'] = '96'

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        title = 'iOS Packet Capture Tool'
        description = 'This tool is used to capture packets from iOS devices from Windows.'

        # Applying Window Title
        self.setWindowTitle(title)
        # widgets.titleRightInfo.setText(description)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    

    sys.exit(app.exec())

