from collections.abc import Sequence
from dataclasses import dataclass
from typing import NewType

Title = NewType("Title", str)
Description = NewType("Description", str)


@dataclass
class Proposal:
    title: Title
    description: Description


@dataclass
class Proposals(Sequence):
    proposals: list[Proposal]

    def __len__(self):
        return len(self.proposals)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.__class__(self.proposals[key])
        return self.proposals[key]
