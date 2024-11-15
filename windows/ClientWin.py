from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import *
from windows.assortmentWin import AssortmentWin
from windows.makeOrderWin import MakeOrderWin


class ClientWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Магазин книг')
        self.resize(250, 200)
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

        self.main_l = QVBoxLayout()
        self.main_l.addWidget(self.label)
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
