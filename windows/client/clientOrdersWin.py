from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import *


class ClientOrdersWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(1100, 550, 500, 420)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))
        self.setWindowTitle('Заказы')

        self.cancel_btn = QPushButton('Отменить заказ')
        self.cancel_btn.clicked.connect(self.cancel_order)

        orders = [
            ['2', 'Идиот', 'ул. Ленина 22, кв. 57', 'Карта', '02.12.2024']
        ]

        view = QTableView()
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(
            ['Заказ №', 'Книга', 'Адрес доставки', 'Способ оплаты', 'Дата доставки'])
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

    def cancel_order(self):
        QMessageBox.warning(self, 'Подтверждение', 'Вы уверены, что хотите отменить заказ?',
                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

