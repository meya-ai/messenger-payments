from meya import Component


class StockCheck(Component):

    def start(self):
        # TODO: make an API call here to your backend
        # to determine if you can fulfill the order
        success = True
        data = {"success": success}
        return self.respond(data=data)
