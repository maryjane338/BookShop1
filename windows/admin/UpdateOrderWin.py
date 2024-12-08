from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
from database import SessionLocal
from services.book_service import OrderService


class UpdateOrderWin(QWidget):
    def __init__(self, order_win, order=None):
        super().__init__()
        self.order_win = order_win
        self.order = order
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Заказ')
        self.resize(300, 430)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        book_label = QLabel('Введите название книги:')
        self.book_input = QLineEdit()
        address_label = QLabel('Введите адрес:')
        self.address_input = QLineEdit()
        payment_label = QLabel('Статус оплаты:')
        self.payment_choice = QComboBox()
        self.payment_choice_line = QLineEdit()
        self.payment_choice.addItems(['Оплачен', 'Не оплачен'])
        date_label = QLabel('Введите дату:')
        self.date_input = QLineEdit()
        self.id = QLineEdit()
        self.update_btn = QPushButton('Сохранить изменения')
        self.update_btn.clicked.connect(self.save_order)

        if self.order:
            self.book_input.setText(self.order['book_name'])
            self.address_input.setText(self.order['address'])
            self.payment_choice_line.setText(self.order['payment'])

            self.payment_choice.setCurrentIndex(int(self.payment_choice_line.text()) - 1)
            self.date_input.setText(self.order['delivery_date'])
            self.id.setText(self.order['id_order'])


        main_l = QVBoxLayout()
        main_l.addWidget(book_label)
        main_l.addWidget(self.book_input)
        main_l.addWidget(address_label)
        main_l.addWidget(self.address_input)
        main_l.addWidget(payment_label)
        main_l.addWidget(self.payment_choice)
        main_l.addWidget(date_label)
        main_l.addWidget(self.date_input)
        main_l.addStretch()
        main_l.addWidget(self.update_btn)
        self.setLayout(main_l)

    def save_order(self):
        db = SessionLocal()
        order_service = OrderService(db)

        try:
            int(self.book_input.text())

            if self.book_input.text() == '' or self.address_input.text() == '' or self.date_input.text() == '':
                QMessageBox.information(self, 'Информация',
                                        'Вы не заполнили все поля или заполнили их некорректно.')
            else:
                order_service.update_order(
                    id_order=self.id.text(),
                    book_name=self.book_input.text(),
                    address=self.address_input.text(),
                    payment=(self.payment_choice.currentIndex() + 1),
                    delivery_date=self.date_input.text()
                )
            QMessageBox.information(self, 'Информация', 'Заказ успешно изменён!')
            self.close()
            self.order_win.model.clear()
            self.order_win.model.setHorizontalHeaderLabels(['id_order', 'user_name', 'Книга', 'Адрес доставки', 'Способ оплаты',
                                                  'Дата доставки'])
            self.order_win.load_orders()

        except ValueError:
            QMessageBox.information(self, 'Информация',
                                    'Вы не заполнили все поля или заполнили их некорректно.')
