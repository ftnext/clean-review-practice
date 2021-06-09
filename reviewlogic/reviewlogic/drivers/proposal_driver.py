import abc
from typing import TypedDict


class ProposalEntity(TypedDict):
    title: str
    description: str


class ProposalDriver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_all(self):
        raise NotImplementedError


class InMemoryProposalDriver(ProposalDriver):
    proposal_entities = [
        ProposalEntity(title="Pythonのspamについて", description="spam ham egg"),
        ProposalEntity(title="熱のこもったプロポーザル", description="とにかく熱い本文"),
    ]

    def find_all(self):
        return self.proposal_entities
