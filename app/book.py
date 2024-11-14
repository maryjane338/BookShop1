from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *


class AssortmentWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 500, 900)
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle('Книжный магазин')

        self.label1 = QLabel()
        self.label2 = QLabel()
        self.label3 = QLabel()
        self.label4 = QLabel()
        self.label5 = QLabel()
        self.label6 = QLabel()

        self.name_label1 = QLabel('Над пропастью во ржи\nДэвид. Сэллинджер\n800 руб.')
        self.name_label2 = QLabel('1984\nДжордж. Оруэл\n1000 руб.')
        self.name_label3 = QLabel('Преступление и наказание\nФёдор Достоевский\n1500 руб.')
        self.name_label4 = QLabel('Три товарища\nЭрих Мария Ремарк\n400 руб.')
        self.name_label5 = QLabel('Приключения Гекльберри Фина\nМарк Твен\n1200 руб.')
        self.name_label6 = QLabel('Мёртвые Души\nНиколай Гоголь\n500 руб.')

        self.pixmap = QPixmap()

        self.page_btn1 = QPushButton('1')
        self.page_btn1.setFixedSize(25, 25)
        self.page_btn1.clicked.connect(self.button_click1)
        self.page_btn2 = QPushButton('2')
        self.page_btn2.setFixedSize(25, 25)
        self.page_btn2.clicked.connect(self.button_click2)
        self.page_btn3 = QPushButton('3')
        self.page_btn3.setFixedSize(25, 25)
        self.page_btn3.clicked.connect(self.button_click3)
        self.page_btn4 = QPushButton('4')
        self.page_btn4.setFixedSize(25, 25)
        self.page_btn4.clicked.connect(self.button_click4)
        self.page_btn5 = QPushButton('5')
        self.page_btn5.setFixedSize(25, 25)
        self.page_btn5.clicked.connect(self.button_click5)
        self.page_btn6 = QPushButton('6')
        self.page_btn6.setFixedSize(25, 25)
        self.page_btn6.clicked.connect(self.button_click6)

        self.page_label = QLabel('Текущяя страница: 1')

        self.button_click1()

        main_l = QVBoxLayout()
        h_l1 = QHBoxLayout()
        hl1_name = QHBoxLayout()
        h_l2 = QHBoxLayout()
        hl2_name = QHBoxLayout()
        h_l3 = QHBoxLayout()
        hl3_name = QHBoxLayout()
        hl_pages = QHBoxLayout()
        hl_page_label = QHBoxLayout()
        h_l1.addWidget(self.label1)
        h_l1.addWidget(self.label2)
        hl1_name.addWidget(self.name_label1)
        hl1_name.addWidget(self.name_label2)
        h_l2.addWidget(self.label3)
        h_l2.addWidget(self.label4)
        hl2_name.addWidget(self.name_label3)
        hl2_name.addWidget(self.name_label4)
        h_l3.addWidget(self.label5)
        h_l3.addWidget(self.label6)
        hl3_name.addWidget(self.name_label5)
        hl3_name.addWidget(self.name_label6)
        hl_pages.addWidget(self.page_btn1)
        hl_pages.addWidget(self.page_btn2)
        hl_pages.addWidget(self.page_btn3)
        hl_pages.addWidget(self.page_btn4)
        hl_pages.addWidget(self.page_btn5)
        hl_pages.addWidget(self.page_btn6)
        hl_page_label.addWidget(self.page_label)
        main_l.addLayout(h_l1)
        main_l.addLayout(hl1_name)
        main_l.addLayout(h_l2)
        main_l.addLayout(hl2_name)
        main_l.addLayout(h_l3)
        main_l.addLayout(hl3_name)
        main_l.addStretch()
        main_l.addLayout(hl_pages)
        main_l.addLayout(hl_page_label)
        self.setLayout(main_l)

    def button_click1(self):
        self.name_label1.setText('Над пропастью во ржи\nДэвид. Сэллинджер\n800 руб.')
        self.name_label2.setText('1984\nДжордж. Оруэл\n1000 руб.')
        self.name_label3.setText('Преступление и наказание\nФёдор Достоевский\n1500 руб.')
        self.name_label4.setText('Три товарища\nЭрих Мария Ремарк\n400 руб.')
        self.name_label5.setText('Приключения Гекльберри Фина\nМарк Твен\n1200 руб.')
        self.name_label6.setText('Мёртвые Души\nНиколай Гоголь\n500 руб.')

        self.pixmap.load("book.jpg")
        self.scaled_pixmap = self.pixmap.scaled(150, 200)

        self.label1.setPixmap(self.scaled_pixmap)
        self.label2.setPixmap(self.scaled_pixmap)
        self.label3.setPixmap(self.scaled_pixmap)
        self.label4.setPixmap(self.scaled_pixmap)
        self.label5.setPixmap(self.scaled_pixmap)
        self.label6.setPixmap(self.scaled_pixmap)

        self.page_btn1.setStyleSheet('QPushButton {background-color: #A3C1DA}')
        self.page_btn2.setStyleSheet('QPushButton {background-color: #00000}')
        self.page_btn3.setStyleSheet('QPushButton {background-color: #00000}')
        self.page_btn4.setStyleSheet('QPushButton {background-color: #00000}')
        self.page_btn5.setStyleSheet('QPushButton {background-color: #00000}')
        self.page_btn6.setStyleSheet('QPushButton {background-color: #00000}')

        self.page_label.setText('Текущая страница: 1')

    def button_click2(self):
        self.name_label1.setText('Кортик\nДэвид. Сэллинджер\n500 руб.')
        self.name_label2.setText('Чёрный Обелиск\nДжордж. Оруэл\n800 руб.')
        self.name_label3.setText('Идиот\nФёдор Достоевский\n1200 руб.')
        self.name_label4.setText('На западном фронте без перемен\nЭрих Мария Ремарк\n900 руб.')
        self.name_label5.setText('Приключения Тома Соера\nМарк Твен\n350 руб.')
        self.name_label6.setText('Вий\nНиколай Гоголь\n700 руб.')

        self.pixmap.load('book.jpg')
        self.scaled_pixmap = self.pixmap.scaled(150, 200)

        self.label1.setPixmap(self.scaled_pixmap)
        self.label2.setPixmap(self.scaled_pixmap)
        self.label3.setPixmap(self.scaled_pixmap)
        self.label4.setPixmap(self.scaled_pixmap)
        self.label5.setPixmap(self.scaled_pixmap)
        self.label6.setPixmap(self.scaled_pixmap)

        self.page_btn1.setStyleSheet('QPushButton {background-color: #00000}')
        self.page_btn2.setStyleSheet('QPushButton {background-color: #A3C1DA}')
        self.page_btn3.setStyleSheet('QPushButton {background-color: #00000}')
        self.page_btn4.setStyleSheet('QPushButton {background-color: #00000}')
        self.page_btn5.setStyleSheet('QPushButton {background-color: #00000}')
        self.page_btn6.setStyleSheet('QPushButton {background-color: #00000}')

        self.page_label.setText('Текущая страница: 2')

    def button_click3(self):
        self.page_label.setText('Текущая страница: 3')

    def button_click4(self):
        self.page_label.setText('Текущая страница: 4')

    def button_click5(self):
        self.page_label.setText('Текущая страница: 5')

    def button_click6(self):
        self.page_label.setText('Текущая страница: 6')


def main():
    app = QApplication([])
    win = AssortmentWin()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()
