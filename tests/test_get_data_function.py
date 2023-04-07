from get_xml import join_url
from main import parse_data_from_xml, create_text_message


def test_join_url():
    today = '01/04/2023'
    url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req=01/04/2023'
    assert join_url(today) == url


def test_parse_data_from_xml():
    xmlstr = """<ValCurs Date='06.04.2023' name='Foreign Currency Market'>
    <Valute ID="R01010">
        <NumCode>036</NumCode>
        <CharCode>AUD</CharCode>
        <Nominal>1</Nominal>
        <Name>Австралийский доллар</Name>
        <Value>53,5486</Value>
    </Valute>
    </ValCurs>"""
    except_str = "1 Австралийский доллар = 53,5486 руб."
    assert type(parse_data_from_xml(xmlstr)) == list
    assert len(parse_data_from_xml(xmlstr)) == 1
    assert parse_data_from_xml(xmlstr)[0] == except_str
    xmlstr = ''
    assert type(parse_data_from_xml(xmlstr)) == list


def test_create_text_message():
    list_strings = ['la', 'la', 'la']
    except_string = 'la\nla\nla'
    assert create_text_message(list_strings) == except_string
    list_strings = []
    except_string = ''
    assert create_text_message(list_strings) == except_string
