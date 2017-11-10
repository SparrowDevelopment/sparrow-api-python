from .models import SaleInfo

def invoice_factory(sprw):
    class Invoice(object):
        def __init__(self):
            raise TypeError("This class can't be instantiated")
        
        @classmethod
        def create(cls, data):
            return sprw._call("createmerchantinvoice", **data)

        @classmethod
        def get(cls, id):
            return sprw._call("getinvoice", invoicenumber=id)
        
        @classmethod
        def update(cls, id, data):
            return sprw._call("updateinvoice", invoicenumber=id, **data)
        
        @classmethod
        def cancel(cls, id, reason, by_customer=False):
            method = "cancelinvoicebycustomer" if by_customer else "cancelinvoice"
            return sprw._call(method,
                              invoicenumber=id,
                              invoicestatusreason=reason)
        
        @classmethod
        def pay(cls, id, payment_method):
            if "invoice.pay" not in payment_method.allowed_methods:
                raise TypeError("This payment method doesn't support invoice.pay()")

            return sprw._call("payinvoice", invoicenumber=id, **payment_method)
    
    return Invoice