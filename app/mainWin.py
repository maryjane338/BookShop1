from PyQt6.QtWidgets import *
from app.book import AssortmentWin
from app.makeOrderWin import MakeOrderWin


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Книжный магазин')
        self.resize(200, 200)
        self.setFixedSize(self.width(), self.height())

        self.assortment_win_btn = QPushButton('Книги в наличии')
        self.assortment_win_btn.clicked.connect(self.show_assortment_win)

        self.make_order_btn = QPushButton('Сделать заказ')
        self.make_order_btn.clicked.connect(self.show_make_order_win)

        self.main_l = QVBoxLayout()
        self.main_l.addStretch()
        self.main_l.addWidget(self.assortment_win_btn)
        self.main_l.addWidget(self.make_order_btn)
        self.main_l.addStretch()
        self.setLayout(self.main_l)

    def show_assortment_win(self):
        self.assortment = AssortmentWin()
        self.assortment.show()

    def show_make_order_win(self):
        self.make_order_win = MakeOrderWin()
        self.make_order_win.show()

    def closeEvent(self, event):
        QApplication.quit()
