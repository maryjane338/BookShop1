from PyQt6.QtWidgets import QApplication
from app.mainWin import MainWin
import sys


def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
