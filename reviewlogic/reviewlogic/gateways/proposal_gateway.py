import abc

from reviewlogic.domains import proposal
from reviewlogic.value_objects import ProposalId


class ProposalPort(metaclass=abc.ABCMeta):
    def __init__(self, driver):
        self.driver = driver

    @abc.abstractmethod
    def list(self):
        raise NotImplementedError


class ProposalGateway(ProposalPort):
    def list(self):
        entities = self.driver.find_all()
        proposals = [
            proposal.Proposal(
                ProposalId(entity["id"]),
                entity["title"],
                entity["description"],
            )
            for entity in entities
        ]
        return proposal.Proposals(proposals)
