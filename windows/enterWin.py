from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
from windows.AdminWin import AdminWin


class EnterWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 700, 500, 150)
        self.setWindowTitle('Вход')
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        login = QLabel('Введите логин:')
        self.login_line = QLineEdit()
        password = QLabel('Введите пароль:')
        self.password_line = QLineEdit()
        self.enter_btn = QPushButton('Войти')
        self.enter_btn.clicked.connect(self.enter)


        main_l = QVBoxLayout()
        main_l.addWidget(login)
        main_l.addWidget(self.login_line)
        main_l.addWidget(password)
        main_l.addWidget(self.password_line)
        main_l.addWidget(self.enter_btn)
        self.setLayout(main_l)

    def enter(self):
        self.login = self.login_line.text()
        self.password = self.password_line.text()
        if self.login == 'Вова' and self.password == '123':
            self.admin_win = AdminWin()
            self.admin_win.show()
            self.close()
        else:
            QMessageBox.information(self, 'Инфо', 'Логин или пароль неверны, попробуйте ещё раз.')
