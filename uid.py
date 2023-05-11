from dataclasses import dataclass, asdict

import requests
from bs4 import BeautifulSoup

from common import *


@dataclass(frozen=True, order=True, unsafe_hash=True)
class RecordRnd:
    """structure for rnd record"""

    serial: int
    uid: int


def cleanse_record(soup: BeautifulSoup) -> RecordRnd:
    """get serial and uid from scrapped web page and returns structure of them"""

    scrap: list = soup.find_all('td')
    serial: int = int(drop_whitespace(scrap[1]))
    uid: int = int(soup.find('input')['value'])  # type: ignore
    return RecordRnd(serial=serial, uid=uid)


def scraping(
    page_list: str = 'https://www.ntis.go.kr/rndgate/eg/un/ra/mng.do',
    paginate: int = 100,
    pageid: int = 1
) -> list:
    """scrap web data and returns cleansed data"""

    response = requests.post(
        url=page_list,
        data={
            'pageUnit': paginate,
            'pageIndex': pageid
        }
    )
    soup = BeautifulSoup(markup=response.text, features='html.parser')
    records = soup.find_all('tbody')[3].find_all('tr')
    return [asdict(cleanse_record(i)) for i in records]


def total_num() -> int:
    page_list: str = 'https://www.ntis.go.kr/rndgate/eg/un/ra/mng.do'
    response = requests.get(page_list)
    soup = BeautifulSoup(markup=response.text, features='html.parser')
    return soup.find('input', {'id':'totalCount'})['value']  # type: ignore


if __name__ == '__main__':
    import csv
    from pathlib import Path

    data = scraping()
    # print(data)
    # print(total_num())

    with open(file=Path('tmp') / 'table_uid.csv', mode='w', newline='') as f:
        csv_cols = data[0].keys()
        table_uid = csv.DictWriter(f, csv_cols)
        table_uid.writeheader()
        for i in data:
            table_uid.writerow(i)