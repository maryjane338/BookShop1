from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *

from database import init_db, SessionLocal
from services.book_service import AdminService
from windows.admin.adminWin import AdminWin


class AuthorizationWin(QWidget):
    def __init__(self, enter_win):
        super().__init__()
        self.enter_win = enter_win
        self.initUI()

    def initUI(self):
        self.resize(400, 200)
        self.setWindowTitle('Авторизация')
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        login = QLabel('Введите логин:(Вова)')
        self.login_line = QLineEdit()
        password = QLabel('Введите пароль:(123)')
        self.password_line = QLineEdit()
        self.enter_btn = QPushButton('Войти')
        self.enter_btn.clicked.connect(self.enter)

        self.back_btn = QPushButton('Назад')
        self.back_btn.clicked.connect(self.back)

        main_l = QVBoxLayout()
        main_l.addWidget(login)
        main_l.addWidget(self.login_line)
        main_l.addWidget(password)
        main_l.addWidget(self.password_line)
        main_l.addWidget(self.enter_btn)
        main_l.addStretch()
        main_l.addWidget(self.back_btn)
        self.setLayout(main_l)

    def enter(self):
        init_db()
        db = SessionLocal()

        admin_service = AdminService(db)
        admin_password = admin_service.select_admin_for_enter(self.login_line.text())
        if self.password_line.text() == admin_password:
            self.admin_win = AdminWin(self.enter_win)
            self.admin_win.show()
            self.close()
        else:
            QMessageBox.information(self, 'Инфо', 'Администратора с таким логином или паролем не существует!\n'
                                                  'Попробуйте ещё раз.')

    def back(self):
        self.close()
        self.enter_win.show()
