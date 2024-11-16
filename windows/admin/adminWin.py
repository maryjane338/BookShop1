from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
from windows.admin.adminOrderWin import AdminOrderWin


class AdminWin(QWidget):
    def __init__(self, enter_win):
        super().__init__()
        self.enter_win = enter_win
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Магазин книг')
        self.resize(200, 200)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        self.all_orders_btn = QPushButton('Заказы')
        self.all_orders_btn.clicked.connect(self.show_all_orders_win)

        self.back_enter_btn = QPushButton('Вернуться ко входу')
        self.back_enter_btn.clicked.connect(self.back_to_enter)

        self.main_l = QVBoxLayout()
        self.main_l.addStretch()
        self.main_l.addWidget(self.all_orders_btn)
        self.main_l.addWidget(self.back_enter_btn)
        self.main_l.addStretch()
        self.setLayout(self.main_l)

    def show_all_orders_win(self):
        self.adm_orders_win = AdminOrderWin()
        self.adm_orders_win.show()

    def back_to_enter(self):
        self.hide()
        self.enter_win.show()

    def closeEvent(self, event):
        QApplication.quit()
