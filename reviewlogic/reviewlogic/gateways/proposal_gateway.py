import abc

from reviewlogic.domains import proposal
from reviewlogic.drivers.proposal_driver import ProposalNotFound


class ProposalPort(metaclass=abc.ABCMeta):
    def __init__(self, driver):
        self.driver = driver

    @abc.abstractmethod
    def list(self):
        raise NotImplementedError

    @abc.abstractmethod
    def find_by(self, proposal_id):
        raise NotImplementedError


class ProposalGateway(ProposalPort):
    def list(self):
        entities = self.driver.find_all()
        proposals = [
            proposal.Proposal.from_entity(entity) for entity in entities
        ]
        return proposal.Proposals(proposals)

    def find_by(self, proposal_id):
        try:
            entity = self.driver.find_by_id(proposal_id.value)
        except ProposalNotFound:
            message = f"Id {proposal_id} is not in proposal list"
            raise ValueError(message)
        return proposal.Proposal.from_entity(entity)
