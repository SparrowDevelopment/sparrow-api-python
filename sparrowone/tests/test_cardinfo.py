from sparrowone import Connection, ConnectionError, CardInfo
import pytest
from os import environ
import datetime

def test_cardinfo():
    ci = CardInfo(number='4111111111111111', expiration=datetime.date(2010, 5, 24), cvv='123')
    assert ci.number == '4111111111111111'
    assert ci.expiration == datetime.date(2010, 5, 24)
    assert ci.cvv == '123'

def test_cardinfo_dict():
    ci = CardInfo(number='4111111111111111', expiration=datetime.date(2010, 5, 24), cvv='123')
    d = ci.to_dict()
    assert d['cardnum'] == '4111111111111111'
    assert d['cardexp'] == '1005'
    assert d['cvv'] == '123'

def test_cardinfo_dict():
    ci = CardInfo(number='4111111111111111', expiration='1005', cvv='123')
    d = ci.to_dict()
    assert d['cardnum'] == '4111111111111111'
    assert d['cardexp'] == '1005'
    assert d['cvv'] == '123'
