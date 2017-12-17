from sparrowone import SPARROW_PREFIX, Connection, ConnectionError
import pytest
from os import environ

def test_empty_connection():
    with pytest.raises(ConnectionError):
        Connection()

def test_connection_with_mkey():
    c = Connection(mkey='123')
    assert c.mkey == '123'
    
def test_connection_with_env_mkey():
    k = "{SPARROW_PREFIX}_MKEY"
    old=None
    if k in environ:
        old = environ[k]
    environ['SPARROW_MKEY']='123'
    c = Connection()
    assert c.mkey == '123'
    if(old):
        environ[k]=old
    