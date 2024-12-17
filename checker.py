import requests
import whois
from datetime import datetime

def check_url_ssl(url):
    try:
        response = requests.get(url, timeout=5)
        return 'https' in response.url
    except requests.RequestException:
        return False

def check_url_whois(url):
    try:
        domain_info = whois.whois(url)
        return {
            "registrar": domain_info.registrar,
            "creation_date": domain_info.creation_date,
            "expiration_date": domain_info.expiration_date
        }
    except Exception:
        return "WHOIS data not found"
