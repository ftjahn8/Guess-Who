import random

from character import Character, Question


class GameBoard:
    _random = random.Random()

    characters: list[Character]
    mystery_person: Character

    def __init__(self):
        self.characters = []
        self.characters.append(Character("Claire", ["Woman", "Ginger Hair", "Hat", "Glasses"]))
        self.characters.append(Character("Eric", ["Yellow Hair", "Hat"]))
        self.characters.append(Character("Maria", ["Woman", "Brown Hair", "Hat"]))
        self.characters.append(Character("George", ["White Hair", "Hat"]))
        self.characters.append(Character("Bernard", ["Brown Hair", "Hat", "Bulbous Nose"]))
        self.characters.append(Character("Sam", ["White Hair", "Bald", "Glasses"]))
        self.characters.append(Character("Tom", ["Black Hair", "Bald", "Blue Eyes", "Glasses"]))
        self.characters.append(Character("Paul", ["White Hair", "Glasses"]))
        self.characters.append(Character("Joe", ["Yellow Hair", "Glasses"]))
        self.characters.append(Character("Frans", ["Ginger Hair"]))
        self.characters.append(Character("Anne", ["Woman", "Black Hair"]))
        self.characters.append(Character("Max", ["Black Hair", "Moustache", "Thick Lips", "Bulbous Nose"]))
        self.characters.append(Character("Alex", ["Black Hair", "Moustache", "Thick Lips"]))
        self.characters.append(Character("Philip", ["Black Hair", "Beard", "Rosy Cheeks"]))
        self.characters.append(Character("Bill", ["Ginger Hair", "Bald", "Beard", "Rosy Cheeks"]))
        self.characters.append(Character("Anita", ["Woman", "Yellow Hair", "Rosy Cheeks", "Blue Eyes"]))
        self.characters.append(Character("David", ["Yellow Hair", "Beard"]))
        self.characters.append(Character("Charles", ["Yellow Hair", "Moustache", "Thick Lips"]))
        self.characters.append(Character("Herman", ["Ginger Hair", "Bald", "Bulbous Nose"]))
        self.characters.append(Character("Peter", ["White Hair", "Thick Lips", "Blue Eyes", "Bulbous Nose"]))
        self.characters.append(Character("Susan", ["Woman", "White Hair", "Rosy Cheeks", "Thick Lips"]))
        self.characters.append(Character("Robert", ["Brown Hair", "Rosy Cheeks", "Blue Eyes", "Bulbous Nose"]))
        self.characters.append(Character("Richard", ["Brown Hair", "Bald", "Moustache", "Beard"]))
        self.characters.append(Character("Alfred", ["Ginger Hair", "Moustache", "Blue Eyes"]))

        self.mystery_person = self._random.choice(self.characters)
        # print(f"MysteryPerson: {self.mystery_person.name}")

    def characters_that_match(self, question: Question) -> int:
        return sum(int(question(character)) for character in self.characters)
