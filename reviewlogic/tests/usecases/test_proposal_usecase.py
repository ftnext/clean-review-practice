from unittest import TestCase
from unittest import mock
from unittest.mock import MagicMock

from reviewlogic.gateways import proposal_gateway
from reviewlogic.usecases import proposal_usecase


class ProposalUseCaseTestCase(TestCase):
    def test_list(self):
        mock_gateway = MagicMock(spec=proposal_gateway.ProposalGateway)
        usecase = proposal_usecase.ProposalUseCase(mock_gateway)

        actual = usecase.list()

        self.assertEqual(actual, mock_gateway.list.return_value)
        mock_gateway.list.assert_called_once_with()
