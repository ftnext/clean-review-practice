from unittest import TestCase
from unittest.mock import MagicMock, call, patch

from reviewlogic.domains import proposal
from reviewlogic.drivers import proposal_driver
from reviewlogic.gateways import proposal_gateway
from reviewlogic.value_objects import ProposalId


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

    @patch("reviewlogic.domains.proposal.Proposal.from_entity")
    def test_find_by_when_found(self, from_entity):
        proposal_id = ProposalId(6)
        entity = proposal_driver.ProposalEntity(
            id=6, title="Found", description="The found one."
        )
        self.mock_driver.find_by_id.return_value = entity
        found_proposal = proposal.Proposal(
            ProposalId(6), "Found", "The found one."
        )
        from_entity.return_value = found_proposal

        actual = self.gateway.find_by(proposal_id)

        self.assertEqual(actual, found_proposal)
        self.mock_driver.find_by_id.assert_called_once_with(6)
        from_entity.assert_called_once_with(entity)

    def test_find_by_when_not_found(self):
        self.mock_driver.find_by_id.side_effect = (
            proposal_driver.ProposalNotFound
        )
        proposal_id = ProposalId(10008)

        with self.assertRaises(ValueError) as cm:
            self.gateway.find_by(proposal_id)

        self.assertEqual(str(cm.exception), "Id 10008 is not in proposal list")
        self.mock_driver.find_by_id.assert_called_once_with(10008)
