import abc

import reviewlogic.domains.review as r
from reviewlogic.drivers.review_driver import ReviewEntity
from reviewlogic.value_objects import ReviewId


class ReviewPort(abc.ABC):
    def __init__(self, driver):
        self.driver = driver

    @abc.abstractmethod
    def save(self, review: r.Review):
        raise NotImplementedError


class ReviewGateway(ReviewPort):
    def save(self, review: r.Review) -> ReviewId:
        entity = ReviewEntity(
            user_id=review.user_id.value,
            proposal_id=review.proposal_id.value,
            score=review.score.value,
            comment=review.comment,
        )
        return ReviewId(self.driver.save(entity))
