from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *


class UpdateOrderWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Заказ')
        self.resize(300, 430)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        user_name_label = QLabel('Введите имя пльзователя:')
        self.user_name_input = QLineEdit()
        book_label = QLabel('Введите название книги:')
        self.book_input = QLineEdit()
        phone_label = QLabel('Введите номер телефона:')
        self.phone_input = QLineEdit()
        address_label = QLabel('Введите адрес:')
        self.address_input = QLineEdit()
        payment_label = QLabel('Укажите способ оплаты:')
        self.payment_choice = QComboBox()
        self.payment_choice.addItems(['Наличные', 'Дебетовая карта', 'Криптовалюта'])
        date_label = QLabel('Введите дату')
        self.date_input = QLineEdit()
        self.update_btn = QPushButton('Сохранить изменения')
        self.update_btn.clicked.connect(self.save_order)

        main_l = QVBoxLayout()
        main_l.addWidget(user_name_label)
        main_l.addWidget(self.user_name_input)
        main_l.addWidget(book_label)
        main_l.addWidget(self.book_input)
        main_l.addWidget(phone_label)
        main_l.addWidget(self.phone_input)
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
        QMessageBox.information(self, 'Информация', 'Заказ успешно изменён!')
        self.close()
