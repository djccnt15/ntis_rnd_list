from pathlib import Path

import selenium
import requests
from bs4 import BeautifulSoup


class RecordRnd:
    """data model class for rnd record"""

    def __init__(self, _serial: int, _department: str, _title: str) -> None:
        self.serial: int = _serial
        self.department: str = _department
        self.title: str = _title

    def to_dict(self) -> dict:
        data = {
            'serial': self.serial,
            'department': self.department,
            'title': self.title,
        }
        return data


def drop_whitespace(soup: BeautifulSoup) -> str:
    return soup.text.replace('\n', '').replace(' ', '').replace('\r', '')


def cleanse_record(soup: BeautifulSoup) -> RecordRnd:
    scrap: list = soup.find_all('td')
    serial: int = int(drop_whitespace(scrap[1]))
    department: str = drop_whitespace(scrap[3])
    title: str = soup.find('input')['title']  # type: ignore
    return RecordRnd(serial, department, title)


def get_records(soup: BeautifulSoup) -> list:
    return soup.find_all('tbody')[3].find_all('tr')


if __name__ == '__main__':
    path_sample = 'sample'
    file_name = 'response.html'
    sample = Path(path_sample, file_name)

    if sample.is_file():
        with open(file=sample, mode='r', encoding='utf-8') as f:
            soup = BeautifulSoup(markup=f, features='html.parser')
    else:
        # basic scrap
        url_scrap = 'https://www.ntis.go.kr/rndgate/eg/un/ra/mng.do'
        response = requests.get(url=url_scrap)
        soup = BeautifulSoup(markup=response.text, features='html.parser')

        # save sample file
        with open(file=sample, mode='w', encoding='utf-8') as f:
            f.write(response.text)

    # print cleansed scrap data
    records = get_records(soup=soup)
    # print(records)
    [print(cleanse_record(i).to_dict()) for i in records]