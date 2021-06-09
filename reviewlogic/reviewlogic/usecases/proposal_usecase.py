class ProposalUseCase:
    def __init__(self, port):
        self.port = port

    def list(self):
        return self.port.list()

    def find_by(self, proposal_id):
        raise NotImplementedError
