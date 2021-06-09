import abc

from reviewlogic.domains import proposal


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
        entity = self.driver.find_by_id(proposal_id.value)
        return proposal.Proposal.from_entity(entity)
