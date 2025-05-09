
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def sendEmail(pdf_path,subject, body, to_email, from_email):
    try:
        # Создаем объект сообщения
        msg = MIMEMultipart()
        msg["From"] = from_email
        msg["To"] = to_email
        msg["Subject"] = subject

        # Добавляем текст письма
        msg.attach(MIMEText(body, "plain"))

        # Открываем PDF-файл и добавляем его как вложение
        with open(pdf_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={pdf_path.split('/')[-1]}",  # Имя файла в письме
        )
        msg.attach(part)

        # Отправляем письмо через SMTP
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(from_email, password)
        smtp_server.sendmail(from_email, to_email, msg.as_string())
        smtp_server.quit()

        print("ok")
    except Exception as e:
        return 1    

if __name__ == "__main__":
    sendEmail(  pdf_path="1.pdf",
                    subject="afs",
                    body="body",
                    to_email='',  # Замените на реальный email
                    from_email=''  # Замените на реальный email
                )
