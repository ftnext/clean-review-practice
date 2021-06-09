from unittest import TestCase
from unittest.mock import MagicMock, call, patch

from reviewlogic.domains import proposal
from reviewlogic.drivers import proposal_driver
from reviewlogic.gateways import proposal_gateway


class ProposalGatewayTestCase(TestCase):
    def setUp(self):
        self.mock_driver = MagicMock(proposal_driver.ProposalDriver)
        self.gateway = proposal_gateway.ProposalGateway(self.mock_driver)

    @patch("reviewlogic.domains.proposal.Proposal.from_entity")
    def test_list(self, from_entity):
        entity1 = proposal_driver.ProposalEntity(
            id=1, title="Title 1", description="Description 1"
        )
        entity2 = proposal_driver.ProposalEntity(
            id=2, title="Title 2", description="Description 2"
        )
        self.mock_driver.find_all.return_value = [entity1, entity2]
        proposal1 = MagicMock(spec=proposal.Proposal)
        proposal2 = MagicMock(spec=proposal.Proposal)
        from_entity.side_effect = (proposal1, proposal2)
        expected = proposal.Proposals([proposal1, proposal2])

        actual = self.gateway.list()

        self.assertEqual(actual, expected)
        self.mock_driver.find_all.assert_called_once_with()
        from_entity.assert_has_calls([call(entity1), call(entity2)])
