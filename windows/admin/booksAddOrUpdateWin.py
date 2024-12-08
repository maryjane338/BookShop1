from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *

from database import SessionLocal
from services.book_service import BookService


class BooksAddOrUpdateWin(QWidget):
    def __init__(self, bookswin, book=None):
        super().__init__()
        self.bookswin = bookswin
        self.book = book
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
        picture_label = QLabel('Название картинки (picture.jpg):')
        self.picture_input = QLineEdit()
        price_label = QLabel('Введите цену (руб.):')
        self.price_input = QLineEdit()
        self.save_btn = QPushButton('Сохранить')
        self.id = QLineEdit()
        self.save_btn.clicked.connect(self.save_book)

        if self.book:
            self.author_name_input.setText(self.book['author'])
            self.book_input.setText(self.book['book_name'])

            path = list(self.book['book_picture'])
            del path[0:14]
            path_string = (''.join(path))

            self.picture_input.setText(path_string)
            self.price_input.setText(self.book['price'])
            self.id.setText(self.book['id'])

        main_l = QVBoxLayout()
        main_l.addWidget(author_name_label)
        main_l.addWidget(self.author_name_input)
        main_l.addWidget(book_label)
        main_l.addWidget(self.book_input)
        main_l.addWidget(picture_label)
        main_l.addWidget(self.picture_input)
        main_l.addWidget(price_label)
        main_l.addWidget(self.price_input)
        main_l.addStretch()
        main_l.addWidget(self.save_btn)
        self.setLayout(main_l)

    def save_book(self):
        db = SessionLocal()
        book_service = BookService(db)

        try:
            int(self.price_input.text())

            if self.author_name_input.text() == '' or self.book_input.text() == '' or self.picture_input.text() == ''\
                    or self.price_input.text() == '':
                QMessageBox.information(self, 'Информация',
                                        'Вы не заполнили все поля или заполнили их некорректно.')
            else:
                if self.id.text():
                    book_service.update_book(
                        id_book=self.id.text(),
                        author=self.author_name_input.text(),
                        book_name=self.book_input.text(),
                        book_picture=f'book_pictures/{self.picture_input.text()}',
                        price=int(self.price_input.text())
                    )
                else:
                    book_service.add_book(
                        author=self.author_name_input.text(),
                        book_name=self.book_input.text(),
                        book_picture=f'book_pictures/{self.picture_input.text()}',
                        price=int(self.price_input.text())
                    )
                QMessageBox.information(self, 'Информация', 'Книга успешно сохранена!')
                self.close()
                self.bookswin.model.clear()
                self.bookswin.model.setHorizontalHeaderLabels(['id', 'Автор', 'Название', 'Картинка', 'Цена'])
                self.bookswin.load_books()

        except ValueError:
            QMessageBox.information(self, 'Информация',
                                    'Вы не заполнили все поля или заполнили их некорректно.')
