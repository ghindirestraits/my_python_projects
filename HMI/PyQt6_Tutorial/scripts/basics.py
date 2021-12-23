#! /usr/bin/env python

import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget

XPOS = 500
YPOS = 200
WIDTH = 500
HEIGHT = 400

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PyQt6 Basics")
        self.setWindowIcon(QIcon("HMI/PyQt6_Tutorial/resources/qt.png"))
        # self.setFixedHeight(200)
        # self.setFixedWidth(200)

        self.setGeometry(XPOS, YPOS, WIDTH, HEIGHT)

        self.setStyleSheet('background-color:red')
        stylesheet = (
            'background-color:red'
        )
        self.setStyleSheet(stylesheet)

if __name__ == '__main__':
    app = QApplication([])
    win = Window()
    win.show()
    sys.exit(app.exec())
