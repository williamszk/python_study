from abc import abstractmethod, ABCMeta, ABC
from typing import Union


class BreadEater(ABC):
    @abstractmethod
    def eat_bread(self):
        # this is a default implementation
        print("Eating bread...")


class Duck:
    def eat_bread(self):
        print("The duck is eating bread...")


# the register will not enforce the abstract method
# but the isinstance function will tell that Duck is instance of BreadEater
BreadEater.register(Duck)


class Monkey:
    def eat_bread(self):
        print("The monkey is eating bread...")


AnimalType = Union[Duck, Monkey]


def feed_animal(animal: AnimalType):
    pass


def feed_bread(bread_eater: BreadEater):
    bread_eater.eat_bread()
