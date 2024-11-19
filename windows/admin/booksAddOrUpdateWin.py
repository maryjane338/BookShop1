from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *


class BooksAddOrUpdateWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Заказ')
        self.setGeometry(1550, 100, 300, 300)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        author_name_label = QLabel('Введите автора:')
        self.author_name_input = QLineEdit()
        book_label = QLabel('Введите название книги:')
        self.book_input = QLineEdit()
        price_label = QLabel('Введите цену (руб.):')
        self.price_input = QLineEdit()
        self.save_btn = QPushButton('Сохранить')
        self.save_btn.clicked.connect(self.save_book)

        main_l = QVBoxLayout()
        main_l.addWidget(author_name_label)
        main_l.addWidget(self.author_name_input)
        main_l.addWidget(book_label)
        main_l.addWidget(self.book_input)
        main_l.addWidget(price_label)
        main_l.addWidget(self.price_input)
        main_l.addStretch()
        main_l.addWidget(self.save_btn)
        self.setLayout(main_l)

    def save_book(self):
        QMessageBox.information(self, 'Информация', 'Книга успешно сохранена!')
        self.close()
