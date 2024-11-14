from PyQt6.QtWidgets import *


class MakeOrderWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(1100, 100, 500, 300)
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle('Заказ')

        book_name_label = QLabel('Название книги:')
        self.book_name_input = QLineEdit()
        self.payment_method = QComboBox()
        payment_method_label = QLabel('Выберите способ оплаты:')
        self.payment_method.addItems(['-', 'Наличность', 'Дебетовая крата', 'Криптовалюта'])
        self.payment_method.currentIndexChanged.connect(self.cash_payment)

        self.cash_info_label = QLabel()
        self.make_order_btn = QPushButton('Сделать заказ')

        self.main_l = QVBoxLayout()
        self.main_l.addWidget(book_name_label)
        self.main_l.addWidget(self.book_name_input)
        self.main_l.addWidget(payment_method_label)
        self.main_l.addWidget(self.payment_method)
        self.main_l.addStretch()
        self.setLayout(self.main_l)

    def cash_payment(self, i):
        if i == 1:
            if self.cash_info_label.text() == 'Деньги возьмёт курьер':
                self.main_l.removeWidget(self.card_number_input)
                self.card_number_input.deleteLater()
                self.main_l.removeWidget(self.cvv_input)
                self.cvv_input.deleteLater()
                self.main_l.removeWidget(self.card_owner_input)
                self.card_owner_input.deleteLater()
                self.main_l.removeWidget(self.cash_info_label)
                self.main_l.removeWidget(self.make_order_btn)
                self.cash_info_label.setText('Деньги возьмёт курьер')
                self.main_l.addWidget(self.cash_info_label)
                self.main_l.addWidget(self.make_order_btn)
            else:
                self.cash_info_label.setText('Деньги возьмёт курьер')
                self.main_l.addWidget(self.cash_info_label)
                self.main_l.addWidget(self.make_order_btn)
        elif i == 2:
            if self.cash_info_label.text() == 'Деньги возьмёт курьер':
                self.main_l.removeWidget(self.cash_info_label)
                self.main_l.removeWidget(self.card_number_input)
                self.main_l.removeWidget(self.cvv_input)
                self.main_l.removeWidget(self.card_owner_input)
                self.main_l.removeWidget(self.make_order_btn)
                self.card_number_input = QLineEdit()
                self.cvv_input = QLineEdit()
                self.card_owner_input = QLineEdit()
                self.cash_info_label.setText('Введите данные карты')
                self.card_number_input.setPlaceholderText("Номер карты: 0000 0000 0000")
                self.cvv_input.setPlaceholderText('CVV карты: 000')
                self.card_owner_input.setPlaceholderText('Владелец карты: IVAN IVANOV')
                self.main_l.addWidget(self.cash_info_label)
                self.main_l.addWidget(self.card_number_input)
                self.main_l.addWidget(self.cvv_input)
                self.main_l.addWidget(self.card_owner_input)
                self.main_l.addWidget(self.make_order_btn)
            elif self.cash_info_label.text() == 'Введите данные карты':
                self.main_l.removeWidget(self.cash_info_label)
                self.main_l.removeWidget(self.card_number_input)
                self.main_l.removeWidget(self.cvv_input)
                self.main_l.removeWidget(self.card_owner_input)
                self.main_l.removeWidget(self.make_order_btn)
                self.card_number_input = QLineEdit()
                self.cvv_input = QLineEdit()
                self.card_owner_input = QLineEdit()
                self.cash_info_label.setText('Введите данные карты')
                self.card_number_input.setPlaceholderText("Номер карты: 0000 0000 0000")
                self.cvv_input.setPlaceholderText('CVV карты: 000')
                self.card_owner_input.setPlaceholderText('Владелец карты: IVAN IVANOV')
                self.main_l.addWidget(self.cash_info_label)
                self.main_l.addWidget(self.card_number_input)
                self.main_l.addWidget(self.cvv_input)
                self.main_l.addWidget(self.card_owner_input)
                self.main_l.addWidget(self.make_order_btn)
            else:
                self.card_number_input = QLineEdit()
                self.cvv_input = QLineEdit()
                self.card_owner_input = QLineEdit()
                self.cash_info_label.setText('Введите данные карты')
                self.card_number_input.setPlaceholderText("Номер карты: 0000 0000 0000")
                self.cvv_input.setPlaceholderText('CVV карты: 000')
                self.card_owner_input.setPlaceholderText('Владелец карты: IVAN IVANOV')
                self.main_l.addWidget(self.cash_info_label)
                self.main_l.addWidget(self.card_number_input)
                self.main_l.addWidget(self.cvv_input)
                self.main_l.addWidget(self.card_owner_input)
                self.main_l.addWidget(self.make_order_btn)
