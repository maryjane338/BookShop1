from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *


class AdminWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Магазин книг')
        self.resize(200, 200)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        self.main_l = QVBoxLayout()
        self.main_l.addStretch()
        self.main_l.addStretch()
        self.setLayout(self.main_l)

    def closeEvent(self, event):
        QApplication.quit()
