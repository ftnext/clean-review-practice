from collections.abc import Sequence
from dataclasses import dataclass
from typing import NewType

from reviewlogic.value_objects import ProposalId

Title = NewType("Title", str)
Description = NewType("Description", str)


@dataclass
class Proposal:
    id: ProposalId
    title: Title
    description: Description

    @classmethod
    def from_entity(cls, entity):
        return cls(
            ProposalId(entity["id"]), entity["title"], entity["description"]
        )


@dataclass
class Proposals(Sequence):
    proposals: list[Proposal]

    def __len__(self):
        return len(self.proposals)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.__class__(self.proposals[key])
        return self.proposals[key]
