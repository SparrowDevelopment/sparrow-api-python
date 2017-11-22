import unittest
import uuid

import sparrowone


M_KEY = "CUK5YODHVAZHFBM6KESZO1J4"
ACH_M_KEY = "RZOZ2AMMYF7GX2VF1L05WW1G"

class PlansCreateTestCase(unittest.TestCase):
    def setUp(self):
        self.sprw = sparrowone.Connection(M_KEY)

    def test_creating_a_payment_plan(self):
        resp = self.sprw.plans.create(data=dict(
            mkey=M_KEY,
            planname="PaymentPlan1",
            plandesc="1st Payment Plan",
            startdate="01/31/2017",
            defaultachmkey=ACH_M_KEY,
            defaultcreditcardmkey=M_KEY,
            defaultcheckmkey=M_KEY,
            defaultstarcardmkey=M_KEY,
            defaulte_walletmkey=M_KEY,
            sequence_1=1,
            amount_1=1.99,
            scheduletype_1="custom",
            scheduleday_1=7,
            duration_1=365,
            productid_1="abc",
            description_1="Weekly",
            sequence_2=2,
            amount_2=2.99,
            scheduletype_2="monthly",
            scheduleday_2=1,
            duration_2=-1,
            productid_2="123",
            description_2="Monthly",
            notifyfailures=False,
            userecycling=True,
            retrycount=2,
            retrytype="daily",
            retryperiod=1,
            autocreateclientaccounts=True,
        ))
        self.assertEqual(resp["textresponse"], "SUCCESS")


class PlansTestCase(unittest.TestCase):
    def setUp(self):
        self.sprw = sparrowone.Connection(M_KEY)
        resp = self.sprw.plans.create(data=dict(
            mkey=M_KEY,
            planname="PaymentPlan1",
            plandesc="1st Payment Plan",
            startdate="01/31/2017",
            defaultachmkey=ACH_M_KEY,
            defaultcreditcardmkey=M_KEY,
            defaultcheckmkey=M_KEY,
            defaultstarcardmkey=M_KEY,
            defaulte_walletmkey=M_KEY,
            sequence_1=1,
            amount_1=1.99,
            scheduletype_1="custom",
            scheduleday_1=7,
            duration_1=365,
            productid_1="abc",
            description_1="Weekly",
            sequence_2=2,
            amount_2=2.99,
            scheduletype_2="monthly",
            scheduleday_2=1,
            duration_2=-1,
            productid_2="123",
            description_2="Monthly",
            notifyfailures=False,
            userecycling=True,
            retrycount=2,
            retrytype="daily",
            retryperiod=1,
            autocreateclientaccounts=True,
        ))
        self.plan_token = resp["plantoken"]
        resp = self.sprw.customers.create(data=dict(
            firstname="John",
            lastname="Doe",
            username="py_test_user_%r" % uuid.uuid1(),
            email="john@example.com",
            paytype_1="creditcard",
            cardnum_1="4111111111111111",
            cardexp_1="1019"
        ))
        self.customer_token = resp["customertoken"]
        self.payment_token = resp["paymenttoken_1"]

    def test_updating_a_payment_plan(self):
        resp = self.sprw.plans.update(self.plan_token, data=dict(
            planname="PaymentPlan1Updated",
        ))
        self.assertEqual(resp["textresponse"], "SUCCESS")
    
    def test_deleting_a_plan(self):
        resp = self.sprw.plans.delete(self.plan_token)
        self.assertEqual(resp["textresponse"], "SUCCESS")
    
    def test_assigning_a_payment_plan_to_a_customer(self):
        resp = self.sprw.plans.assign(self.plan_token,
                                      self.customer_token,
                                      self.payment_token)
        self.assertEqual(resp["textresponse"], "Success")  # ???
