from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import *


class AdminOrderWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Заказы')
        self.setGeometry(50, 300, 750, 400)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        self.update_btn = QPushButton('Изменить')
        self.delete_btn = QPushButton('Удалить')

        orders = [
            ['1', 'elenaLOVE', 'Преступление и наказание', '+7 914 285 01 02', 'ул. Мухина 145, кв. 11', 'Карта', '30.11.2024'],
            ['2', 'Jeka_2004', 'Идиот', '+7 963 444 44 03', 'ул. Ленина 22, кв. 57', 'Карта', '02.12.2024'],
            ['3', 'volchara28rus', 'Вий', '+7 996 129 27 10', 'ул. Зейская 241, кв. 137', 'Наличные', '05.11.2024']
        ]

        view = QTableView()
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['id_order', 'user_name', 'Книга', 'Номер тел.', 'Адрес доставки', 'Способ оплаты', 'Дата доставки'])
        view.setModel(model)

        for order in orders:
            row = [QStandardItem(field) for field in order]
            model.appendRow(row)

        main_l = QVBoxLayout()
        v_l = QHBoxLayout()
        main_l.addLayout(v_l)
        v_l.addWidget(self.update_btn)
        v_l.addWidget(self.delete_btn)
        main_l.addWidget(view)
        self.setLayout(main_l)
