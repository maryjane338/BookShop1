from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
from windows.enterWin import EnterWin
from windows.ClientWin import ClientWin
from windows.AdminWin import AdminWin


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 50, 500, 100)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))
        self.setWindowTitle('Магазин книг')

        self.client_enter_btn = QPushButton('Войти как клиент')
        self.client_enter_btn.clicked.connect(self.show_client_win)

        self.admin_enter_btn = QPushButton('Войти как администратор')
        self.admin_enter_btn.clicked.connect(self.show_admin_win)

        self.main_l = QVBoxLayout()
        self.main_l.addStretch()
        self.main_l.addWidget(self.client_enter_btn)
        self.main_l.addWidget(self.admin_enter_btn)
        self.main_l.addStretch()
        self.setLayout(self.main_l)

    def show_client_win(self):
        self.client_win = ClientWin()
        self.client_win.show()
        self.close()

    def show_admin_win(self):
        self.enter_win = EnterWin()
        self.enter_win.show()
        self.close()
