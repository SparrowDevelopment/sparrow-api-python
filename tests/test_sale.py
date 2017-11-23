import unittest

import sparrowone

M_KEY = "CUK5YODHVAZHFBM6KESZO1J4"


class SaleTestCase(unittest.TestCase):
    def setUp(self):
        self.sprw = sparrowone.Connection(M_KEY)

    def test_simple_sale(self):
        card = sparrowone.CardInfo(
            number="4111111111111111",
            expiration="1019",
            cvv="999"
        )
        resp = self.sprw.sale(10.0, card)
        self.assertEqual(resp["textresponse"], "SUCCESS")

    def test_simple_sale_decline(self):
        card = sparrowone.CardInfo(
            number="4111111111111111",
            expiration="1019",
            cvv="999"
        )
        with self.assertRaises(sparrowone.SparrowAPIError):
            self.sprw.sale(0.01, card)

    def test_simple_sale_invalid_card(self):
        card = sparrowone.CardInfo(
            number="1234567890123456",
            expiration="1019",
            cvv="999"
        )
        with self.assertRaises(sparrowone.SparrowAPIError):
            self.sprw.sale(9.95, card)

    def test_simple_sale_avs_mismatch(self):
        sale = sparrowone.SaleInfo(
            amount=0.01,  # XXX
            billing_contact=sparrowone.Contact(
                address1="888",
                zip="77777",
            ),
        )

        card = sparrowone.CardInfo(
            number="4111111111111111",
            expiration="1019",
            cvv="999",
        )

        with self.assertRaises(sparrowone.SparrowAPIError) as cm:
            self.sprw.sale(sale, card)

        self.assertEqual(cm.exception.data["textresponse"], "DECLINE")

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

        resp = self.sprw.sale(sale, card)
        self.assertEqual(resp["textresponse"], "SUCCESS")
    
    def test_passenger_sale(self):
        sale = sparrowone.SaleInfo(
            amount=9.95,
            airportcode1="LAS",
            airportcode2="CDG",
            airportcode3="IAD",
            airportcode4="CPH",
            ticketnumber=1234567890,
            flightdatecoupon1="01/31/2017",
            flightdeparturetimecoupon1="23:59",
            addressverificationcode="A",
            approvalcode=123456,
            transactionid=1234567890,
            authcharindicator="A",
            referencenumber=123456789012,
            validationcode=1234,
            authresponsecode="AB",
        )

        card = sparrowone.CardInfo(
            number="4111111111111111",
            expiration="1019",
            cvv="999",
        )

        resp = self.sprw.sale(sale, card)
        self.assertEqual(resp["textresponse"], "SUCCESS")
