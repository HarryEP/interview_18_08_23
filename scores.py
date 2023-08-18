'''Scrabble game'''

import random


def calculate_word_score(word: str) -> int:
    '''calculates total points for the word given'''
    word_points = 0
    for letter in word.upper():
        word_points += calculate_letter_score(letter)
    return word_points


def calculate_letter_score(letter_points: dict, letter: str) -> int:
    '''returns the value of the letter given'''
    for key, value in letter_points.items():
        if letter in value:
            return key
    return 0


def get_random_letter() -> str:
    random_number = random.randint(65, 90)
    return chr(random_number)


def build_rack() -> list[str]:
    rack = []
    for i in range(7):
        rack.append(get_random_letter())
    return rack


def create_bag(distributions: dict) -> list[str]:
    bag = []
    for key, value in distributions.items():
        for letter in value:
            for i in range(key):
                bag.append(letter)
    return bag


def get_letter_from_bag(bag: list[str]) -> str:
    pass


if __name__ == "__main__":
    letter_points = {
        1: ['E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U'],
        2: ['D', 'G'],
        3: ['B', 'C', 'M', 'P'],
        4: ['F', 'H', 'V', 'W', 'Y'],
        5: ['K'],
        8: ['J', 'K'],
        10: ['Q', 'Z']
    }
    distributions = {
        12: ["E"],
        9: ["A", "I"],
        8: ["O"],
        6: ["N", "R", "T"],
        4: ["L", "S", "U", "D"],
        3: ["G"],
        2: ["B", "C", "M", "P", "F", "H", "V", "W", "Y"],
        1: ["K", "J", "X", "Q", "Z"]
    }
    print(create_bag())
