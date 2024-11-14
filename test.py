from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Создаем layout и добавляем несколько кнопок
        self.layout = QVBoxLayout(self)

        # Пример виджетов, которые мы будем удалять
        self.button1 = QPushButton("Кнопка 1")
        self.button2 = QPushButton("Кнопка 2")
        self.button3 = QPushButton("Кнопка 3")

        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)

        # Кнопка для удаления всех виджетов из layout
        self.clear_button = QPushButton("Удалить все виджеты")
        self.clear_button.clicked.connect(self.clear_layout)
        self.layout.addWidget(self.clear_button)

    def clear_layout(self):
        # Удаляем все виджеты из layout
        self.layout.removeWidget(self.button1)
        self.button1.deleteLater()


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
