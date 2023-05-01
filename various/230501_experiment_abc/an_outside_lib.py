from typing import Protocol, runtime_checkable


@runtime_checkable
class BreadEater(Protocol):
    def eat_bread(self):
        pass


def feed_bread(bread_eater: BreadEater):
    bread_eater.eat_bread()


# Duck is implicitly a BreadEater because it implements the BreadEater Protocol
class Duck:
    def eat_bread(self):
        print("The duck is eating bread...")
