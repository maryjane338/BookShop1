from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
from database import SessionLocal, init_db
from services.book_service import ClientService


class UsersWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Книги')
        self.setGeometry(1150, 600, 400, 400)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('logo_pictures/window_icon.png'))

        self.block_btn = QPushButton('Удалить пользователя')
        self.block_btn.clicked.connect(self.delete_user)

        init_db()
        db = SessionLocal()

        self.client_service = ClientService(db)

        self.view = QTableView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['id_order', 'user_name', 'Книга', 'Номер тел.'])
        self.view.setModel(self.model)

        self.load_users()

        main_l = QVBoxLayout()
        v_l = QHBoxLayout()
        main_l.addLayout(v_l)
        v_l.addWidget(self.block_btn)
        main_l.addWidget(self.view)
        self.setLayout(main_l)

    def load_users(self):
        clients = self.client_service.get_all_clients()
        for client in clients:
            row = [QStandardItem(field) for field in client]
            self.model.appendRow(row)

    def delete_user(self):
        indexes = self.view.selectionModel().selectedRows()
        if indexes:
            row = indexes[0].row()
            dialog = QMessageBox()
            dialog.setGeometry(1200, 775, 400, 400)
            dialog.setWindowTitle("Подтверждение")
            dialog.setText(f"Вы уверены, что хотите удалить пользователя?")
            dialog.setIcon(QMessageBox.Icon.Warning)
            dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            user_response = dialog.exec()
            if user_response == QMessageBox.StandardButton.Yes:
                self.client_service.delete_client(self.model.item(row, 0).text())
                QMessageBox.information(self, "Инфо", 'Запись удалена')
                self.model.clear()
                self.model.setHorizontalHeaderLabels(['id', 'Автор', 'Название', 'Картинка', 'Цена'])
                self.load_users()
        else:
            QMessageBox.information(self, 'Информация',
                                    'Для удаления пользователя, нажмите на его номер в таблице',
                                    QMessageBox.StandardButton.Ok)

