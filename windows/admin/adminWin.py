from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
from windows.admin.adminOrderWin import AdminOrderWin
from windows.admin.booksWin import BooksWin


class AdminWin(QWidget):
    def __init__(self, enter_win):
        super().__init__()
        self.enter_win = enter_win
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Окно Администратора')
        self.resize(300, 200)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        self.all_orders_btn = QPushButton('Заказы')
        self.all_orders_btn.clicked.connect(self.show_all_orders_win)

        self.books_btn = QPushButton('Книги')
        self.books_btn.clicked.connect(self.show_books_win)

        self.back_enter_btn = QPushButton('Вернуться ко входу')
        self.back_enter_btn.clicked.connect(self.back_to_enter)

        self.main_l = QVBoxLayout()
        self.main_l.addStretch()
        self.main_l.addWidget(self.all_orders_btn)
        self.main_l.addWidget(self.books_btn)
        self.main_l.addStretch()
        self.main_l.addWidget(self.back_enter_btn)
        self.setLayout(self.main_l)

        self.win1 = 0
        self.win2 = 0

    def show_books_win(self):
        self.books_win = BooksWin()
        self.books_win.show()
        self.win1 = 1

    def show_all_orders_win(self):
        self.adm_orders_win = AdminOrderWin()
        self.adm_orders_win.show()
        self.win2 = 1

    def back_to_enter(self):
        if self.win1 == 1 and self.win2 == 1:
            self.books_win.close()
            self.adm_orders_win.close()
            self.hide()
        elif self.win1 == 0 and self.win2 == 0:
            self.hide()
        elif self.win1 == 1:
            self.books_win.close()
            self.hide()
        elif self.win2 == 1:
            self.adm_orders_win.close()
            self.hide()
        self.enter_win.show()

    def closeEvent(self, event):
        QApplication.quit()
