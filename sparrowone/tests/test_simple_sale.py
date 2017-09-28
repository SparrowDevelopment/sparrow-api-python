from sparrowone import Connection, ConnectionError, CardInfo
import pytest
from os import environ
import datetime
from pprint import pprint

def test_bad_mkey():
    c = Connection(mkey='123')
    ci = CardInfo(number='4111111111111111', expiration=datetime.date(2010, 5, 24), cvv='123')
    res = c.simpleSale(9.95, ci)
    pprint(vars(res))
    assert res.response == 3
