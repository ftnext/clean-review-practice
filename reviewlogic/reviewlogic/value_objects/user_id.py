from dataclasses import dataclass


@dataclass(frozen=True)
class UserId:
    value: int

    def __init__(self, value) -> None:
        if value < 0:
            raise ValueError("不正: 0未満")
        object.__setattr__(self, "value", value)