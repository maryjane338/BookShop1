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
        self.cancel_btn.clicked.connect(self.delete_book)

        init_db()
        db = SessionLocal()

        self.order_service = OrderService(db)

        self.view = QTableView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
            ['ID Заказа', 'Книга', 'Адрес доставки', 'Статус оплаты', 'Дата доставки'])
        self.view.setModel(self.model)

        self.load_orders()

        main_l = QVBoxLayout()
        v_l = QHBoxLayout()
        main_l.addLayout(v_l)
        v_l.addWidget(self.cancel_btn)
        main_l.addWidget(self.view)
        self.setLayout(main_l)

    def load_orders(self):
        orders = self.order_service.load_orders_for_user(self.user)
        for order in orders:
            row = [QStandardItem(field) for field in order]
            self.model.appendRow(row)

    def delete_book(self):
        indexes = self.view.selectionModel().selectedRows()
        if indexes:
            row = indexes[0].row()
            dialog = QMessageBox()
            dialog.setGeometry(1200, 700, 500, 420)
            dialog.setWindowTitle("Подтверждение")
            dialog.setText(f"Вы уверены, что хотите отменить заказ?")
            dialog.setIcon(QMessageBox.Icon.Warning)
            dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            user_response = dialog.exec()
            if user_response == QMessageBox.StandardButton.Yes:
                self.order_service.delete_order(self.model.item(row, 0).text())
                QMessageBox.information(self, "Инфо", 'Заказ отменён')
                self.model.clear()
                self.model.setHorizontalHeaderLabels(
                    ['ID Заказа', 'Книга', 'Адрес доставки', 'Статус оплаты', 'Дата доставки'])
                self.load_orders()
        else:
            QMessageBox.information(self, 'Информация', 'Для удаления заказа, нажмите на его номер в таблице',
                                    QMessageBox.StandardButton.Ok)
