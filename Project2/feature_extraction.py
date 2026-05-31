import re
import requests
import tldextract
from urllib.parse import urlparse
from bs4 import BeautifulSoup


def extract_features(url):

    features = []

    # 1 URL Length
    features.append(len(url))

    # 2 HTTPS
    features.append(1 if url.startswith("https") else 0)

    # 3 Dot Count
    features.append(url.count('.'))

    # 4 Hyphen Count
    features.append(url.count('-'))

    # 5 @ Symbol Count
    features.append(url.count('@'))

    # 6 Digit Count
    features.append(sum(c.isdigit() for c in url))

    # 7 Suspicious Words
    suspicious_words = [
        'login',
        'verify',
        'secure',
        'account',
        'update',
        'banking',
        'confirm',
        'password',
        'signin',
        'wp',
        'admin'
    ]

    suspicious_count = sum(
        word in url.lower()
        for word in suspicious_words
    )

    features.append(suspicious_count)

    # 8 IP Address Presence
    ip_pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')

    features.append(
        1 if ip_pattern.search(url) else 0
    )

    # 9 Subdomain Count
    ext = tldextract.extract(url)

    subdomains = ext.subdomain.split('.')

    features.append(len(subdomains))

    # 10 Path Length
    parsed = urlparse(url)

    features.append(len(parsed.path))

    # 11 Query Length
    features.append(len(parsed.query))

    # 12 Special Characters
    special_chars = ['=', '?', '%', '&']

    special_count = sum(url.count(char) for char in special_chars)

    features.append(special_count)

    # 13 HTML Features
    iframe_count = 0
    form_count = 0

    try:

        response = requests.get(
            url,
            timeout=5,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        soup = BeautifulSoup(response.text, "html.parser")

        iframe_count = len(soup.find_all("iframe"))

        form_count = len(soup.find_all("form"))

    except:
        pass

    features.append(iframe_count)

    features.append(form_count)

    return features