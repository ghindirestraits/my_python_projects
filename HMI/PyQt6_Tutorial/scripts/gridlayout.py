#! /usr/bin/env python

import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

XPOS = 500
YPOS = 200
WIDTH = 500
HEIGHT = 400

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PyQt6 GridLayout")
        self.setWindowIcon(QIcon("HMI/PyQt6_Tutorial/resources/qt.png"))

        self.setGeometry(XPOS, YPOS, WIDTH, HEIGHT)

        grid = QGridLayout()
        btn1 = QPushButton("Button One")
        btn2 = QPushButton("Button Two")
        btn3 = QPushButton("Button Three")
        btn4 = QPushButton("Button Four")
        btn5 = QPushButton("Button Five")
        btn6 = QPushButton("Button Six")
        btn7 = QPushButton("Button Seven")
        btn8 = QPushButton("Button Eight")

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 0, 2)
        grid.addWidget(btn4, 0, 3)
        grid.addWidget(btn5, 1, 0)
        grid.addWidget(btn6, 1, 1)
        grid.addWidget(btn7, 1, 2)
        grid.addWidget(btn8, 1, 3)

        self.setLayout(grid)

if __name__ == '__main__':
    app = QApplication([])
    win = Window()
    win.show()
    sys.exit(app.exec())
