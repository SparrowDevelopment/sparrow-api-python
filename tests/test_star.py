import unittest

import sparrowone

M_KEY = "CUK5YODHVAZHFBM6KESZO1J4"


class StarTestCase(unittest.TestCase):
    def setUp(self):
        self.sprw = sparrowone.Connection(M_KEY)

    def test_simple_star_card(self):
        card = sparrowone.MilitaryStarCard(
            number="4111111111111111",
            expiration="1019",
            cid="12345678901"
        )
        resp = self.sprw.sale(10.0, card)
        self.assertEqual(resp["textresponse"], "SUCCESS")
    
    def test_advanced_star_card(self):
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
                sparrowone.Product(
                    skunumber=1999,
                    description="Blue whale",
                    amount=1.99,
                    quantity=4
                )
            ],
            ip_addr="192.168.12.34",
        )
        card = sparrowone.MilitaryStarCard(
            number="4111111111111111",
            expiration="1019",
            cid="12345678901"
        )
        resp = self.sprw.sale(sale, card)
        self.assertEqual(resp["textresponse"], "SUCCESS")