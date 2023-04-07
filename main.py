import xml.etree.cElementTree as ET
from get_xml import get_xml_file
from settings import get_logger

logger = get_logger(__name__)


def parse_data_from_xml(xmlstring: str) -> list:
    list_currencies = []
    try:
        tree = ET.fromstring(xmlstring)
        currencies = tree.findall('Valute')
        for VALUTE in currencies:
            nominal = VALUTE.find('Nominal')
            name = VALUTE.find('Name')
            value = VALUTE.find('Value')
            if name.text == 'СДР (специальные права заимствования)':
                continue
            list_currencies.append(f'{nominal.text} {name.text} = {value.text} руб.')
    except Exception as error:
        logger.error(error)

    return list_currencies


def create_text_message(list_strings: list) -> str:
    message = '\n\n'.join(list_strings)
    return message


def get_message():
    xml_str = get_xml_file()
    list_str = parse_data_from_xml(xml_str)
    message = create_text_message(list_str)

    return message


if __name__ == "__main__":
    print(get_message())
    pass
