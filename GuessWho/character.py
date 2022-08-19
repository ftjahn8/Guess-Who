from typing import Callable


class Character:
    name: str
    features: list[str]

    def __init__(self, name: str, features: list[str]):
        self.name = name
        self.features = features

    def contains_all(self, features: list[str]) -> bool:
        return all(feature in self.features for feature in features)

    def contains_any(self, features: list[str]) -> bool:
        return any(feature in self.features for feature in features)


Question = Callable[[Character], bool]
