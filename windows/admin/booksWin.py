from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import *

from database import SessionLocal, init_db
from services.book_service import BookService
from windows.admin.booksAddOrUpdateWin import BooksAddOrUpdateWin


class BooksWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Книги')
        self.setGeometry(1150, 100, 400, 400)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        self.update_btn = QPushButton('Изменить')
        self.update_btn.clicked.connect(self.show_booksaddorupdate_win)
        self.delete_btn = QPushButton('Удалить')
        self.delete_btn.clicked.connect(self.delete_book)
        self.add_btn = QPushButton('Добавить')
        self.add_btn.clicked.connect(self.show_booksaddorupdate_win)

        init_db()
        db = SessionLocal()

        books_service = BookService(db)
        books = books_service.get_all_books()

        self.view = QTableView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['id', 'Автор', 'Название', 'Картинка', 'Цена'])
        self.view.setModel(self.model)

        self.view.selectionModel().selectionChanged.connect(self.on_selection_changed)

        for book in books:
            row = [QStandardItem(field) for field in book]
            self.model.appendRow(row)

        main_l = QVBoxLayout()
        v_l = QHBoxLayout()
        main_l.addLayout(v_l)
        v_l.addWidget(self.update_btn)
        v_l.addWidget(self.delete_btn)
        v_l.addWidget(self.add_btn)
        main_l.addWidget(self.view)
        self.setLayout(main_l)

    def show_booksaddorupdate_win(self):
        self.booksaddorupdate_win = BooksAddOrUpdateWin()
        self.booksaddorupdate_win.show()

    def on_selection_changed(self):
        indexes = self.view.selectionModel().selectedRows()
        for index in indexes:
            row = index.row()
            row_data = []
            for column in range(self.model.columnCount()):
                cell_value = self.model.item(row, column).text()
                row_data.append(cell_value)
                print('fksl')
                print(row)
                print(row_data)
    def delete_book(self):
        QMessageBox.warning(self, 'Подтверждение', 'Вы уверены, что хотите удалить запись?',
                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
