import requests
from ipwhois import IPWhois
from pprint import pprint
import socket
from urllib.parse import urlparse


def check_url_ssl(url):
    try:
        response = requests.get(url, timeout=5)
        return 'https' in response.url
    except requests.RequestException:
        return False
def check_url_whois(url):
    ip = get_ip_from_url(url)
    whois_info_with_none = IPWhois(ip).lookup_rdap()
    whois_info = remove_none_values(whois_info_with_none)
    return whois_info
def get_ip_from_url(url):
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
    if isinstance(d, dict):
        return {k: remove_none_values(v) for k, v in d.items() if v is not None}
    elif isinstance(d, list):
        return [remove_none_values(item) for item in d if item is not None]
    else:
        return d
if __name__ == ('__main__'):
    #ip = "46.17.40.108"
    
    url = "https://ru.wikipedia.org"
    ip = get_ip_from_url(url)
    
    info_1 = check_url_ssl(url)
    
    info_5 = IPWhois(ip).lookup_rdap()
    info_5 = remove_none_values(info_5)
    pprint(f"SSl info : {info_1}")
    
    pprint(info_5)
