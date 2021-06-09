from unittest import TestCase
from unittest.mock import MagicMock

from reviewlogic.domains import proposal
from reviewlogic.drivers import proposal_driver
from reviewlogic.gateways import proposal_gateway


class ProposalGatewayTestCase(TestCase):
    def test_list(self):
        mock_driver = MagicMock(proposal_driver.ProposalDriver)
        gateway = proposal_gateway.ProposalGateway(mock_driver)
        expected = proposal.Proposals(
            [
                proposal.Proposal("Title 1", "Description 1"),
                proposal.Proposal("Title 2", "Description 2"),
            ]
        )
        mock_driver.find_all.return_value = [
            proposal_driver.ProposalEntity(
                title="Title 1", description="Description 1"
            ),
            proposal_driver.ProposalEntity(
                title="Title 2", description="Description 2"
            ),
        ]

        actual = gateway.list()

        self.assertEqual(actual, expected)
        mock_driver.find_all.assert_called_once_with()
