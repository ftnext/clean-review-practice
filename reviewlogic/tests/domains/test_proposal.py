from unittest import TestCase

from reviewlogic.domains import proposal


class ProposalsTestCase(TestCase):
    def setUp(self):
        self.proposals = proposal.Proposals(
            [
                proposal.Proposal("Title 1", "Description 1"),
                proposal.Proposal("Title 2", "Description 2"),
            ]
        )

    def test_length(self):
        actual = len(self.proposals)

        self.assertEqual(actual, 2)

    def test_return_slice(self):
        actual = self.proposals[:]

        self.assertEqual(actual, self.proposals)
