import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


def window():
    app = QApplication(sys.argv)

    new_window = QWidget()
    layout = QVBoxLayout()
    label = QLabel("Get last close price")
    layout.addWidget(label)
    layout.addWidget((QPushButton("Get price")))
    new_window.setLayout(layout)
    new_window.show()

    app.exec()


window()
