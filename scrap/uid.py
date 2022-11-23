import requests
from bs4 import BeautifulSoup

from scrap.common import *


class RecordRnd:
    """structure for rnd record"""

    def __init__(self, _serial: int, _uid: int) -> None:
        self.serial: int = _serial
        self.uid: int = _uid

    def to_dict(self) -> dict:
        data = {
            'serial': self.serial,
            'uid': self.uid,
        }
        return data


def cleanse_record(soup: BeautifulSoup) -> RecordRnd:
    """get serial and uid from scrapped web page and returns structure of them"""

    scrap: list = soup.find_all('td')
    serial: int = int(drop_whitespace(scrap[1]))
    uid: int = int(soup.find('input')['value'])  # type: ignore
    return RecordRnd(_serial=serial, _uid=uid)


def scrapping(
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
    return [cleanse_record(i).to_dict() for i in records]


def total_num() -> int:
    page_list: str = 'https://www.ntis.go.kr/rndgate/eg/un/ra/mng.do'
    response = requests.get(page_list)
    soup = BeautifulSoup(markup=response.text, features='html.parser')
    return soup.find('input', {'id':'totalCount'})['value']  # type: ignore

if __name__ == '__main__':
    import csv

    data = scrapping()
    # print(data)
    # print(total_num())

    with open(file='tmp/table_uid.csv', mode='w', newline='') as f:
        csv_cols = data[0].keys()
        table_uid = csv.DictWriter(f, csv_cols)
        table_uid.writeheader()
        [table_uid.writerow(i) for i in data]