from sparrowone import Connection, ConnectionError
import pytest
from os import environ

def test_empty_connection():
    with pytest.raises(ConnectionError):
        Connection()

def test_connection_with_mkey():
    c = Connection(mkey='123')
    assert c.mkey == '123'
    
def test_connection_with_env_mkey():
    environ['SPARROW_MKEY']='123'
    c = Connection()
    assert c.mkey == '123'