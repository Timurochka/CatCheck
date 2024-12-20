import sqlite3
import csv

def import_links(file_name):
    try:
        conn = sqlite3.connect('phishing_links.db')
        cursor = conn.cursor()
        with open(file_name, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Пропустить заголовок
            for row in reader:
                cursor.execute(
                    'INSERT INTO phishing_links (url, status) VALUES (?, ?)',
                    (row[1], row[2])
                )
        conn.commit()
        conn.close()
        print(f"Импорт данных из {file_name} выполнен успешно.")
    except Exception as e:
        print(f"Ошибка при импорте данных: {e}")

def export_links(file_name="database.csv"):
    conn = sqlite3.connect('phishing_links.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM phishing_links")
    links = cursor.fetchall()
    conn.close()

    try:
        with open(file_name, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "URL", "Status", "Added On"])
            writer.writerows(links)
        print(f"База данных успешно экспортирована в {file_name}.")
    except Exception as e:
        print(f"Ошибка при экспорте: {e}")

def init_db():
    conn = sqlite3.connect('phishing_links.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS phishing_links (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            status TEXT NOT NULL,
            added_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def add_link(url, status):
    conn = sqlite3.connect('phishing_links.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO phishing_links (url, status) VALUES (?, ?)', (url, status))
    conn.commit()
    conn.close()

def get_links():
    conn = sqlite3.connect('phishing_links.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM phishing_links')
    links = cursor.fetchall()
    conn.close()
    return links

# Initialize the database
if __name__ == "__main__":
    init_db()
