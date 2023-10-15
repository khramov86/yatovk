from typing import List
from dataclasses import dataclass

@dataclass
class UserInfo:
    first: str
    last: str
    middle: str

# class Contact:
#     alias: bool
#     main: bool
#     syntetic: bool
#     type: str
#     value: str


@dataclass
class User:
    id: str
    about: str
    birthday: str
    isRobot: bool
    isEnabled: bool
    language: str
    name: UserInfo
    email: str
    departmentId: 1
    isAdmin: bool
    # contacts: List[Contact]

class Users:
    userlist: List[User]
