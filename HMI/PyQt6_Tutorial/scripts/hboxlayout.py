#! /usr/bin/env python

import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

XPOS = 500
YPOS = 200
WIDTH = 500
HEIGHT = 400

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PyQt6 HBoxLayout")
        self.setWindowIcon(QIcon("HMI/PyQt6_Tutorial/resources/qt.png"))

        self.setGeometry(XPOS, YPOS, WIDTH, HEIGHT)

        hbox = QHBoxLayout()
        btn1 = QPushButton("Button One")
        btn2 = QPushButton("Button Two")
        btn3 = QPushButton("Button Three")
        btn4 = QPushButton("Button Four")

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)

        self.setLayout(hbox)

if __name__ == '__main__':
    app = QApplication([])
    win = Window()
    win.show()
    sys.exit(app.exec())
