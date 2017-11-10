import unittest

import sparrowone


M_KEY = "CUK5YODHVAZHFBM6KESZO1J4"
ACH_M_KEY = "RZOZ2AMMYF7GX2VF1L05WW1G"
CUSTOMER_TOKEN = "TL2X2O9SD3HTZOU9"  # TEMP

class InvoicesCreateTestCase(unittest.TestCase):
    def setUp(self):
        self.sprw = sparrowone.Connection(M_KEY)

    def test_creating_an_invoice(self):
        resp = self.sprw.invoices.create(data=dict(
            customertoken=CUSTOMER_TOKEN,
            invoicedate="12/01/2017",
            currency="USD",
            invoicestatus="draft",
            invoicesource="DataVault",
            invoiceamount="10.00",
            invoiceitemsku_1="123",
            invoiceitemsku_2="456",
            invoiceitemdescription_1="Widget 1",
            invoiceitemdescription_2="Widget 2",
            invoiceitemprice_1="2.00",
            invoiceitemprice_2="4.00",
            invoiceitemquantity_1="1",
            invoiceitemquantity_2="2"
        ))
        self.assertEqual(resp["textresponse"], "invoice has been successfully created")

    def test_creating_active_invoice(self):
        resp = self.sprw.invoices.create(data=dict(
            customertoken=CUSTOMER_TOKEN,
            invoicedate="12/01/2017",
            currency="USD",
            invoicestatus="active",
            invoicesource="DataVault",
            invoiceamount="10.00",
            invoiceitemsku_1="123",
            invoiceitemsku_2="456",
            invoiceitemdescription_1="Widget 1",
            invoiceitemdescription_2="Widget 2",
            invoiceitemprice_1="2.00",
            invoiceitemprice_2="4.00",
            invoiceitemquantity_1="1",
            invoiceitemquantity_2="2"
        ))
        self.assertEqual(resp["textresponse"], "invoice has been successfully created")


class InvoicesTestCase(unittest.TestCase):
    def setUp(self):
        self.sprw = sparrowone.Connection(M_KEY)
        resp = self.sprw.invoices.create(data=dict(
            customertoken=CUSTOMER_TOKEN,
            invoicedate="12/01/2017",
            currency="USD",
            invoicestatus="draft",
            invoicesource="DataVault",
            invoiceamount="10.00",
            invoiceitemsku_1="123",
            invoiceitemsku_2="456",
            invoiceitemdescription_1="Widget 1",
            invoiceitemdescription_2="Widget 2",
            invoiceitemprice_1="2.00",
            invoiceitemprice_2="4.00",
            invoiceitemquantity_1="1",
            invoiceitemquantity_2="2"
        ))
        self.invoice_id = resp["invoicenumber"]

    def test_update_invoice(self):
        resp = self.sprw.invoices.update(self.invoice_id, data=dict(
            invoicedate="12/15/2017",
            invoiceamount="15.00",
            invoicestatus="active",
        ))
        self.assertEqual(resp["textresponse"], "Invoice has been successfully updated")

    def test_cancel_invoice(self):
        resp = self.sprw.invoices.cancel(self.invoice_id, "test")
        self.assertEqual(resp["textresponse"], "invoice has been successfully canceled")

    def test_cancel_invoice_by_customer(self):
        resp = self.sprw.invoices.cancel(self.invoice_id, "test", by_customer=True)
        self.assertEqual(resp["textresponse"], "invoice has been successfully canceled")

    def test_paying_an_invoice_with_a_credit_card(self):
        self.sprw.invoices.update(self.invoice_id, data=dict(
            invoicestatus="active",
        ))

        card = sparrowone.CardInfo(
            number="4111111111111111",
            expiration="1019",
            cvv="999"
        )
        resp = self.sprw.invoices.pay(self.invoice_id, card)
        self.assertEqual(resp["textresponse"], "Invoice has been successfully paid")


class InvoicesACHTestCase(unittest.TestCase):
    def setUp(self):
        self.sprw = sparrowone.Connection(ACH_M_KEY)
        resp = self.sprw.invoices.create(data=dict(
            customertoken=CUSTOMER_TOKEN,
            invoicedate="12/01/2017",
            currency="USD",
            invoicestatus="active",
            invoicesource="DataVault",
            invoiceamount="10.00",
            invoiceitemsku_1="123",
            invoiceitemsku_2="456",
            invoiceitemdescription_1="Widget 1",
            invoiceitemdescription_2="Widget 2",
            invoiceitemprice_1="2.00",
            invoiceitemprice_2="4.00",
            invoiceitemquantity_1="1",
            invoiceitemquantity_2="2"
        ))
        self.invoice_id = resp["invoicenumber"]

    def test_paying_an_invoice_with_a_bank_account(self):
        ach_account = sparrowone.ACHInfo(
            bank_name="First Test Bank",
            routing="110000000",
            account="1234567890123",
            type="checking",
            subtype="personal",
            first_name="Alma",
            last_name="Armas"
        )
        resp = self.sprw.invoices.pay(self.invoice_id, ach_account)
        self.assertEqual(resp["textresponse"], "Invoice has been successfully paid")
