from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem


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

        books = [
            ['elenaLOVE', '+7 914 285 01 02'],
            ['Jeka_2004', '+7 963 444 44 03'],
            ['volchara28rus', '+7 996 129 27 10'],
        ]

        view = QTableView()
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['user_name', 'phone_nmber'])
        view.setModel(model)

        for book in books:
            row = [QStandardItem(field) for field in book]
            model.appendRow(row)

        main_l = QVBoxLayout()
        v_l = QHBoxLayout()
        main_l.addLayout(v_l)
        v_l.addWidget(self.block_btn)
        main_l.addWidget(view)
        self.setLayout(main_l)

    def block_user(self):
        QMessageBox.warning(self, 'Подтверждение', 'Вы уверены, что хотите заблокировать пользователя?',
                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
