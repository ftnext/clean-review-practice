import abc
from typing import TypedDict


class ProposalEntity(TypedDict):
    title: str
    description: str


class ProposalDriver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_all(self):
        raise NotImplementedError
