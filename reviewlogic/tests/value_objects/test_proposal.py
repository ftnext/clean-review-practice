# 完全コンストラクタの重複が気になり継承を使った書き直した際に使ったテスト
import dataclasses
from unittest import TestCase

from reviewlogic.value_objects import ProposalId


class ProposalTestCase(TestCase):
    def test_raise_error_under_0_value(self):
        with self.assertRaises(ValueError) as cm:
            ProposalId(0)

        self.assertEqual(str(cm.exception), "不正: 0以下")

    def test_frozen(self):
        proposal_id = ProposalId(1)

        with self.assertRaises(dataclasses.FrozenInstanceError):
            proposal_id.value = 2
