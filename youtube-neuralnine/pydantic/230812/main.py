import string
from pydantic import BaseModel, field_validator
from typing import Optional


# by inheriting from BaseModel this is basically a dataclass already
class User(BaseModel):
    username: str
    password: str
    age: int
    score: float
    email: Optional[str] = "default@mail.com"
    phone_number: Optional[str] = "9999-9999"

    # we can create validator methods
    @field_validator("username")
    def username_valid(cls, username: str):
        if any(p in username for p in string.punctuation):
            raise ValueError("username must not have punctuation")
        return username

    @field_validator("password")
    def password_valid(cls, password: str):
        if len(password) < 8:
            raise ValueError("password must be more than 8 characters long")
        # check if the password has any digits and punctuation and lower case and upper case characters
        if (
            any(p in password for p in string.punctuation)
            and any(d in password for d in string.digits)
            and any(l in password for l in string.ascii_lowercase)
            and any(u in password for u in string.ascii_uppercase)
        ):
            return password

        raise ValueError(
            "password must have digits and punctuation and lower case and upper case characters"
        )

    @field_validator("age")
    def age_valid(cls, age: int):
        if age < 0:
            raise ValueError("age must be a non-negative number")
        return age

    @field_validator("score")
    def score_valid(cls, score: float):
        if score < 0:
            raise ValueError("score must be a non-negative number")
        return score


# user1 = User(username="user1", password="123456", age=20, score=0, email="my@mail.com")
user1 = User(username="user1", password="12345678!hH", age=10, score=9.0)
# user1 = User(username="user1", password=123, age=10, score=9.0)

print(user1)
print(user1.age)
