from typing import List
from dataclasses import dataclass


@dataclass
class UserInfo:
    first: str
    last: str
    middle: str

    def __repr__(self) -> str:
        return f"{self.first} {self.last} {self.middle}"
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
    isEnabled: bool
    language: str
    userInfo: UserInfo
    email: str
    departmentId: 1
    isAdmin: bool
    # contacts: List[Contact]
    def __repr__(self) -> str:
        return f"{self.id} {self.userInfo}"


@dataclass
class UserList:
    users: List[User]

    def add_user(self, user: User):
        self.users.append(user)

    def __repr__(self) -> str:
        return ','.join([user.id for user in self.users])