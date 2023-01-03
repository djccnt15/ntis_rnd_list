from bs4 import BeautifulSoup

def drop_whitespace(soup: BeautifulSoup) -> str:
    """remove meaninglessly appended whitespace from beautifulsoup object"""

    return soup.text.replace('\n', '').replace(' ', '').replace('\r', '').replace('\t', '')