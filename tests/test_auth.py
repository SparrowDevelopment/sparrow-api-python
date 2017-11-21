import unittest

import sparrowone

M_KEY = "CUK5YODHVAZHFBM6KESZO1J4"


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.sprw = sparrowone.Connection(M_KEY)

    def test_simple_sale(self):
        card = sparrowone.CardInfo(
            number="4111111111111111",
            expiration="1019",
            cvv="999"
        )
        resp = self.sprw.auth(10.0, card)
        self.assertEqual(resp["textresponse"], "SUCCESS")

    def test_advanced_sale(self):
        sale = sparrowone.SaleInfo(
            amount=7.96,
            currency="USD",
            billing_contact=sparrowone.Contact(
                first_name="Dana",
                last_name="Zane",
            ),
            ship_to=sparrowone.Contact(
                first_name="Julianne",
                last_name="Stingray",
                address1="16100 N 72nd Street",
                address2="Suite 171",
                city="Glitch City",
                zip="220000",
                country="XX",
                email="noreply@sparrowone.com",
            ),
            products=[
                sparrowone.Product(skunumber=1999,
                                description="Blue whale",
                                amount=1.99,
                                quantity=4)
            ],
            ip_addr="192.168.12.34",
        )

        card = sparrowone.CardInfo(
            number="4111111111111111",
            expiration="1019",
            cvv="999",
        )

        resp = self.sprw.auth(sale, card)
        self.assertEqual(resp["textresponse"], "SUCCESS")


class CaptureTestCase(unittest.TestCase):
    def setUp(self):
        self.sprw = sparrowone.Connection(M_KEY)
        self.card = sparrowone.CardInfo(
            number="4111111111111111",
            expiration="1019",
            cvv="999"
        )
        resp = self.sprw.auth(10.0, self.card)
        self.transid = resp["transid"]
        self.card_exp = "1019"
        self.amount = 10.0

    def test_simple_capture(self):
        resp = self.sprw.capture(self.transid, self.amount,
                                 card_exp=self.card_exp)
        self.assertEqual(resp["textresponse"], "SUCCESS")
    
    def test_simple_offline_capture(self):
        resp = self.sprw.offline(self.amount, self.card,
                                 auth_code="123456",
                                 auth_date="01/31/2017")
        self.assertEqual(resp["textresponse"], "SUCCESS")
