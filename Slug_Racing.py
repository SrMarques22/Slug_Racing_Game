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
        print(emoji.emojize(f"{slug.name}: {' _' * slug.position}:snail:"))


def move_slugs(slug_list):
    for slug in slug_list:
        #adicionamos um random abaixo, pois o valor só estava sendo atribuido 1 vez no inicio da corrida
        slug.position+= random.randint(0,slug.speed)
    print('==' * 30)

def check_finish_line(slug_list):
    for slug in slug_list:
        if slug.position >= FINISH_LINE:
            return slug
    return None

def main():
    print(emoji.emojize("Get ready for the slug race! :crossed_flags:"))
    slug_list = [Slug(name) for name in SLUG_NAMES]
    winner = None
    while not winner:
        display_race(slug_list)
        move_slugs(slug_list)
        winner = check_finish_line(slug_list)
        time.sleep(1)
    print(emoji.emojize(f" :crossed_flags: :crossed_flags: :crossed_flags: The winner is {winner.name}  :crossed_flags: :crossed_flags: :crossed_flags:"))

if __name__ == "__main__":
    main()