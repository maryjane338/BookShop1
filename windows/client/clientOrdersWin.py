from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import *
from database import SessionLocal, init_db
from services.book_service import OrderService


class ClientOrdersWin(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.initUI()

    def initUI(self):
        self.setGeometry(1100, 550, 500, 420)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))
        self.setWindowTitle('Заказы')

        self.cancel_btn = QPushButton('Отменить заказ')

        init_db()
        db = SessionLocal()

        order_service = OrderService(db)

        orders = order_service.load_orders_for_user(self.user)

        view = QTableView()
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(
            ['Заказ №', 'Книга', 'Адрес доставки', 'Статус оплаты', 'Дата доставки'])
        view.setModel(model)

        for order in orders:
            row = [QStandardItem(field) for field in order]
            model.appendRow(row)

        main_l = QVBoxLayout()
        v_l = QHBoxLayout()
        main_l.addLayout(v_l)
        v_l.addWidget(self.cancel_btn)
        main_l.addWidget(view)
        self.setLayout(main_l)
