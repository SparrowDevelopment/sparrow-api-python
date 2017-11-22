def plan_factory(sprw):
    class Plan(object):
        def __init__(self):
            raise TypeError("This class can't be instantiated")
        
        @classmethod
        def create(cls, data):
            return sprw._call("addplan", **data)

        @classmethod
        def get(cls, id):
            return sprw._call("getinvoice", token=id)
        
        @classmethod
        def update(cls, token, data):
            return sprw._call("updateplan", token=token, **data)
        
        @classmethod
        def delete(cls, token):
            return sprw._call("deleteplan", token=token)
        
        @classmethod
        def assign(cls, token, customer_token, payment_token=None):
            return sprw._call("assignplan",
                              plantoken=token,
                              customertoken=customer_token,
                              paymenttoken=payment_token)
    
    return Plan