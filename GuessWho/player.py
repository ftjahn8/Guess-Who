from __future__ import annotations

import random
from abc import ABC, abstractmethod

from gameboard import GameBoard
from character import Question


class PlayerInterface(ABC):
    _ready_to_guess_person: bool
    _has_guessed_person: bool
    _figured_it_out: bool

    @property
    def ready_to_guess_person(self) -> bool:
        return self._ready_to_guess_person

    @property
    def has_guessed_person(self) -> bool:
        return self._has_guessed_person

    @property
    def figured_it_out(self) -> bool:
        return self._figured_it_out

    @abstractmethod
    def take_turn(self, other: PlayerInterface) -> None:
        """"""

    @abstractmethod
    def ask_question(self) -> Question:
        """"""

    @abstractmethod
    def guess_person(self) -> Question:
        """"""

    @abstractmethod
    def answer_question(self, question: Question) -> bool:
        """"""


class Player(PlayerInterface):
    game_board: GameBoard

    def __init__(self):
        self.game_board = GameBoard()

    def take_turn(self, other: PlayerInterface) -> None:
        if len(self.game_board.characters) == 1:
            pass

        question = self.guess_person() if self.ready_to_guess_person else self.ask_question()
        result = other.answer_question(question)
        # print(f"Result was {result}")
        remaining_characters = [character for character in self.game_board.characters if question(character) == result]
        # print(f"Amount remaining character {len(remaining_characters)}")
        self.game_board.characters = remaining_characters
        self._figured_it_out = self.has_guessed_person and len(remaining_characters) == 1 and result

    def answer_question(self, question: Question) -> bool:
        return question(self.game_board.mystery_person)

    def ask_question(self) -> Question:
        pass

    def guess_person(self) -> Question:
        pass


class SimplePlayer(Player):
    _random = random.Random()
    _ready_to_guess_person = True
    _has_guessed_person = False

    def ask_question(self) -> Question:
        return self.guess_person()

    def guess_person(self) -> Question:
        self._has_guessed_person = True
        name = self._random.choice(self.game_board.characters).name
        # print(f"Guessing Character: {name}")
        return lambda character: character.name == name


class NormalPlayer(Player):
    _has_guessed_person = False

    _random = random.Random()
    queried_features: list[str]

    def __init__(self):
        super().__init__()
        self.queried_features = []

    @property
    def ready_to_guess_person(self):
        return len(self.game_board.characters) == 1

    def ask_question(self) -> Question:
        remaining_features = set()
        for remaining_character in self.game_board.characters:
            remaining_features = remaining_features.union(set(remaining_character.features))

        remaining_features = remaining_features - set(self.queried_features)
        feature = self._random.choice(list(remaining_features))
        self.queried_features.append(feature)
        # print(f"Asking Feature: {feature}")
        return lambda character: feature in character.features

    def guess_person(self) -> Question:
        self._has_guessed_person = True
        name = self._random.choice(self.game_board.characters).name
        # print(f"Guessing Character: {name}")
        return lambda character: character.name == name


class LessThanHalfPlayer(Player):
    _has_guessed_person = False
    _random = random.Random()

    @property
    def ready_to_guess_person(self):
        return len(self.game_board.characters) == 1

    def ask_question(self) -> Question:
        target_size = max((len(self.game_board.characters) - 1) // 2, 1)
        remaining_features = set()
        for remaining_character in self.game_board.characters:
            remaining_features = remaining_features.union(set(remaining_character.features))
        return self.calculate_features(target_size, [], list(remaining_features))

    def calculate_features(self, target: int, first_group: list[str], second_group: list[str]) -> Question:
        new_second_group = second_group.copy()
        for feature in second_group:
            new_first_group = [feature] + first_group.copy()
            question = lambda character: character.contains_any(new_first_group)
            if target == self.game_board.characters_that_match(question):
                # print(f"Do they have {' or '.join(new_first_group)}?")
                return question

            new_second_group.remove(feature)
            question = self.calculate_features(target, new_first_group, new_second_group)
            if question is not None:
                return question

    def guess_person(self) -> Question:
        self._has_guessed_person = True
        name = self._random.choice(self.game_board.characters).name
        # print(f"Guessing Character: {name}")
        return lambda character: character.name == name


class AlwaysHalfPlayer(Player):
    _has_guessed_person = False
    _random = random.Random()

    @property
    def ready_to_guess_person(self):
        return len(self.game_board.characters) == 1

    def ask_question(self) -> Question:
        target_size = len(self.game_board.characters) // 2
        remaining_features = set()
        for remaining_character in self.game_board.characters:
            remaining_features = remaining_features.union(set(remaining_character.features))
        return self.calculate_features(target_size, [], list(remaining_features))

    def calculate_features(self, target: int, first_group: list[str], second_group: list[str]) -> Question:
        new_second_group = second_group.copy()
        for feature in second_group:
            new_first_group = [feature] + first_group.copy()
            question = lambda character: character.contains_any(new_first_group)
            if target == self.game_board.characters_that_match(question):
                # print(f"Do they have {' or '.join(new_first_group)}?")
                return question

            new_second_group.remove(feature)
            question = self.calculate_features(target, new_first_group, new_second_group)
            if question is not None:
                return question

    def guess_person(self) -> Question:
        self._has_guessed_person = True
        name = self._random.choice(self.game_board.characters).name
        # print(f"Guessing Character: {name}")
        return lambda character: character.name == name


class CombinedPlayer(Player):
    _has_guessed_person = False
    _random = random.Random()

    @property
    def ready_to_guess_person(self):
        return len(self.game_board.characters) <= 3

    def ask_question(self) -> Question:
        target_size = len(self.game_board.characters) // 2
        remaining_features = set()
        for remaining_character in self.game_board.characters:
            remaining_features = remaining_features.union(set(remaining_character.features))
        return self.calculate_features(target_size, [], list(remaining_features))

    def calculate_features(self, target: int, first_group: list[str], second_group: list[str]) -> Question:
        new_second_group = second_group.copy()
        for feature in second_group:
            new_first_group = [feature] + first_group.copy()
            question = lambda character: character.contains_any(new_first_group)
            if target == self.game_board.characters_that_match(question):
                # print(f"Do they have {' or '.join(new_first_group)}?")
                return question

            new_second_group.remove(feature)
            question = self.calculate_features(target, new_first_group, new_second_group)
            if question is not None:
                return question

    def guess_person(self) -> Question:
        self._has_guessed_person = True
        name = self._random.choice(self.game_board.characters).name
        # print(f"Guessing Character: {name}")
        return lambda character: character.name == name
