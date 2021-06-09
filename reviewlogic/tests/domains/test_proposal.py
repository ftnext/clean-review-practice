from unittest import TestCase

from reviewlogic.domains import proposal
from reviewlogic.value_objects import ProposalId


class ProposalTestCase(TestCase):
    def test_from_entity(self):
        entity = {"id": 108, "title": "タイトル", "description": "詳細"}
        expected = proposal.Proposal(ProposalId(108), "タイトル", "詳細")

        actual = proposal.Proposal.from_entity(entity)

        self.assertEqual(actual, expected)


class ProposalsTestCase(TestCase):
    def setUp(self):
        self.proposals = proposal.Proposals(
            [
                proposal.Proposal(ProposalId(1), "Title 1", "Description 1"),
                proposal.Proposal(ProposalId(2), "Title 2", "Description 2"),
            ]
        )

    def test_length(self):
        actual = len(self.proposals)

        self.assertEqual(actual, 2)

    def test_return_slice(self):
        actual = self.proposals[:]

        self.assertEqual(actual, self.proposals)
