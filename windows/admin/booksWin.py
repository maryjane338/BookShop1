from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import *


class BooksWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Книги')
        self.setGeometry(1150, 300, 400, 400)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        self.update_btn = QPushButton('Изменить')
        self.delete_btn = QPushButton('Удалить')
        self.add_btn = QPushButton('Добавить')

        books = [
            ['Дж. Д. Сэллинджер', 'Над пропастью во ржи', '800 руб.'],
            ['Дж. Оруэл', '1984', '1000 руб.'],
            ['Ф. Достоевский', 'Преступление и наказание', '1500 руб.'],
            ['Э. М. Ремарк', 'Три товарища', '400 руб.'],
            ['М. Твен', 'Приключения Гекльберри Финна', '1200 руб.'],
            ['Н. Гоголь', 'Мёртвые Души', '500 руб.'],
            ['', '', '.']
        ]

        view = QTableView()
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Автор', 'Название', 'Цена'])
        view.setModel(model)

        for book in books:
            row = [QStandardItem(field) for field in book]
            model.appendRow(row)

        main_l = QVBoxLayout()
        v_l = QHBoxLayout()
        main_l.addLayout(v_l)
        v_l.addWidget(self.update_btn)
        v_l.addWidget(self.delete_btn)
        v_l.addWidget(self.add_btn)
        main_l.addWidget(view)
        self.setLayout(main_l)
