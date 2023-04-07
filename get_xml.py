import requests
from datetime import datetime


def get_today_date() -> str:
    today = datetime.today().strftime('%d/%m/%Y')
    return today


def join_url(today: str, base='https://www.cbr.ru/scripts/XML_daily.asp?date_req=') -> str:
    url = base + today
    return url


def get_url() -> str:
    today = get_today_date()
    url = join_url(today)
    return url


def get_xml_file():
    url = get_url()
    file = requests.get(url)
    return file.text


if __name__ == "__main__":
    url = get_url()
    get_xml_file()
