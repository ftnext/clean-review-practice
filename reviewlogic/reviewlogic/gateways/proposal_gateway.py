class ProposalGateway:
    def __init__(self, driver):
        self.driver = driver

    def list(self):
        raise NotImplementedError
