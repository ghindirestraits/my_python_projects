#! /usr/bin/env python

import sys
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox

XPOS = 500
YPOS = 200
WIDTH = 500
HEIGHT = 400

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("PyQt6 Checkbox")
        self.setWindowIcon(QIcon("HMI/PyQt6_Tutorial/resources/qt.png"))

        self.setGeometry(XPOS, YPOS, WIDTH, HEIGHT)

        self.create_checkbox()
    
    def create_checkbox(self):
        hbox = QHBoxLayout()

        self.check1 = QCheckBox("Python")
        self.check1.setFont(QFont("Sans Serif", 14))
        self.check1.toggled.connect(self.item_selected)
        hbox.addWidget(self.check1)

        self.check2 = QCheckBox("Java")
        self.check2.setFont(QFont("Sans Serif", 14))
        self.check2.toggled.connect(self.item_selected)
        hbox.addWidget(self.check2)

        self.check3 = QCheckBox("C++")
        self.check3.setFont(QFont("Sans Serif", 14))
        self.check3.toggled.connect(self.item_selected)
        hbox.addWidget(self.check3)

        self.check4 = QCheckBox("C#")
        self.check4.setFont(QFont("Sans Serif", 14))
        self.check4.toggled.connect(self.item_selected)
        hbox.addWidget(self.check4)

        vbox = QVBoxLayout()

        self.label = QLabel("Label")
        self.label.setFont(QFont("Sans Serif", 15))
        self.label.setStyleSheet('color:red')

        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
    
    def item_selected(self):
        value = ""

        if self.check1.isChecked():
            value = self.check1.text()
        elif self.check2.isChecked():
            value = self.check2.text()
        elif self.check3.isChecked():
            value = self.check3.text()
        elif self.check4.isChecked():
            value = self.check4.text()
        else:
            value = ""
        
        self.label.setText("You have selected: " + value)

if __name__ == '__main__':
    app = QApplication([])
    win = Window()
    win.show()
    sys.exit(app.exec())
