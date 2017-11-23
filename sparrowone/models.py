class PaymentMethod(dict):
    pass


class CardInfo(PaymentMethod):
    allowed_methods = ["sale", "auth", "offline", "invoice.pay"]

    def __init__(self, number, expiration, cvv=None):
        """
        A PaymentMethod representing a credit or debit card.
        """
        self.update({
            "cardnum": number,
            "cardexp": expiration,
            "cvv": cvv,
        })


class FiservCard(PaymentMethod):
    allowed_methods = ["sale"]

    def __init__(self, number, expiration, cvv=None):
        """
        A PaymentMethod representing a credit or debit card
        used through Fiserv.
        """
        self.update({
            "cardnum": number,
            "cardexp": expiration,
            "cvv": cvv,
        })


class MilitaryStarCard(PaymentMethod):
    allowed_methods = ["sale", "auth", "invoice.pay"]

    def __init__(self, number, expiration, cid):
        """
        A PaymentMethod representing a Military Star card.
        """
        self.update({
            "cardnum": number,
            "cardexp": expiration,
            "CID": cid,
        })


class ACHInfo(PaymentMethod):
    allowed_methods = ["sale", "credit", "invoice.pay"]

    def __init__(self, bank_name, routing, account, type, subtype,
                 first_name=None, last_name=None, company=None):
        """
        A PaymentMethod representing an ACH account.
        """
        self.update({
            "bankname": bank_name,
            "routing": routing,
            "account": account,
            "achaccounttype": type,
            "achaccountsubtype": subtype,
        })

        if first_name is not None:
            self["firstname"] = first_name
        if last_name is not None:
            self["lastname"] = last_name
        if company is not None:
            self["company"] = company


class EWallet(PaymentMethod):
    allowed_methods = ["credit"]

    def __init__(self, account, type="PayPal"):
        """
        A PaymentMethod representing an eWallet (i. e. PayPal) account.
        """
        self.update({
            "ewalletaccount": account,
            "ewallet_type": type,
        })


class Contact(dict):
    def __init__(self, first_name=None, last_name=None, company=None,
                 address1=None, address2=None, city=None, state=None,
                 zip=None, country=None, phone=None, fax=None, email=None):
        self.update({
            "firstname": first_name,
            "lastname": last_name,
            "company": company,
            "address1": address1,
            "address2": address2,
            "city": city,
            "state": state,
            "zip": zip,
            "country": country,
            "phone": phone,
            "fax": fax,
            "email": email,
        })


class Product(dict):
    def __init__(self, skunumber=None, description=None,
                 amount=None, quantity=None):
        self.update({
            "skunumber": skunumber,
            "description": description,
            "amount": amount,
            "quantity": quantity,
        })


class Option(dict):
    def __init__(self, type=None, value=None, percentage=None):
        self.update({
            "type": type,
            "value": value,
            "percentage": percentage,
        })


class SaleInfo(dict):
    def __init__(self, amount, currency=None,
                 ip_addr=None, order_id=None, order_desc=None,
                 tax=None, shipping_cost=None, po_number=None,
                 billing_contact=None, ship_to=None,
                 products=[], options=[], **kwargs):
        self.update({
            "amount": amount,
            "currency": currency,
            "cardipaddress": ip_addr,
            "orderid": order_id,
            "orderdesc": order_desc,
            "tax": tax,
            "shipamount": shipping_cost,
            "ponumber": po_number,
        })

        if billing_contact is not None:
            self.update(billing_contact)

        if ship_to is not None:
            self.update({
                "ship" + key: value
                for key, value in ship_to.items()
            })
            # XXX: the only parameter not present on shipping address is
            # "fax", let's ignore it for now
            self.pop("shipfax", None)

        for i, product in enumerate(products):
            self.update({
                "skunumber_%i" % i: product.get("skunumber"),
                "description_%i" % i: product.get("description"),
                "amount_%i" % i: product.get("amount"),
                "quantity_%i" % i: product.get("quantity"),
            })

        for i, option in enumerate(options):
            self.update({
                "opt_amount_type_%i" % i: option.get("type"),
                "opt_amount_value_%i" % i: option.get("value"),
                "opt_amount_percentage_%i" % i: option.get("percentage"),
            })
        
        self.update(kwargs)
