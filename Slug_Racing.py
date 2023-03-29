#Python Slug Race Game


import random
import time
import emoji

#emoji.emojize('Olá mundo Python :sunglasses:', use_aliases=True)

FINISH_LINE = 31
SLUG_NAMES = ["Lesma1", "Lesma2","Lesma3","Lesma4","Lesma5"]

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
    print('==' * 35)

def check_finish_line(slug_list):
    for slug in slug_list:
        if slug.position >= FINISH_LINE:
            return slug
    return None



def main():
    while True :
        aposta = input(f'Em qual lesma deseja apostar? \n{SLUG_NAMES[0]}\n{SLUG_NAMES[1]}\n{SLUG_NAMES[2]}\n{SLUG_NAMES[3]}\n{SLUG_NAMES[4]}\n-> ').title()
        if aposta not in SLUG_NAMES:
            print('Insira o nome correto da Lesma!')
        else:
            break

    try:
        val = int(input('Qual valor deseja apostar? R$ '))
    except Exception:
        pass
        print('Digite um código correto')

    print(emoji.emojize("Preparar, Apontar, GO ! :crossed_flags:"))
    slug_list = [Slug(name) for name in SLUG_NAMES]
    winner = None
    while not winner:
        display_race(slug_list)
        move_slugs(slug_list)
        winner = check_finish_line(slug_list)
        time.sleep(2)
    if winner.name == aposta:
        print('Parabéns você venceu!')
        print(f'Aposta realizada: {aposta}')
        print(f'Valor Apostado:  R${val}   |   Valor Recebido: R${(val*5)*90//100}')
    else:
        print('você perdeu !!!')
        print(f'Aposta realizada: {aposta}')
        print(f'Valor Apostado:  R${val}   |   Valor Perdido: R${val}')
    print(emoji.emojize(f" :crossed_flags: :crossed_flags: :crossed_flags: The winner is {winner.name}  :crossed_flags: :crossed_flags: :crossed_flags:"))

if __name__ == "__main__":
    main()