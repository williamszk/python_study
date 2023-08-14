def add_numbers(n1: int, n2: int) -> int:
    return n1 + n2


initial: dict[str, int] = {}

initial2: list[str] = []

# a tuple of undefined size which contains strings
initial3: tuple[str, ...] = ()


class Parent:
    def capitalize(self, text: str) -> str:
        return text.upper()


# typehints.py:19: error: Argument 1 of "capitalize" is incompatible with supertype "Parent"; supertype defines the argument type as "str"  [override]
# typehints.py:19: note: This violates the Liskov substitution principle
# typehints.py:19: note: See https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides
# Found 1 error in 1 file (checked 1 source file)

# class Child(Parent):
#     def capitalize(self, text: int) -> str:
#         return str(text).upper()
