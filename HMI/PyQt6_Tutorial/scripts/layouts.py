#! /usr/bin/env python

import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

XPOS = 500
YPOS = 200
WIDTH = 500
HEIGHT = 400

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PyQt6 Layouts")
        self.setWindowIcon(QIcon("HMI/PyQt6_Tutorial/resources/qt.png"))

        self.setGeometry(XPOS, YPOS, WIDTH, HEIGHT)

        vbox = QVBoxLayout()
        btn1 = QPushButton("Button One")
        btn2 = QPushButton("Button Two")
        btn3 = QPushButton("Button Three")
        btn4 = QPushButton("Button Four")

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication([])
    win = Window()
    win.show()
    sys.exit(app.exec())
