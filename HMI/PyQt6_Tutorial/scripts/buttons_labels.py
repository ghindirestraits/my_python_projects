#! /usr/bin/env python

import sys
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel

XPOS = 500
YPOS = 200
WIDTH = 500
HEIGHT = 400

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PyQt6 Buttons & Labels")
        self.setWindowIcon(QIcon("HMI/PyQt6_Tutorial/resources/qt.png"))

        self.setGeometry(XPOS, YPOS, WIDTH, HEIGHT)

        self.create_button()
        self.create_label()
    
    def create_button(self):
        btn = QPushButton("Click Me", self)
        # btn.move(100, 100)
        btn.setGeometry(100, 100, 100, 100)
        btn.setStyleSheet('background-color:red')
        btn.setIcon(QIcon('HMI/science.png'))

    def create_label(self):
        self.lbl = QLabel("My Label", self)
        # self.lbl.move(100, 200)
        self.lbl.setGeometry(100, 220, 200, 100)
        self.lbl.setStyleSheet('color:green')
        self.lbl.setFont(QFont("Times New Roman", 15))

if __name__ == '__main__':
    app = QApplication([])
    win = Window()
    win.show()
    sys.exit(app.exec())
