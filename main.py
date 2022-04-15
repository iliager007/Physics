from PyQt6.QtCore import QTimer, pyqtSignal, QSize, QTime
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QMainWindow, QInputDialog, \
    QFileDialog
from PyQt6.QtWidgets import QLCDNumber, QLineEdit, QMessageBox, QCheckBox, QHBoxLayout, QVBoxLayout, QRadioButton
from PyQt6.QtGui import QIcon, QPalette, QBrush, QImage
import sys
import random


class Interface(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.vbox = QVBoxLayout()

        self.hbox = QHBoxLayout()
        self.label = QLabel("Введите кол-во формул:")
        self.lineEdit = QLineEdit()
        self.hbox.addWidget(self.label)
        self.hbox.addWidget(self.lineEdit)

        self.labelThemes = QLabel("Темы:")
        self.checkBoxes = []
        self.checkBoxes.append(QCheckBox("Все"))

        self.btn = QPushButton("Создать вариант")
        self.btn.clicked.connect(self.solve)

        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.labelThemes)
        for checkBox in self.checkBoxes:
            checkBox.setChecked(True)
            self.vbox.addWidget(checkBox)
        self.vbox.addWidget(self.btn)
        self.setLayout(self.vbox)

    def solve(self):
        item = self.vbox.takeAt(0)
        layout = item.layout()
        item = layout.takeAt(0)
        widget = item.widget()
        widget.deleteLater()
        item = layout.takeAt(0)
        widget = item.widget()
        widget.deleteLater()
        while self.vbox.count() > 0:
            item = self.vbox.takeAt(0)
            widget = item.widget()
            widget.deleteLater()
        self.number = 1
        self.formula = QLabel("Формула 1")
        self.vbox.addWidget(self.formula)
        self.count = 5
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.timerLabel = QLabel(str(self.count))
        self.vbox.addWidget(self.timerLabel)

    def next(self):
        self.number += 1
        self.formula.setText("Формула " + str(self.number))
        self.count = 5
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.timerLabel.setText(str(self.count))

    def showTime(self):
        self.count -= 1
        self.timerLabel.setText(str(self.count))
        if self.count == 0:
            self.next()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Interface()
    ex.show()
    sys.exit(app.exec())
