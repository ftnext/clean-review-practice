import abc
from typing import TypedDict


class ReviewEntity(TypedDict):
    user_id: int
    proposal_id: int
    score: str
    comment: str


class ReviewDriver(abc.ABC):
    @abc.abstractmethod
    def save(self, entity):
        raise NotImplementedError
