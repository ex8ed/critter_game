# -*- coding: UTF-8 -*-
"""Тамагочи для освоения классов и простейших методов"""
from config import start_text


class Critter:
    """Тамагочи по Доусону"""

    def __init__(self, name='Борис Бритва', hunger=0, boredom=0):
        self.__name = name
        self.__hunger = hunger
        self.__boredom = boredom

    def __pass_time(self):
        self.__hunger += 1
        self.__boredom += 1

    @property
    def mood(self):
        md = self.__hunger + self.__boredom
        if md < 5:
            return 'прекрасно'
        elif 5 <= md <= 10:
            return 'неплохо. Сейчас бы сижку и пивка для ясности мысли'
        elif 11 <= md <= 15:
            return 'не сказать, чтобы отлично'
        else:
            return 'на улице рейн, на душе пейн...'

    def talk(self):
        print(f'Меня зовут {self.__name} и я чувствую себя {self.mood} на данный момент')
        self.__pass_time()

    def eat(self, food=4):
        print('Ммм, баланда :3')
        self.__hunger -= food
        if self.__hunger < 0:
            self.__hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print('УРА МЯЧ! Еще раз за забор выбросишь, скотина, я тебе в тапки насру.')
        self.__boredom -= fun
        if self.__boredom < 0:
            self.__boredom = 0
        self.__pass_time()


def main():
    """Инициализирует процесс игры"""
    print("Вы в игре тамагочи!")
    name = input("Прежде чем играть, настало время ответственно подойти к вопросам.\n\nКак назовешь зверька? ")
    animal = Critter(name)
    choice = None
    while choice != '0':
        print()
        print(start_text)
        choice = input('Ваш выбор:\t')
        if choice == '0':
            print('Закрывайте за собой дверь при выходе!')
        elif choice == '1':
            animal.talk()
        elif choice == '2':
            animal.eat()
        elif choice == '3':
            animal.play()
        elif choice == '4':
            print('Ты охуел руку на животное поднимать? Еще раз так сделаешь, я тебе файловую систему наебну.')
        else:
            print('Что-то ты промахнулся, родной. Такого числа не предусмотрено')


main()
input('Press any button to exit...\nIcon by Freepik\nMIT Licence, 2022, (c). All rights reserved.')
