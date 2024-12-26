from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QStatusBar
from PyQt6.QtCore import QCoreApplication, QMetaObject, Qt, QTimer, QPointF
from PyQt6.QtGui import QPainter, QColor
import sys
import random


class SnowflakeTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.snowflakes = []
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_snowflakes)
        self.timer.start(20)  # Обновление каждые 50 мс
        self.generate_snowflakes(120)

    def generate_snowflakes(self, count):
        """Генерирует снежинки с случайными начальными позициями"""
        for _ in range(count):
            x = random.randint(0, self.width())
            y = random.randint(0, self.height())
            size = random.randint(2, 5)
            speed = random.uniform(0.5, 2.0)
            self.snowflakes.append({'x': x, 'y': y, 'size': size, 'speed': speed})

    def update_snowflakes(self):
        """Обновляет позиции снежинок"""
        for snowflake in self.snowflakes:
            snowflake['y'] += snowflake['speed']
            # Если снежинка выходит за пределы, она появляется заново сверху
            if snowflake['y'] > self.height():
                snowflake['y'] = 0
                snowflake['x'] = random.randint(0, self.width())
                snowflake['size'] = random.randint(2, 5)
                snowflake['speed'] = random.uniform(0.5, 2.0)
        self.viewport().update()  # Обновляем область виджета

    def paintEvent(self, event):
        super().paintEvent(event)  # Рисуем стандартное содержимое QTextEdit
        painter = QPainter(self.viewport())
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Рисуем снежинки
        for snowflake in self.snowflakes:
            painter.setBrush(QColor(255, 255, 255))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(QPointF(snowflake['x'], snowflake['y']), snowflake['size'], snowflake['size'])


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName('CatCheck')
        MainWindow.resize(624, 462)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName('verticalLayout')
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName('label')
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QTextEdit(self.centralwidget)  # Используем кастомное поле
        self.textEdit.setObjectName('textEdit')
        self.textEdit.setMaximumHeight(40)
        self.verticalLayout.addWidget(self.textEdit)
        self.outputEdit = SnowflakeTextEdit(self.centralwidget)  # Используем кастомное поле
        self.outputEdit.setObjectName('outputEdit')
        self.outputEdit.setReadOnly(False)
        self.verticalLayout.addWidget(self.outputEdit)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName('pushButton')
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName('pushButton_4')
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName('pushButton_3')
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName('pushButton_2')
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName('pushButton_5')
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName('pushButton_6')
        self.verticalLayout.addWidget(self.pushButton_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName('statusbar')
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('CatCheck', 'CatCheck'))
        self.label.setText(_translate('CatCheck', 'Поле ввода URL сайта'))
        self.pushButton.setText(_translate('CatCheck', 'Проверить URL'))
        self.pushButton_4.setText(_translate('CatCheck', 'Экспорт базы данных'))
        self.pushButton_3.setText(_translate('CatCheck', 'Импорт базы данных'))
        self.pushButton_2.setText(_translate('CatCheck', 'Вывести базу данных'))
        self.pushButton_5.setText(_translate('CatCheck', 'Сформировать отчет'))
        self.pushButton_6.setText(_translate('CatCheck', 'Информация о фишинге'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
