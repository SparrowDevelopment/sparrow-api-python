import unittest

import sparrowone

ACH_M_KEY = "RZOZ2AMMYF7GX2VF1L05WW1G"


class ACHTestCase(unittest.TestCase):
    def setUp(self):
        self.sprw = sparrowone.Connection(ACH_M_KEY)

    def test_simple_ach(self):
        sale = sparrowone.SaleInfo(
            amount=9.95,
            billing_contact=sparrowone.Contact(
                first_name="Gillian",
                last_name="Fenimore",
            ),
        )
        ach_account = sparrowone.ACHInfo(
            bank_name="First Test Bank",
            routing="110000000",
            account="1234567890123",
            type="checking",
            subtype="personal",
        )
        resp = self.sprw.sale(sale, ach_account)
        self.assertEqual(resp["textresponse"], "SUCCESS")

    def test_simple_ach_refund(self):
        sale = sparrowone.SaleInfo(
            amount=9.95,
            billing_contact=sparrowone.Contact(
                first_name="Gillian",
                last_name="Fenimore",
            ),
        )
        ach_account = sparrowone.ACHInfo(
            bank_name="First Test Bank",
            routing="110000000",
            account="1234567890123",
            type="checking",
            subtype="personal",
        )
        resp = self.sprw.sale(sale, ach_account)
        self.assertEqual(resp["textresponse"], "SUCCESS")

        try:
            resp2 = self.sprw.refund(resp["transid"], 9.95,
                                     ach_account=ach_account)
        except sparrowone.SparrowAPIError as e:
            # XXX bad test?
            self.assertIn("Transaction not found", e.data["textresponse"])
        else:
            self.assertEqual(resp["textresponse"], "SUCCESS")

    def test_simple_ach_credit(self):
        credit = sparrowone.SaleInfo(
            amount=9.95,
            billing_contact=sparrowone.Contact(
                first_name="Julianne",
                last_name="Stingray",
            ),
        )
        ach_account = sparrowone.ACHInfo(
            bank_name="First Test Bank",
            routing="110000000",
            account="1234567890123",
            type="checking",
            subtype="personal",
        )
        resp = self.sprw.credit(credit, ach_account)
        self.assertEqual(resp["textresponse"], "SUCCESS")

    def test_advanced_ach(self):
        sale = sparrowone.SaleInfo(
            amount=9.95,
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
        ach_account = sparrowone.ACHInfo(
            bank_name="First Test Bank",
            routing="110000000",
            account="1234567890123",
            type="checking",
            subtype="personal",
        )
        resp = self.sprw.sale(sale, ach_account)
        self.assertEqual(resp["textresponse"], "SUCCESS")
