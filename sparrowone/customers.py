def customer_factory(sprw):
    class Customer(object):
        def __init__(self):
            raise TypeError("This class can't be instantiated")

        @classmethod
        def create(cls, data):
            return sprw._call("addcustomer", **data)

        @classmethod
        def get(cls, token):
            return sprw._call("getcustomer", token=token)

        @classmethod
        def update(cls, token, data):
            return sprw._call("updatecustomer", token=token, **data)

        @classmethod
        def delete_payment_type(cls, token, payment_token):
            return sprw._call("updatecustomer", token=token,
                              operationtype_1="deletepaytype",
                              token_1=payment_token)

        @classmethod
        def delete(cls, token):
            return sprw._call("deletecustomer", token=token)

    return Customer
