
import requests


# api - ключ от сервисов google, для пользования api google save browsing
API_KEY = "AIzaSyA01TyRfuGCtCjil93vczc5sfNWshjjf2E"
URL = 'https://safebrowsing.googleapis.com/v4/threatMatches:find?key=' + API_KEY

def check_url_safety(url):
    """ Проверка url по api google save browsing

    Args:
        url (_type_): str

    Returns:
        _type_: str 
    """    
    # Создаем payload для API
    payload = {
        "client": {
            "clientId": "yourcompanyname",
            "clientVersion": "1.5.2"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }

    # Отправляем запрос
    response = requests.post(URL, json=payload)
    if response.status_code == 200:
        threats = response.json()
        if "matches" in threats:
            return "Небезопасно"
        else:
            return "Безопасно"
    else:
        return f"Ошибка: {response.status_code} - {response.text}"

if __name__ == "__main__":
    url_to_check = "http://testsafebrowsing.appspot.com/s/malware.html"
    result = check_url_safety(url_to_check)
    print(result)