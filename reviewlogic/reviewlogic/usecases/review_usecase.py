class ReviewUseCase:
    def __init__(self, port) -> None:
        self.port = port

    def save(self, user_id, proposal_id, score, comment):
        raise NotImplementedError
