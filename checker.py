import requests
from ipwhois import IPWhois
from urllib.parse import urlparse
import socket


def check_url_ssl(url):
    """Проверка HTTPS соединения."""
    try:
        response = requests.get(url, timeout=5)
        return 'https' in response.url
    except requests.RequestException:
        return False


def get_ip_from_url(url):
    """Возвращает IP по доменному имени."""
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.hostname  # Извлекаем только домен
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        print(f"Ошибка получения IP для {url}: {e}")
        return None


def remove_none_values(data):
    """Удаляет пустые значения из словаря."""
    if isinstance(data, dict):
        return {k: remove_none_values(v) for k, v in data.items() if v is not None}
    elif isinstance(data, list):
        return [remove_none_values(v) for v in data if v is not None]
    else:
        return data


def parse_whois_info(whois_info):
    """Парсинг информации WHOIS для читаемого вывода."""
    objects = whois_info.get("objects", {})
    first_object_key = next(iter(objects), None)

    contact_info = objects.get(first_object_key, {}).get("contact", {})
    abuse_email = next(
        (
            obj.get("contact", {}).get("email", [{}])[0].get("value", "N/A")
            for obj in objects.values()
            if "abuse" in obj.get("roles", [])
        ),
        "N/A",
    )

    parsed_info = {
        "ASN (Autonomous System)": whois_info.get("asn", "N/A"),
    "ASN Country Code": whois_info.get("asn_country_code", "N/A"),
    "ASN Description": whois_info.get("asn_description", "N/A"),
    "IP Range": whois_info.get("network", {}).get("cidr", "N/A"),
    "IP Version": whois_info.get("network", {}).get("ip_version", "N/A"),
    "Organization": contact_info.get("name", "N/A"),
    "Contact Email": contact_info.get("email", [{}])[0].get("value", "N/A"),
    "Abuse Email": abuse_email,
    "Registration Date": whois_info.get("network", {}).get(
        "events", [{}]
    )[0].get("timestamp", "N/A"),
    }
    return parsed_info


def check_url_whois(url):
    """Проверка WHOIS информации по URL."""
    ip = get_ip_from_url(url)
    if not ip:
        return {"Ошибка": "Невозможно получить IP-адрес."}
    try:
        whois_info_with_none = IPWhois(ip).lookup_rdap()
        whois_info = remove_none_values(whois_info_with_none)
        return parse_whois_info(whois_info)
    except Exception as e:
        return {"Ошибка": str(e)}


def get_ip_from_url(url):
    """ Возввращает ip по доменному имени
    input:  url
    output: ip_address
    """
    try:
        # Извлекаем домен из URL
        parsed_url = urlparse(url)
        domain = parsed_url.hostname  # Извлекаем только домен без протокола

        # Получаем IP-адрес по доменному имени
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        # В случае ошибки, например, если домен не существует
        print(f"Ошибка получения IP для {url}: {e}")
        return None


def remove_none_values(d):
    """Чистит информацию от None (в информации whois много None)
    input: dictionary
    output: dictionary
    """
    if isinstance(d, dict):
        return {k: remove_none_values(v) for k, v in d.items() if v is not None}
    elif isinstance(d, list):
        return [remove_none_values(item) for item in d if item is not None]
    else:
        return d


if __name__ == ('__main__'):
    ##  Проверка всех функций
    # ip = "46.17.40.108"

    url = "https://ru.wikipedia.org"
    ip = get_ip_from_url(url)

    info_1 = check_url_ssl(url)

    info_5 = IPWhois(ip).lookup_rdap()
    info_5 = remove_none_values(info_5)
    print(f"SSl info : {info_1}")

    print(info_5)