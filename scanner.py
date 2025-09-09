import requests
from bs4 import BeautifulSoup

def check_sql_injection(url):
    test_url = url + "'"
    try:
        r = requests.get(test_url, timeout=5)
        if "sql" in r.text.lower() or "syntax" in r.text.lower():
            return True
    except:
        return False
    return False

def check_xss(url):
    payload = "<script>alert('XSS')</script>"
    try:
        r = requests.get(url, params={"q": payload}, timeout=5)
        if payload in r.text:
            return True
    except:
        return False
    return False

def scan(url):
    results = {}
    results["SQL Injection"] = check_sql_injection(url)
    results["XSS"] = check_xss(url)
    return results
