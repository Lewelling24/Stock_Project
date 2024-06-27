import sys

from PyQt5.QtWidgets import QApplication, QWidget


def window():
    app = QApplication(sys.argv)

    new_window = QWidget()
    new_window.show()

    app.exec()


window()
