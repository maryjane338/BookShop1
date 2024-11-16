from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *


class ClientOrdersWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))
        self.setWindowTitle('Заказы')
