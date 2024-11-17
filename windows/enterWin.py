from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
from windows.admin.authorizationWin import AuthorizationWin
from windows.client.clientAuthorizationWin import ClientAuthorizationWin


class EnterWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 100)
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
        self.client_authorization_win = ClientAuthorizationWin(self)
        self.client_authorization_win.show()
        self.hide()

    def show_admin_win(self):
        self.enter_win = AuthorizationWin(self)
        self.enter_win.show()
        self.hide()

    def closeEvent(self, event):
        QApplication.quit()
