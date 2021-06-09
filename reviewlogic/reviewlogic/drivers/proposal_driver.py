import abc
from typing import TypedDict


class ProposalNotFound(Exception):
    pass


class ProposalEntity(TypedDict):
    id: int
    title: str
    description: str


class ProposalDriver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_all(self):
        raise NotImplementedError

    @abc.abstractmethod
    def find_by_id(self, id):
        raise NotImplementedError


class InMemoryProposalDriver(ProposalDriver):
    proposal_entities = [
        ProposalEntity(
            id=1, title="Pythonのspamについて", description="spam ham egg"
        ),
        ProposalEntity(id=2, title="熱のこもったプロポーザル", description="とにかく熱い本文"),
    ]

    def find_all(self):
        return self.proposal_entities
