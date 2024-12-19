from PyQt6.QtWidgets import QFileDialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import textwrap

def save_results_pdf(url, is_ssl, google_response, whois_info):
    try: 
        # Открытие диалога сохранения файла
        file_name, _ = QFileDialog.getSaveFileName(
            None, "Сохранить отчет", "", "PDF Files (*.pdf)"
        )
        if not file_name:  # Если файл не выбран, выходим
            return 0

        # Создаем PDF-документ
        pdf = canvas.Canvas(file_name, pagesize=letter)
        width, height = letter

        # Заголовок документа
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(50, height - 50, "The result of the check URL")

        # Основной текст
        pdf.setFont("Helvetica", 10)
        y = height - 80  # Стартовая координата по высоте

        # Записываем URL
        pdf.drawString(50, y, f"URL: {url}")
        y -= 20

        # Результат проверки SSL
        ssl_status = "Safe" if is_ssl else "Suspicious"
        pdf.drawString(50, y, f"The result of SSL: {ssl_status}")
        y -= 20

        # Результат Google Safe Browsing
        google_response = "Safe" if (google_response == "Безопасно") else "Suspicious"
        pdf.drawString(50, y, f"Result Google Safe Browsing: {google_response}")
        y -= 20

        # WHOIS информация
        pdf.drawString(50, y, "WHOIS information:")
        y -= 15

        # Разбиваем WHOIS информацию на строки с переносами
        whois_text = str(whois_info)  # Преобразуем в строку
        wrapped_lines = textwrap.wrap(whois_text, width=90)  # Перенос строк по 90 символов

        for line in wrapped_lines:
            if y < 50:  # Если место на странице закончилось
                pdf.showPage()
                pdf.setFont("Helvetica", 10)
                y = height - 50
            pdf.drawString(60, y, line)
            y -= 15

        # Сохраняем PDF
        pdf.save()
        return None
    except Exception as e:
        return e