import os
import datetime
import urllib
import requests

SPARROW_PREFIX='SPARROW'
ENDPOINT='https://secure.sparrowone.com/Payments/Services_api.aspx'
class Connection:
    def __init__(self, mkey=None):
        if(mkey==None):
            if(os.environ.get(f"{SPARROW_PREFIX}_MKEY") is not None):
                mkey = os.environ[f"{SPARROW_PREFIX}_MKEY"]
            else:
                raise ConnectionError("An MKEY is required.")
        self.mkey = mkey
        print(f"MKEY is {mkey}")

    def simpleSale(self, amount, cardInfo):
        payload = cardInfo.to_dict()
        payload['mkey']=self.mkey
        payload['transtype']='sale'
        payload['amount']=amount
        r = requests.post(ENDPOINT, data=payload)
        return Response(r.text)

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
        for k in d:
            v = d[k][0]
            self.__dict__[k] = int(v) if self.is_number(v) else v

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass
 
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        
        return False