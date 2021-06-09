from reviewlogic.domains import proposal


class ProposalGateway:
    def __init__(self, driver):
        self.driver = driver

    def list(self):
        entities = self.driver.find_all()
        proposals = [
            proposal.Proposal(entity["title"], entity["description"])
            for entity in entities
        ]
        return proposal.Proposals(proposals)
