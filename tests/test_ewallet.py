import unittest

import sparrowone

EWALLET_M_KEY = "1W53QL0TJLIERXHIQKRXJRTK"


class EWalletTestCase(unittest.TestCase):
    def setUp(self):
        self.sprw = sparrowone.Connection(EWALLET_M_KEY)

    def test_e_wallet_simple_credit(self):
        ewallet = sparrowone.EWallet("user@example.com")
        resp = self.sprw.credit(9.95, ewallet)
        self.assertEqual(resp["textresponse"], "Successful")
