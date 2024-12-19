# Файл с дизайном приложения, написано с помощью qt-designer
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QStatusBar
from PyQt6.QtCore import QCoreApplication, QMetaObject

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName('Ivan_gey')
        MainWindow.resize(624, 462)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName('verticalLayout')
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName('label')
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName('textEdit')
        self.textEdit.setMaximumHeight(40)
        self.verticalLayout.addWidget(self.textEdit)
        self.outputEdit = QTextEdit(self.centralwidget)
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
        self.pushButton_5.setText(_translate('CatCheck', 'СФормировать отчет'))
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())