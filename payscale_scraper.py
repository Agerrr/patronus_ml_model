from __future__ import unicode_literals
import sys
import pandas as pd
from bs4 import BeautifulSoup
import requests


def get_universities_and_avg_salaries():
    PAYSCALE_URL = 'https://www.payscale.com'
    LIST_OF_UNIVERSITIES_URL = PAYSCALE_URL + '/index/UK/School'

    r = requests.get(LIST_OF_UNIVERSITIES_URL)
    data = r.text
    soup = BeautifulSoup(''.join(data), "html.parser")
    tab = soup.find("table", {"class": "table table-condensed"})

    school_name_urls = tab.find_all("a", href=True)
    school_url_name_list = [(url['href'], url.string) for url in school_name_urls]

    uni_avg_salary_dict = []

    for salary_url, name in school_url_name_list:
        print("Retrieving average salary for university: %s" % name)
        SALARY_URL = PAYSCALE_URL + salary_url
        salary_response = requests.get(SALARY_URL)
        salary_data = salary_response.text
        salary_soup = BeautifulSoup(''.join(salary_data), "html.parser")

        avg_pay = salary_soup.find("div", {"class": "pay-value"})
        if avg_pay:
            avg_pay = avg_pay.string
        uni_avg_salary_dict.append(pd.DataFrame({'university': name, 'avg_entry_salary': avg_pay}, index=[0]))

    uni_avg_salary_dict = pd.concat(uni_avg_salary_dict)
    return uni_avg_salary_dict





