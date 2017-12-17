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
        def add_payment_type(cls, token, data):
            data = {
                ("%s_1" % k): v
                for (k, v) in data.items()
            }
            return sprw._call("updatecustomer", token=token,
                              operationtype_1="addpaytype",
                              **data)
        
        @classmethod
        def get_payment_type(cls, payment_token):
            return sprw._call("getcustomer", token=payment_token)
        
        @classmethod
        def update_payment_type(cls, token, payment_token, data):
            data = {
                ("%s_1" % k): v
                for (k, v) in data.items()
            }
            return sprw._call("updatecustomer", token=token,
                              operationtype_1="updatepaytype",
                              token_1=payment_token,
                              **data)
        
        @classmethod
        def delete_payment_type(cls, token, payment_token):
            return sprw._call("updatecustomer", token=token,
                              operationtype_1="deletepaytype",
                              token_1=payment_token)

        @classmethod
        def delete(cls, token):
            return sprw._call("deletecustomer", token=token)
        
        @classmethod
        def decrypt_field(cls, token, payment_token, field_name):
            return sprw._call("decrypt", customertoken=token,
                              paymenttoken=payment_token,
                              fieldname=field_name)

    return Customer
