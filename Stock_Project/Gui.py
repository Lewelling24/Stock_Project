import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


def window():
    app = QApplication(sys.argv)

    new_window = QWidget()
    new_button = QPushButton("Hello")
    new_button.show()
    new_window.show()

    app.exec()


window()
