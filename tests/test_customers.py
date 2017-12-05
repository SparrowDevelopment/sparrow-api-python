import uuid
import unittest

import sparrowone


M_KEY = "CUK5YODHVAZHFBM6KESZO1J4"
ACH_M_KEY = "RZOZ2AMMYF7GX2VF1L05WW1G"

class CustomersCreateTestCase(unittest.TestCase):
    def setUp(self):
        self.sprw = sparrowone.Connection(M_KEY)

    def test_adding_a_customer(self):
        resp = self.sprw.customers.create(data=dict(
            firstname="John",
            lastname="Doe",
            note="Customer Note",
            address1="16100 N 71st Street",
            address2="Suite 170",
            city="Scottsdale",
            state="AZ",
            zip="85254",
            country="US",
            email="john@norepy.com",
            shipfirstname="Jane",
            shiplastname="Doe",
            shipcompany="Sparrow Two",
            shipaddress1="16100 N 72nd Street",
            shipaddress2="Suite 171",
            shipcity="Pheonix",
            shipstate="AZ",
            shipzip="85004",
            shipcountry="US",
            shipphone="6025551234",
            shipemail="jane@noreply.com",
            username=str(uuid.uuid1()),
            password="Password123",
            clientuseremail="john@norepy.com",
            paytype_1="creditcard",
            firstname_1="John",
            lastname_1="Doe",
            address1_1="123 Main Street",
            address2_1="Suite 1",
            city_1="Pheonix",
            state_1="AZ",
            zip_1="85111",
            country_1="US",
            phone_1="6025551234",
            email_1="john@norepy.com",
            cardnum_1="4111111111111111",
            cardexp_1="1019",
            paytype_2="check",
            firstname_2="John",
            lastname_2="Doe",
            address1_2="321 1st Street",
            address2_2="Suite 2",
            city_2="Scottsdale",
            state_2="AZ",
            zip_2="85222",
            country_2="US",
            phone_2="6025554321",
            email_2="jane@noreploy.com",
            cardnum_2="4111111111111111",
            cardexp_2="1019",
            bankname_2="First Test Bank",
            routing_2="110000000",
            account_2="1234567890123",
            achaccounttype_2="personal",
            payno_2="2",
        ))
        self.assertIn("successfully created", resp["textresponse"])

    def test_add_customer_credit_card_simple(self):
        resp = self.sprw.customers.create(data=dict(
            firstname="John",
            lastname="Doe",
            paytype_1="creditcard",
            cardnum_1="4111111111111111",
            cardexp_1="1019"
        ))
        self.assertIn("successfully created", resp["textresponse"])

    def test_add_customer_e_wallet_simple(self):
        resp = self.sprw.customers.create(data=dict(
            firstname="John",
            lastname="Doe",
            paytype_1="ewallet",
            ewallettype_1="paypal",
            ewalletaccount_1="user@example.com"
        ))
        self.assertIn("successfully created", resp["textresponse"])


class CustomersACHTestCase(unittest.TestCase):
    def setUp(self):
        self.sprw = sparrowone.Connection(ACH_M_KEY)

    def test_add_customer_ach_simple(self):
        resp = self.sprw.customers.create(data=dict(
            firstname="John",
            lastname="Doe",
            paytype_1="ach",
            bankname_1="First Test Bank",
            routing_1=110000000,
            account_1=1234567890123,
            achaccounttype_1="checking",
            achaccountsubtype_1="personal"
        ))
        self.assertIn("successfully created", resp["textresponse"])


class CustomersTestCase(unittest.TestCase):
    def setUp(self):
        self.sprw = sparrowone.Connection(M_KEY)
        resp = self.sprw.customers.create(data=dict(
            firstname="John",
            lastname="Doe",
            paytype_1="creditcard",
            cardnum_1="4111111111111111",
            cardexp_1="1019"
        ))
        self.customer_token = resp["customertoken"]
        self.payment_token = resp["paymenttoken_1"]
        
    def test_add_payment_type(self):
        resp = self.sprw.customers.add_payment_type(
            self.customer_token,
            data={
                "paytype": "creditcard",
                "cardnum": "4111111111111112",
                "cardexp": "1019",
            }
        )
        self.assertIn("successfully updated", resp["textresponse"])

    def test_update_payment_type(self):
        resp = self.sprw.customers.update_payment_type(
            self.customer_token,
            self.payment_token,
            data={
                "cardnum": "4111111111111112",
            }
        )
        self.assertIn("successfully updated", resp["textresponse"])
    
    def test_delete_payment_type(self):
        resp = self.sprw.customers.delete_payment_type(self.customer_token,
                                                       self.payment_token)
        self.assertIn("successfully updated", resp["textresponse"])

    def test_delete_data_vault_customer(self):
        resp = self.sprw.customers.delete(self.customer_token)
        self.assertEqual(resp["textresponse"], "SUCCESS")
    
    def test_decrypting_custom_fields(self):
        resp = self.sprw.customers.decrypt_field(
            self.customer_token,
            self.payment_token,
            field_name="customField1"
        )
        self.assertEqual(resp["textresponse"], "SUCCESS")
