import abc
from typing import TypedDict


class ReviewEntity(TypedDict, total=False):
    id: int
    user_id: int
    proposal_id: int
    score: str
    comment: str


class ReviewDriver(abc.ABC):
    @abc.abstractmethod
    def save(self, entity):
        raise NotImplementedError


class InMemoryReviewDriver(ReviewDriver):
    review_entities: list[ReviewEntity] = []

    def save(self, entity: ReviewEntity) -> int:
        if "id" not in entity:
            entity["id"] = len(self.review_entities) + 1
        self.review_entities.append(entity)
        return entity["id"]
