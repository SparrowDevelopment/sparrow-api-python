import unittest
import uuid

import sparrowone


M_KEY = "CUK5YODHVAZHFBM6KESZO1J4"

class PlansCreateTestCase(unittest.TestCase):
    def setUp(self):
        self.sprw = sparrowone.Connection(M_KEY)

    def test_creating_a_payment_plan(self):
        resp = self.sprw.plans.create(data=dict(
            mkey=M_KEY,
            planname="PaymentPlan1",
            plandesc="1st Payment Plan",
            startdate="01/31/2017",
            sequence_1=1,
            amount_1=1.99,
            scheduletype_1="custom",
            scheduleday_1=7,
            duration_1=365,
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
            sequence_1=1,
            amount_1=1.99,
            scheduletype_1="custom",
            scheduleday_1=7,
            duration_1=365,
        ))
        self.plan_token = resp["plantoken"]
        resp = self.sprw.customers.create(data=dict(
            firstname="John",
            lastname="Doe",
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

    def test_update_payment_plan_assignment(self):
        resp = self.sprw.plans.assign(
            self.plan_token,
            self.customer_token,
            self.payment_token
        )
        assignment_token = resp["assignmenttoken"]

        resp = self.sprw.plans.update_assignment(
            assignment_token,
            startdate="1/1/2018"
        )
        self.assertEqual(resp["textresponse"], "Success")  # ???
