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

        self.block_btn = QPushButton('Заблокировать')
        self.block_btn.clicked.connect(self.block_user)

        init_db()
        db = SessionLocal()

        order_service = ClientService(db)
        clients = order_service.get_all_clients()

        self.view = QTableView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['id_order', 'user_name', 'Книга', 'Номер тел.'])
        self.view.setModel(self.model)

        for client in clients:
            row = [QStandardItem(field) for field in client]
            self.model.appendRow(row)

        main_l = QVBoxLayout()
        v_l = QHBoxLayout()
        main_l.addLayout(v_l)
        v_l.addWidget(self.block_btn)
        main_l.addWidget(self.view)
        self.setLayout(main_l)

    def block_user(self):
        QMessageBox.warning(self, 'Подтверждение', 'Вы уверены, что хотите заблокировать пользователя?',
                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
