from unittest import TestCase
from unittest.mock import MagicMock

from reviewlogic.gateways import proposal_gateway
from reviewlogic.usecases import proposal_usecase
from reviewlogic.value_objects import ProposalId


class ProposalUseCaseTestCase(TestCase):
    def setUp(self):
        self.mock_port = MagicMock(spec=proposal_gateway.ProposalPort)
        self.usecase = proposal_usecase.ProposalUseCase(self.mock_port)

    def test_list(self):
        actual = self.usecase.list()

        self.assertEqual(actual, self.mock_port.list.return_value)
        self.mock_port.list.assert_called_once_with()

    def test_find_by(self):
        proposal_id = ProposalId(5)

        actual = self.usecase.find_by(proposal_id)

        self.assertEqual(actual, self.mock_port.find_by.return_value)
        self.mock_port.find_by.assert_called_once_with(proposal_id)
