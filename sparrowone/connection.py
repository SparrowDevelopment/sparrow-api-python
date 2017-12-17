try:
    from urllib.parse import parse_qsl
except ImportError:
    from urlparse import parse_qsl

import requests

from .models import PaymentMethod, SaleInfo
from .invoices import invoice_factory
from .customers import customer_factory
from .plans import plan_factory
from .errors import SparrowAPIError


class Connection(object):
    API_URL = "https://secure.sparrowone.com/Payments/Services_api.aspx"

    def __init__(self, m_key):
        """
        A Sparrow API client.

        Args:
            m_key (str): Merchant Key, can be obitained in your
                        Sparrow account
        """
        self.m_key = m_key
        self.invoices = invoice_factory(self)
        self.customers = customer_factory(self)
        self.plans = plan_factory(self)

    def _error(self, data):
        return "errorcode" in data or data.get("response", "1") not in ["00", "1"]

    def _format_value(self, val):
        if type(val) is bool:
            return str(val).lower()

        return val

    def _call(self, transtype, **kwargs):
        kwargs.setdefault("mkey", self.m_key)
        kwargs.setdefault("transtype", transtype)

        data = {
            k: self._format_value(v)
            for k, v in kwargs.items()
            if v is not None
        }

        r = requests.post(self.API_URL, data=data)
        # return r  # XXX
        data = dict(parse_qsl(r.text))
        if self._error(data):
            raise SparrowAPIError(data, r)

        return data

    def sale(self, amount_or_sale, payment_method):
        """
        Direct a transaction to the appropriate merchant account
        for transaction processing. (TODO: proper docs)

        Args:
            amount_or_sale (float or .models.SaleInfo):
                total amount to be charged
            card_info (.models.PaymentMethod):
                card to be charged
        """

        if "sale" not in payment_method.allowed_methods:
            raise TypeError("This payment method doesn't support sale()")

        if not isinstance(amount_or_sale, SaleInfo):
            amount_or_sale = SaleInfo(amount=amount_or_sale)

        kwargs = {}
        kwargs.update(amount_or_sale)
        kwargs.update(payment_method)

        return self._call("sale", **kwargs)

    def auth(self, amount_or_sale, payment_method):
        """
        Direct a transaction to the appropriate merchant account
        for transaction processing. (TODO: proper docs)

        Args:
            amount_or_sale (float or .models.SaleInfo):
                total amount to be charged
            card_info (.models.PaymentMethod):
                card to be charged
        """

        if "auth" not in payment_method.allowed_methods:
            raise TypeError("This payment method doesn't support auth()")

        if not isinstance(amount_or_sale, SaleInfo):
            amount_or_sale = SaleInfo(amount=amount_or_sale)

        kwargs = {}
        kwargs.update(amount_or_sale)
        kwargs.update(payment_method)

        return self._call("auth", **kwargs)

    def verify(self, payment_method):
        """
        An Account Verification transaction is used when certain aspects
        of the credit card are needed prior to a purchase. An Account
        Verification transaction would be sent in as a normal Authorization
        request with the amount of $0.
        """

        return self.auth(amount_or_sale=0, payment_method=payment_method)
    
    def balance_inquire(self, payment_method):
        """
        The Balance Inquiry operation returns the available card balance.
        """

        if "balance_inquire" not in payment_method.allowed_methods:
            raise TypeError("This payment method doesn't support balance_inquire()")

        return self._call("balanceinquire", **payment_method)

    def refund(self, transid, amount, ach_account={},
               send_receipt_to_billing_email=False,
               send_receipt_to_shipping_email=False,
               send_receipt_to=[]):
        return self._call("refund",
                          transid=transid,
                          amount=amount,
                          sendtransreceipttobillemail=send_receipt_to_billing_email,
                          sendtransreceipttoshipemail=send_receipt_to_shipping_email,
                          sendtransreceipttoemails=",".join(send_receipt_to),
                          **ach_account)

    def void(self, transid, amount,
             send_receipt_to_billing_email=False,
             send_receipt_to_shipping_email=False,
             send_receipt_to=[]):
        return self._call("void",
                          transid=transid,
                          amount=amount,
                          sendtransreceipttobillemail=send_receipt_to_billing_email,
                          sendtransreceipttoshipemail=send_receipt_to_shipping_email,
                          sendtransreceipttoemails=",".join(send_receipt_to))

    def chargeback(self, transid, amount, reason):
        return self._call("chargeback",
                          transid=transid,
                          amount=amount,
                          reason=reason)

    def offline(self, amount_or_sale, payment_method,
                auth_code, auth_date=None):
        """
        Offline Capture closes an open authorization which was manually
        obtained from the card issuer.

        Args:
            amount_or_sale (float or .models.SaleInfo):
                total amount to be charged
            card_info (.models.PaymentMethod):
                card to be charged
            auth_code (str):
                auth code received from the issuer
            auth_date (str):
                date that auth code was obtained, required for Chase only
                (MM/DD/YYYY)
        """

        if "offline" not in payment_method.allowed_methods:
            raise TypeError("This payment method doesn't support offline()")

        if not isinstance(amount_or_sale, SaleInfo):
            amount_or_sale = SaleInfo(amount=amount_or_sale)

        kwargs = {
            "authcode": auth_code,
            "authdate": auth_date,
        }
        kwargs.update(amount_or_sale)
        kwargs.update(payment_method)

        return self._call("offline", **kwargs)

    def capture(self, transid, amount, card_exp,
               send_receipt_to_billing_email=False,
               send_receipt_to_shipping_email=False,
               send_receipt_to=[]):
        return self._call("capture",
                          transid=transid,
                          amount=amount,
                          cardexp=card_exp,
                          sendtransreceipttobillemail=send_receipt_to_billing_email,
                          sendtransreceipttoshipemail=send_receipt_to_shipping_email,
                          sendtransreceipttoemails=",".join(send_receipt_to))

    def credit(self, amount_or_sale, payment_method):
        if "credit" not in payment_method.allowed_methods:
            raise TypeError("This payment method doesn't support credit()")

        if not isinstance(amount_or_sale, SaleInfo):
            amount_or_sale = SaleInfo(amount=amount_or_sale)

        kwargs = {}
        kwargs.update(amount_or_sale)
        kwargs.update(payment_method)

        return self._call("credit", **kwargs)
