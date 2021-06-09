from dataclasses import dataclass
from enum import Enum
from typing import NewType

from reviewlogic.value_objects import ProposalId, UserId

Comment = NewType("Comment", str)


class ScoreEnum(str, Enum):
    YES = "Yes"
    MAYBE = "Maybe"
    NO = "No"


@dataclass
class Review:
    user_id: UserId
    proposal_id: ProposalId
    score: ScoreEnum
    comment: Comment
