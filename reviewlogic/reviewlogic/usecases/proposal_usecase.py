class ProposalUseCase:
    def __init__(self, port):
        self.port = port

    def list(self):
        raise NotImplementedError
