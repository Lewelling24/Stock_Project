import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


def window():
    app = QApplication(sys.argv)

    new_window = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QPushButton("Top"))
    layout.addWidget(QPushButton("Bottom"))

    new_window.setLayout(layout)
    label = QLabel("Hello")
    layout.addWidget(label)
    new_window.show()

    app.exec()


window()
