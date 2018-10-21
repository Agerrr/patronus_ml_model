from __future__ import unicode_literals
import pandas as pd
from bs4 import BeautifulSoup
import requests
import json


def get_avg_salaries_per_university():
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


def get_median_salary_by_uni_degree():
    PAYSCALE_URL = 'https://www.payscale.com'
    LIST_OF_UNIVERSITIES_URL = PAYSCALE_URL + '/index/UK/School'

    r = requests.get(LIST_OF_UNIVERSITIES_URL)
    data = r.text
    soup = BeautifulSoup(''.join(data), "html.parser")
    tab = soup.find("table", {"class": "table table-condensed"})

    school_name_urls = tab.find_all("a", href=True)

    def get_uni_link_name(url):
        sublinks = url.split('/')
        uni_link_name = sublinks[3]
        uni_link_name = uni_link_name.replace('School=', '')
        return uni_link_name

    school_url_name_list = [(url['href'], url.string, get_uni_link_name(url['href'])) for url in school_name_urls]

    degree_salary_base_url_prefix = "https://api.payscale.com/rcdata/v1/school/"
    degree_salary_base_url_suffix = "/report/SALARY/subreport/Average%20Salary%20By%20Degree%20Major?countryAbbr=UK"

    degree_salary_for_all_unis_df = []
    for uni_salary_url, name, uni_link_name in school_url_name_list:
        print(name)
        uni_link_name = uni_link_name.replace('_', '%20')
        degree_salary_url = degree_salary_base_url_prefix + uni_link_name + degree_salary_base_url_suffix
        degree_salary_response = requests.get(degree_salary_url)
        degree_salary_dict = json.loads(degree_salary_response.text)
        degree_salary_df = pd.DataFrame(degree_salary_dict['rows'])

        degree_salary_df['university'] = name
        degree_salary_for_all_unis_df.append(degree_salary_df)

    degree_salary_for_all_unis_df = pd.concat(degree_salary_for_all_unis_df)
    return degree_salary_for_all_unis_df



