from unittest import TestCase
from unittest.mock import MagicMock

from reviewlogic.domains import review as r
from reviewlogic.drivers import review_driver as rd
from reviewlogic.gateways import review_gateway as rg
from reviewlogic.value_objects import ProposalId, ReviewId, UserId


class ReviewGatewayTestCase(TestCase):
    def test_save(self):
        mock_driver = MagicMock(spec=rd.ReviewDriver)
        mock_driver.save.return_value = 1
        gateway = rg.ReviewGateway(mock_driver)
        review = r.Review(
            UserId(1239), ProposalId(8), r.ScoreEnum("Maybe"), "So-so"
        )

        actual = gateway.save(review)

        self.assertEqual(actual, ReviewId(1))
        mock_driver.save.assert_called_once_with(
            rd.ReviewEntity(
                user_id=1239, proposal_id=8, score="Maybe", comment="So-so"
            )
        )
