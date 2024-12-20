import csv
from database import get_links

def generate_report_csv(file_name="report.csv"):
    links = get_links()
    if not links:
        print("Нет данных для создания отчета.")
        return
    try:
        with open(file_name, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "URL", "Status", "Added On"])
            writer.writerows(links)
        print(f"Отчет успешно сохранен в {file_name}.")
    except Exception as e:
        print(f"Ошибка при создании отчета: {e}")

if __name__ == "__main__":
    generate_report_csv()
