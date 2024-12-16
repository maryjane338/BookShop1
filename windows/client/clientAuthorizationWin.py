from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
from database import init_db, SessionLocal
from services.book_service import ClientService
from windows.client.clientWin import ClientWin


class ClientAuthorizationWin(QWidget):
    def __init__(self, enter_win):
        super().__init__()
        self.enter_win = enter_win
        self.initUI()

    def initUI(self):
        self.resize(400, 200)
        self.setWindowTitle('Вход')
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        login_label = QLabel('Введите ваш логин: (Jeka_2004)')
        self.login_input = QLineEdit()
        password_label = QLabel('Введите пароль: (321)')
        self.password_input = QLineEdit()
        self.continue_btn = QPushButton('Продолжить')
        self.continue_btn.clicked.connect(self.show_orders)
        self.back_btn = QPushButton('Назад')
        self.back_btn.clicked.connect(self.back)

        main_l = QVBoxLayout()
        main_l.addWidget(login_label)
        main_l.addWidget(self.login_input)
        main_l.addWidget(password_label)
        main_l.addWidget(self.password_input)
        main_l.addWidget(self.continue_btn)
        main_l.addStretch()
        main_l.addWidget(self.back_btn)
        self.setLayout(main_l)

    def show_orders(self):
        init_db()
        db = SessionLocal()

        client_service = ClientService(db)
        user_password = client_service.select_user_for_enter(self.login_input.text())
        if self.password_input.text() == user_password:
            user = client_service.select_user(self.login_input.text())
            self.client_win = ClientWin(self.enter_win, user)
            self.client_win.show()
            self.close()
        else:
            QMessageBox.information(self, 'Ой-ой', 'Неверный логин или пароль!\nПопробуйте ещё раз.')

    def back(self):
        self.close()
        self.enter_win.show()
