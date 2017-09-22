import os
import datetime
import urllib

class Connection:
    def __init__(self, mkey=None):
        if(mkey==None):
            if(os.environ.get('SPARROW_MKEY') is not None):
                mkey = os.environ['SPARROW_MKEY']
            else:
                raise ConnectionError("An MKEY is required.")
        self.mkey = mkey

    def simpleSale(self, amount, cardInfo):
        return Response("response=3")

class ConnectionError(Exception):
    pass


class CardInfo:
    def __init__(self, number=None, expiration=None, cvv=None):
        self.number = number
        self.expiration = expiration
        self.cvv = cvv
        
    def to_dict(self):
        d = {}
        d['cardnum'] = self.number
        d['cardexp'] = self.expiration.strftime('%y%m') if type(self.expiration) is datetime.date else self.expiration
        d['cvv'] = self.cvv
        return d
        
class Response:
    def __init__(self, responseString):
        d = urllib.parse.parse_qs(responseString)
        self.__dict__ = d
