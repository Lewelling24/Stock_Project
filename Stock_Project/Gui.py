import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


def window():
    app = QApplication(sys.argv)

    new_window = QPushButton("Hello")
    new_window.show()

    app.exec()


window()
