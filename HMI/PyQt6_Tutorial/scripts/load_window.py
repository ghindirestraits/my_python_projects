import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget

class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("HMI/PyQt6_Tutorial/resources/Window.ui", self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec())
