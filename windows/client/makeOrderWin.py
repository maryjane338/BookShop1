from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
from database import SessionLocal, init_db
from services.book_service import OrderService, BookService
from datetime import date


class MakeOrderWin(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.initUI()

    def initUI(self):
        self.setGeometry(1100, 200, 500, 320)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))
        self.setWindowTitle('Заказ')

        book_name_label = QLabel('Название книги:')
        self.book_name_input = QLineEdit()
        user_address_label = QLabel('Адрес доставки:')
        self.user_address = QLineEdit()
        self.payment_method = QComboBox()
        payment_method_label = QLabel('Выберите способ оплаты:')
        self.payment_method.addItems(['-', 'Наличные', 'Дебетовая крата', 'Криптовалюта'])
        self.payment_method.currentIndexChanged.connect(self.payment)

        self.cash_info_label = QLabel()
        self.make_order_btn = QPushButton('Создать заказ')
        self.make_order_btn.clicked.connect(self.make_order)
        self.card_number_input = QLineEdit()
        self.cvv_input = QLineEdit()
        self.card_owner_input = QLineEdit()
        self.crypto_wallet_id = QLineEdit()

        self.main_l = QVBoxLayout()
        self.main_l.addWidget(book_name_label)
        self.main_l.addWidget(self.book_name_input)
        self.main_l.addWidget(user_address_label)
        self.main_l.addWidget(self.user_address)
        self.main_l.addWidget(payment_method_label)
        self.main_l.addWidget(self.payment_method)
        self.main_l.addStretch()
        self.setLayout(self.main_l)

    def payment(self, i):
        self.i = i
        if i == 1:
            if self.cash_info_label.text() == 'Введите данные карты':
                self.main_l.removeWidget(self.card_number_input)
                self.card_number_input.setVisible(False)
                self.main_l.removeWidget(self.cvv_input)
                self.cvv_input.setVisible(False)
                self.main_l.removeWidget(self.card_owner_input)
                self.card_owner_input.setVisible(False)
                self.cash_info_label.setText('Оплата будет произведена через курьера')
            elif self.cash_info_label.text() == 'Введите реквизиты вашего кошелька':
                self.main_l.removeWidget(self.crypto_wallet_id)
                self.crypto_wallet_id.setVisible(False)
                self.cash_info_label.setText('Оплата будет произведена через курьера')
            else:
                self.cash_info_label.setText('Оплата будет произведена через курьера')
                self.main_l.addWidget(self.cash_info_label)
                self.main_l.addWidget(self.make_order_btn)
        elif i == 2:
            if self.cash_info_label.text() == 'Оплата будет произведена через курьера':
                self.card_number_input.setVisible(True)
                self.cvv_input.setVisible(True)
                self.card_owner_input.setVisible(True)
                self.cash_info_label.setText('Введите данные карты')
                self.card_number_input.setPlaceholderText("Номер карты: 0000 0000 0000")
                self.cvv_input.setPlaceholderText('CVV карты: 000')
                self.card_owner_input.setPlaceholderText('Владелец карты: IVAN IVANOV')
                self.main_l.addWidget(self.card_number_input)
                self.main_l.addWidget(self.cvv_input)
                self.main_l.addWidget(self.card_owner_input)
                self.main_l.addWidget(self.make_order_btn)
            elif self.cash_info_label.text() == 'Введите реквизиты вашего кошелька':
                self.main_l.removeWidget(self.crypto_wallet_id)
                self.crypto_wallet_id.setVisible(False)
                self.card_number_input.setVisible(True)
                self.cvv_input.setVisible(True)
                self.card_owner_input.setVisible(True)
                self.cash_info_label.setText('Введите данные карты')
                self.card_number_input.setPlaceholderText("Номер карты: 0000 0000 0000")
                self.cvv_input.setPlaceholderText('CVV карты: 000')
                self.card_owner_input.setPlaceholderText('Владелец карты: IVAN IVANOV')
                self.main_l.addWidget(self.card_number_input)
                self.main_l.addWidget(self.cvv_input)
                self.main_l.addWidget(self.card_owner_input)
                self.main_l.addWidget(self.make_order_btn)
            else:
                self.cash_info_label.setText('Введите данные карты')
                self.card_number_input.setPlaceholderText("Номер карты: 0000 0000 0000")
                self.cvv_input.setPlaceholderText('CVV карты: 000')
                self.card_owner_input.setPlaceholderText('Владелец карты: IVAN IVANOV')
                self.main_l.addWidget(self.cash_info_label)
                self.main_l.addWidget(self.card_number_input)
                self.main_l.addWidget(self.cvv_input)
                self.main_l.addWidget(self.card_owner_input)
                self.main_l.addWidget(self.make_order_btn)
        elif i == 3:
            if self.cash_info_label.text() == 'Оплата будет произведена через курьера':
                self.crypto_wallet_id.setVisible(True)
                self.cash_info_label.setText('Введите реквизиты вашего кошелька')
                self.crypto_wallet_id.setPlaceholderText("ID: 00000000")
                self.main_l.addWidget(self.crypto_wallet_id)
                self.main_l.addWidget(self.make_order_btn)
            elif self.cash_info_label.text() == 'Введите данные карты':
                self.main_l.removeWidget(self.card_number_input)
                self.card_number_input.setVisible(False)
                self.main_l.removeWidget(self.cvv_input)
                self.cvv_input.setVisible(False)
                self.main_l.removeWidget(self.card_owner_input)
                self.card_owner_input.setVisible(False)
                self.crypto_wallet_id.setVisible(True)
                self.cash_info_label.setText('Введите реквизиты вашего кошелька')
                self.crypto_wallet_id.setPlaceholderText("ID кошелька: 00000000")
                self.main_l.addWidget(self.cash_info_label)
                self.main_l.addWidget(self.crypto_wallet_id)
                self.main_l.addWidget(self.make_order_btn)
            else:
                self.cash_info_label.setText('Введите реквизиты вашего кошелька')
                self.crypto_wallet_id.setPlaceholderText("ID: 00000000")
                self.main_l.addWidget(self.cash_info_label)
                self.main_l.addWidget(self.crypto_wallet_id)
                self.main_l.addWidget(self.make_order_btn)

    def make_order(self):
        init_db()
        db = SessionLocal()

        order_service = OrderService(db)
        book_service = BookService(db)

        book = book_service.select_book_query(self.book_name_input.text())

        if self.book_name_input.text() == '' or self.user_address.text() == '':
            QMessageBox.information(self, 'Заказ', 'Вы не заполнили все поля.')
        elif book is None:
            QMessageBox.information(self, 'Заказ', 'Такой книги нет в нашем магазине.')
        else:
            if self.i == 1:
                payment = 2
                book_id = book_service.select_book_query(self.book_name_input.text())
                order_service.add_order(client_name=self.user, book_name=book_id, address=self.user_address.text(),
                                        payment=payment, delivery_date=str(date.today()))
                QMessageBox.information(self, 'Заказ', 'Ваш заказ успешно создан!')
                self.close()
            elif self.i == 2:
                if self.card_number_input.text() == '' or self.cvv_input.text() == ''\
                        or self.card_owner_input.text() == '':
                    QMessageBox.information(self, 'Заказ', 'Указаны не все данные карты.')
                else:
                    payment = 1
                    book_id = book_service.select_book_query(self.book_name_input.text())
                    order_service.add_order(client_name=self.user, book_name=book_id,
                                            address=self.user_address.text(),payment=payment,
                                            delivery_date=str(date.today()))
                    QMessageBox.information(self, 'Заказ', 'Ваш заказ успешно создан!')
                    self.close()
            elif self.i == 3:
                if self.crypto_wallet_id.text() == '':
                    QMessageBox.information(self, 'Заказ', 'Укажите реквизиты вашего кошелька.')
                else:
                    payment = 1
                    book_id = book_service.select_book_query(self.book_name_input.text())
                    order_service.add_order(client_name=self.user, book_name=book_id,
                                            address=self.user_address.text(),payment=payment,
                                            delivery_date=str(date.today()))
                    QMessageBox.information(self, 'Заказ', 'Ваш заказ успешно создан!')
                    self.close()
