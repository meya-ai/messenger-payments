from meya import Component


class ShippingOptions(Component):

    def start(self):
        address = self.properties.get("shipping_address", {})
        fedex_amount = 16.99
        if address.get("state", "") == "CA":
            fedex_amount = 4.99

        data = {
            "shipping": [
                {
                    "option_id": "1",
                    "option_title": "Fedex",
                    "price_list": [
                        {
                            "label": "Shipping",
                            "amount": fedex_amount
                        },
                        {
                            "label": "Tax",
                            "amount": 11.74
                        }
                    ]
                },
                {
                    "option_id": "2",
                    "option_title": "USPS",
                    "price_list": [
                        {
                            "label": "Shipping",
                            "amount": 2.99
                        },
                        {
                            "label": "Tax",
                            "amount": 10.32
                        }
                    ]
                }
            ]
        }
        return self.respond(data=data)
