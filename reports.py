import io
from PyQt6.QtWidgets import QFileDialog
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
from mailSender import sendEmail

def save_results_pdf(url, is_ssl, google_response, whois_info):
    try:
        # Получить текущую дату в нужном формате
        check_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Открыть диалог сохранения файла
        file_name, _ = QFileDialog.getSaveFileName(
            None, "Save report", "", "PDF Files (*.pdf)"
        )
        if not file_name:  # Выход, если файл не выбран
            return 0

        # Создать PDF документ с использованием ReportLab
        packet = io.BytesIO()
        c = canvas.Canvas(packet, pagesize=letter)

        # Используем шрифт, поддерживающий кириллицу (Times-Roman)
        c.setFont("Helvetica", 10)

        # Заголовок документа
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, 750, "The result of the URL check")

        # Дата проверки
        c.setFont("Helvetica", 10)
        y = 730  # Начальная координата по оси Y
        c.drawString(50, y, f"Check Date: {check_date}")
        y -= 20

        # URL
        c.drawString(50, y, f"URL: {url}")
        y -= 20

        # Результат проверки SSL
        ssl_status = "Safe" if is_ssl else "Suspicious"
        c.drawString(50, y, f"The result of SSL: {ssl_status}")
        y -= 20

        # Результат Google Safe Browsing
        google_response = "Safe" if (google_response == "Безопасно") else "Suspicious"
        c.drawString(50, y, f"Result Google Safe Browsing: {google_response}")
        y -= 20

        # Информация WHOIS
        c.drawString(50, y, "WHOIS information:")
        y -= 15

        # Проходим по информации WHOIS и выводим ключ-значение
        c.setFont("Helvetica", 10)
        for key, value in whois_info.items():
            # Если место на странице заканчивается, создаем новую страницу
            if y < 50:
                c.showPage()
                y = 750

            # Выводим ключ и значение
            c.drawString(60, y, f"{key}: {value}")
            y -= 15

        c.save()

        # Записываем содержимое, созданное ReportLab, в PyPDF2
        packet.seek(0)
        new_pdf = PdfReader(packet)
        writer = PdfWriter()

        # Добавляем страницу, созданную ReportLab, в PdfWriter
        writer.add_page(new_pdf.pages[0])

        # Сохраняем PDF
        with open(file_name, "wb") as output_file:
            writer.write(output_file)

        
        sendEmail(  pdf_path=file_name,
                    subject="Отчет",
                    body="Отчет приложения Catcheck",
                    to_email='ayzat2142@gmail.com',  # Замените на реальный email
                    from_email='catcheckrobot@gmail.com'  # Замените на реальный email
                )
        return None
    except Exception as e:
        return e
