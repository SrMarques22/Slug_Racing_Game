#Python Slug Race Game


import random
import time
import emoji

#emoji.emojize('Olá mundo Python :sunglasses:', use_aliases=True)

FINISH_LINE = 30
SLUG_NAMES = ["Lesma1", "Lesma2", "Lesma3", "Lesma4", "Lesma5"]

class Slug:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.speed = random.randint(1, 5)

def display_race(slug_list):
    for slug in slug_list:
        print(emoji.emojize(f"{slug.name}: {' .' * slug.position}:snail:"))


def move_slugs(slug_list):
    for slug in slug_list:
        slug.position += slug.speed
    print('==' * 30)

def check_finish_line(slug_list):
    for slug in slug_list:
        if slug.position >= FINISH_LINE:
            return slug
    return None

def main():
    print("Get ready for the slug race!")
    slug_list = [Slug(name) for name in SLUG_NAMES]
    winner = None
    while not winner:
        display_race(slug_list)
        move_slugs(slug_list)
        winner = check_finish_line(slug_list)
        time.sleep(1)
    print(f"The winner is {winner.name}!")

if __name__ == "__main__":
    main()