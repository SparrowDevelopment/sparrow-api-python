import unittest

import sparrowone


M_KEY = "CUK5YODHVAZHFBM6KESZO1J4"

class RefundTestCase(unittest.TestCase):
    def setUp(self):
        self.sprw = sparrowone.Connection(M_KEY)
        card = sparrowone.CardInfo(
            number="4111111111111111",
            expiration="1019",
            cvv="999"
        )
        resp = self.sprw.sale(10.0, card)
        self.transid = resp["transid"]
        self.amount = 10.0

    def test_simple_refund(self):
        resp = self.sprw.refund(self.transid, self.amount)
        self.assertEqual(resp["textresponse"], "SUCCESS")

    def test_simple_void(self):
        resp = self.sprw.void(self.transid, self.amount)
        # XXX: I'd rather check for 'response' rather than 'textresponse'
        # here but it's what the official test suite does:
        #     https://github.com/SparrowDevelopment/sparrow-api-curl/blob/fe0275261d9b1c7918dbe1aa2133f64dc89468c6/api#L478-L513
        self.assertEqual(resp["textresponse"], "Transaction Void Successful")

    def test_advanced_refund(self):
        resp = self.sprw.refund(
            self.transid, self.amount,
            send_receipt_to_billing_email=True,
            send_receipt_to_shipping_email=True,
            send_receipt_to=["noreply@sparrowone.com"]
        )
        self.assertEqual(resp["textresponse"], "SUCCESS")

    def test_advanced_void(self):
        resp = self.sprw.void(
            self.transid, self.amount,
            send_receipt_to_billing_email=True,
            send_receipt_to_shipping_email=True,
            send_receipt_to=["noreply@sparrowone.com"]
        )
        # XXX: (see test_simple_void)
        self.assertEqual(resp["textresponse"], "Transaction Void Successful")
