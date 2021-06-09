from reviewlogic.domains import review


class ReviewUseCase:
    def __init__(self, port) -> None:
        self.port = port

    def save(self, user_id, proposal_id, score, comment):
        review_object = review.Review(user_id, proposal_id, score, comment)
        return self.port.save(review_object)
