from reviewlogic.domains import review
from reviewlogic.gateways import review_gateway as rg
from reviewlogic.value_objects import ProposalId, ReviewId, UserId


class ReviewUseCase:
    def __init__(self, port: rg.ReviewPort) -> None:
        self.port = port

    def save(
        self,
        user_id: UserId,
        proposal_id: ProposalId,
        score: review.ScoreEnum,
        comment: review.Comment,
    ) -> ReviewId:
        review_object = review.Review(user_id, proposal_id, score, comment)
        return self.port.save(review_object)
