from bs4 import BeautifulSoup


def drop_whitespace(soup: BeautifulSoup) -> str:
    return soup.text.replace('\n', '').replace(' ', '').replace('\r', '').replace('\t', '')