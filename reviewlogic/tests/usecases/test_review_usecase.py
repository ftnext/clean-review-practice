from unittest import TestCase
from unittest.mock import MagicMock

from reviewlogic.domains import review
from reviewlogic.gateways import review_gateway
from reviewlogic.usecases import review_usecase
from reviewlogic.value_objects import ProposalId, UserId


class ReviewTestCase(TestCase):
    def test_save(self):
        mock_port = MagicMock(spec=review_gateway.ReviewPort)
        usecase = review_usecase.ReviewUseCase(mock_port)

        user_id = UserId(108)
        proposal_id = ProposalId(2)
        score = review.ScoreEnum("Yes")
        comment = "Awesome"
        actual = usecase.save(user_id, proposal_id, score, comment)

        self.assertEqual(actual, mock_port.save.return_value)
        mock_port.save.assert_called_once_with(
            review.Review(
                UserId(108), ProposalId(2), review.ScoreEnum("Yes"), "Awesome"
            )
        )
