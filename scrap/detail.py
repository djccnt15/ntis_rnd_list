import time
from datetime import datetime, date

import requests
from bs4 import BeautifulSoup

from scrap.common import *


class DetailRnd:
    """structure for detail information of R&D"""

    def __init__(
        self,
        title: str,
        department: str,
        gov_agency: str,
        date_notice: date,
        budget: str
    ) -> None:
        self.title = title
        self.department = department
        self.gov_agency = gov_agency
        self.date_notice = date_notice
        self.budget = budget

    def to_dict(self) -> dict:
        data = {
            'title': self.title,
            'department': self.department,
            'gov_agency': self.gov_agency,
            'date_notice': self.date_notice,
            'budget': self.budget,
        }
        return data


def cleans_detail(soup: BeautifulSoup) -> DetailRnd:
    """get detail information from web scrapping and returns structure of it"""

    title: BeautifulSoup = soup.find('meta', {'property': 'og:description'})['content']  # type: ignore
    gov: BeautifulSoup = soup.find('div', {'class': 'summary1'}).find_all('li')  # type: ignore
    department: str = gov[1].text[6:]  # type: ignore
    gov_agency: str = gov[2].text[8:]  # type: ignore
    date_tmp: str = soup.find('div', {'class': 'summary2'}).find_all('li')[0].text[6:]  # type: ignore
    date_notice: date = datetime.strptime(date_tmp, '%Y.%m.%d').date()
    budget: str = drop_whitespace(soup.find_all('div', {'class': 'summary1'})[1].find_all('li')[1])[5:]

    return DetailRnd(
        title = title,  # type: ignore
        department = department,
        gov_agency = gov_agency,
        date_notice = date_notice,
        budget = budget,
    )


def scrapping(uid: int):
    """scrap web data and returns cleansed data"""

    url_scrap: str = f'https://www.ntis.go.kr/rndgate/eg/un/ra/view.do?roRndUid={uid}&flag=rndList'
    response = requests.get(url=url_scrap)
    soup = BeautifulSoup(markup=response.text, features='html.parser')
    return cleans_detail(soup=soup).to_dict()


if __name__ == '__main__':
    import csv
    from pathlib import Path
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-m', '--mode', dest='mode', default='scratch')
    args = parser.parse_args()

    mode = {
        'scratch': 0,
        'scrap': 1,
    }
    mode = mode[args.mode]

    path_tmp = 'tmp'
    list_name = 'table_uid.csv'
    list_uid = Path(path_tmp, list_name)

    if mode == 0:
        with open(file=list_uid, mode='r') as f:
            uid = list(csv.reader(f))[1][1]
        res = scrapping(uid=uid)  # type: ignore
        print(res)

    elif mode == 1:
        with open(file=list_uid, mode='r') as f:
            uid = list(csv.reader(f))

        for i, u in enumerate(uid):
            if i > 0:
                print(scrapping(uid=u[1]))  # type: ignore
                time.sleep(1)
            else: pass

    else: pass