from unittest import TestCase
from unittest.mock import MagicMock

from reviewlogic.gateways import proposal_gateway
from reviewlogic.usecases import proposal_usecase


class ProposalUseCaseTestCase(TestCase):
    def test_list(self):
        mock_port = MagicMock(spec=proposal_gateway.ProposalPort)
        usecase = proposal_usecase.ProposalUseCase(mock_port)

        actual = usecase.list()

        self.assertEqual(actual, mock_port.list.return_value)
        mock_port.list.assert_called_once_with()
