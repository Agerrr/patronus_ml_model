import pandas as pd
from bs4 import BeautifulSoup
import requests

PAYSCALE_URL = 'https://www.payscale.com'
LIST_OF_UNIVERSITIES_URL = PAYSCALE_URL + '/index/UK/School'


def get_university_list(url):
    r = requests.get(LIST_OF_UNIVERSITIES_URL)
    data = r.text
    soup = BeautifulSoup(''.join(data), "html.parser")
    tab = soup.find("table", {"class": "table table-condensed"})
    school_name_urls = tab.find_all("a", href=True)
    school_names = [url.string for url in school_name_urls]
    return school_names





