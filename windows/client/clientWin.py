from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import *
from windows.client.assortmentWin import AssortmentWin
from windows.client.clientOrdersWin import ClientOrdersWin
from windows.client.makeOrderWin import MakeOrderWin


class ClientWin(QWidget):
    def __init__(self, enter_win, user):
        super().__init__()
        self.enter_win = enter_win
        self.user = user
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Магазин книг')
        self.resize(250, 300)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        self.pixmap = QPixmap()
        self.pixmap.load('logo_pictures/mainLogo.png')
        scaled_pixmap = self.pixmap.scaled(230, 100)
        self.label = QLabel()
        self.label.setPixmap(scaled_pixmap)

        self.assortment_win_btn = QPushButton('Книги в наличии')
        self.assortment_win_btn.clicked.connect(self.show_assortment_win)

        self.make_order_btn = QPushButton('Сделать заказ')
        self.make_order_btn.clicked.connect(self.show_make_order_win)

        self.my_orders_btn = QPushButton('Мои заказы')
        self.my_orders_btn.clicked.connect(self.show_check_login_win)

        self.back_enter_btn = QPushButton('Вернуться ко входу')
        self.back_enter_btn.clicked.connect(self.back_to_enter)

        self.win1 = 0
        self.win2 = 0
        self.win3 = 0

        self.main_l = QVBoxLayout()
        self.main_l.addWidget(self.label)
        self.main_l.addWidget(self.assortment_win_btn)
        self.main_l.addWidget(self.make_order_btn)
        self.main_l.addWidget(self.my_orders_btn)
        self.main_l.addStretch()
        self.main_l.addWidget(self.back_enter_btn)
        self.setLayout(self.main_l)

    def show_assortment_win(self):
        self.assortment = AssortmentWin()
        self.assortment.show()
        self.win1 = 1

    def show_make_order_win(self):
        self.make_order_win = MakeOrderWin(self.user)
        self.make_order_win.show()
        self.win2 = 1

    def show_check_login_win(self):
        self.orders_win = ClientOrdersWin(self.user)
        self.orders_win.show()
        self.win3 = 1

    def back_to_enter(self):
        if self.win1 == 1 and self.win2 == 1 and self.win3 == 1:
            self.assortment.close()
            self.make_order_win.close()
            self.orders_win.close()
            self.hide()
        elif self.win1 == 0 and self.win2 == 0 and self.win3 == 0:
            self.hide()
        elif self.win1 == 1 and self.win2 == 1:
            self.assortment.close()
            self.make_order_win.close()
            self.hide()
        elif self.win2 == 1 and self.win3 == 1:
            self.make_order_win.close()
            self.orders_win.close()
            self.hide()
        elif self.win3 == 1 and self.win1 == 1:
            self.orders_win.close()
            self.assortment.close()
            self.hide()
        self.enter_win.show()

    def closeEvent(self, event):
        QApplication.quit()
