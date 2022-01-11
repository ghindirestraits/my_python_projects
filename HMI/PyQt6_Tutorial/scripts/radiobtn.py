#! /usr/bin/env python

import sys
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGroupBox, QLabel, QHBoxLayout, QRadioButton

XPOS = 500
YPOS = 200
WIDTH = 500
HEIGHT = 400

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PyQt6 Radio Button")
        self.setWindowIcon(QIcon("HMI/PyQt6_Tutorial/resources/qt.png"))

        self.setGeometry(XPOS, YPOS, WIDTH, HEIGHT)

        self.radio_btn()

        vbox = QVBoxLayout()
        vbox.addWidget(self.grpbox)

        self.label = QLabel("Hello")
        self.label.setFont(QFont("Sans Serif", 14))
        vbox.addWidget(self.label)

        self.setLayout(vbox)
    
    def radio_btn(self):
        self.grpbox = QGroupBox("Choose Programming Language:")
        self.grpbox.setFont(QFont("Sans Serif", 15))

        hbox = QHBoxLayout()

        self.rad1 = QRadioButton("Python")
        self.rad1.setChecked(True)
        self.rad1.setFont(QFont("Sans Serif", 14))
        self.rad1.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad1)

        self.rad2 = QRadioButton("C++")
        self.rad2.setFont(QFont("Sans Serif", 14))
        self.rad2.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad2)

        self.rad3 = QRadioButton("Java")
        self.rad3.setFont(QFont("Sans Serif", 14))
        self.rad3.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad3)

        self.rad4 = QRadioButton("C#")
        self.rad4.setFont(QFont("Sans Serif", 14))
        self.rad4.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad4)

        self.grpbox.setLayout(hbox)
    
    def on_selected(self):
        radio = self.sender()
        
        if radio.isChecked():
            self.label.setText("You have selected: " + radio.text())

if __name__ == '__main__':
    app = QApplication([])
    win = Window()
    win.show()
    sys.exit(app.exec())
