# https://www.youtube.com/watch?v=EVa5Wdcgl94&ab_channel=CodingTech

import an_outside_lib
import an_outside_lib_2


class Dog(an_outside_lib_2.BreadEater):
    def eat_bread(self):
        print("The dog is eating bread...")

    def bark(self):
        print("Au au!")


# an_outside_lib.BreadEater.register(Dog)


def main():
    # Can I instantiate a ABC class?
    # my_inst = an_outside_lib.Animal() # this will crash
    # Traceback (most recent call last):
    #   File "/root/python_study/various/230501_experiment_abc/main.py", line 10, in <module>
    #     main()
    #   File "/root/python_study/various/230501_experiment_abc/main.py", line 6, in main
    #     my_inst = an_outside_lib.Animal()
    # TypeError: Can't instantiate abstract class Animal with abstract method eat_bread
    duck = an_outside_lib_2.Duck()
    an_outside_lib_2.feed_bread(duck)
    print(f"{isinstance(duck, an_outside_lib_2.BreadEater) = }")

    dog = Dog()
    an_outside_lib_2.feed_bread(dog)

    # ==========================================================================
    my_duck = an_outside_lib.Duck()
    an_outside_lib.feed_bread(my_duck)

    print(f"{isinstance(my_duck, an_outside_lib.BreadEater) = }")


if __name__ == "__main__":
    main()
