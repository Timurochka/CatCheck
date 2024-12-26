import sys
from PyQt6.QtWidgets import QApplication, QMainWindow,QMessageBox
from design import Ui_MainWindow
from database import init_db, get_links, export_links, import_links
from checker import check_url_ssl, check_url_whois, parse_whois_info
from reports import save_results_pdf
from google_save_browsing_api import check_url_safety as google_api
from datetime import datetime


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Подключаем кнопки к обработчикам
        self.ui.pushButton.clicked.connect(self.check_url)
        self.ui.pushButton_2.clicked.connect(self.show_database)
        self.ui.pushButton_3.clicked.connect(self.import_database)
        self.ui.pushButton_4.clicked.connect(self.export_database)
        self.ui.pushButton_5.clicked.connect(self.generate_report)
        self.ui.pushButton_6.clicked.connect(self.create_info)
    def check_url(self):
        """Проверка URL с выводом результатов в UI."""
        try:
            # Получение текущей даты и времени
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Добавление даты проверки в начало
            self.ui.outputEdit.append(f'<font color="gray"><i>Дата проверки: {current_date}</i></font>')

            url = self.ui.textEdit.toPlainText()
            is_ssl = check_url_ssl(url)
            whois_info = check_url_whois(url)
            status = "Безопасен" if is_ssl else "Подозрительный"
            google_response = google_api(url)

            # Google Safe Browsing
            google_color = "green" if "безопасно" in google_response.lower() else "red"
            self.ui.outputEdit.append(
                f'<font color="{google_color}">Результат Google Safe Browsing: {google_response}</font>'
            )

            # SSL статус
            ssl_color = "green" if is_ssl else "red"
            self.ui.outputEdit.append(
                f'<font color="{ssl_color}">Результат проверки SSL: {status}</font>'
            )

            # WHOIS информация
            self.ui.outputEdit.append('<font color="blue">WHOIS информация:</font>')
            for key, value in whois_info.items():
                self.ui.outputEdit.append(f"<b>{key}</b>: {value}")

        except Exception as e:
            self.ui.outputEdit.append(f"<font color='red'>Ошибка:</font> {str(e)}")

    def show_database(self):
        """Выводит все записи в бд"""
        links = get_links()
        for link in links:
            self.ui.outputEdit.append(' '.join(map(str, link)))

    def import_database(self):
        """Импортирует записи в бд из файла"""
        if import_links() is None:
            self.ui.outputEdit.append("Импорт произошел")
        else:
            self.ui.outputEdit.append("Импорт не произошел")

    def export_database(self):
        """Экспортирует записи из бд в файл"""
        if export_links() is None:
            self.ui.outputEdit.append("Экспорт произошел")
        else:
            self.ui.outputEdit.append("Экспорт не произошел")

    def generate_report(self):
        """Генерация отчета по url"""
        try:
            url = self.ui.textEdit.toPlainText()
            is_ssl = check_url_ssl(url)
            whois_info = check_url_whois(url)
            status = "Безопасен" if is_ssl else "Подозрительный"
            google_response = google_api(url)
            if google_response != "Небезопасно" and google_response != "Безопасно":
                raise Exception
        except Exception as e:
            self.ui.outputEdit.append(f"Формирование отчета не произошел : {e}")
            return
        if save_results_pdf(url, is_ssl, google_response, whois_info) is None:
            self.ui.outputEdit.append("Формирование отчета произошел")
        else:
            self.ui.outputEdit.append("Формирование отчета не произошел")

    def create_info(self):
      """Creates a new window displaying information about phishing."""
      msg_box = QMessageBox()
      msg_box.setWindowTitle("Как распознать фишинг")
      msg_box.setText(
          "Основные признаки фишинга:\n\n"
          "1. **Неожиданные письма/сообщения:** Будьте осторожны, если получили сообщение от неизвестного отправителя или от известного, но с неожиданным содержанием.\n"
          "2. **Запросы личной информации:** Легитимные организации редко запрашивают личную информацию (пароли, номера карт) по электронной почте.\n"
          "3. **Срочность/угрозы:** Фишинговые письма часто создают ощущение срочности или содержат угрозы для принуждения к действиям.\n"
          "4. **Подозрительные ссылки:** Проверяйте ссылки перед тем, как на них нажимать. Обратите внимание на доменное имя и написание ссылки. \n"
          "5. **Ошибки в тексте:** Фишинговые письма могут содержать грамматические или стилистические ошибки.\n"
          "6. **Несоответствие запрошенных данных:** Если в письме есть подозрительные несоответствия в данных, это может говорить о фишинге. \n"
          "7. **Проверяйте отправителя:** Перепроверяйте адрес электронной почты отправителя перед тем, как переходить по ссылкам.\n"
          "\nЕсли у вас есть сомнения, лучше проверьте информацию по телефону или на официальном сайте организации, которая упоминается в сообщении."
      )
      msg_box.setIcon(QMessageBox.Icon.Information)
      msg_box.exec()
def main():
    app = QApplication(sys.argv)  # Создаем приложение
    window = MainApp()
    window.show()
    sys.exit(app.exec())  # Завершаем приложение, после его закрытия


if __name__ == "__main__":
    init_db()  # Инициализация базы данных
    main()  # Запуск приложения
