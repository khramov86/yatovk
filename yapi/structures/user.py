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
    isEnabled: bool
    language: str
    userInfo: UserInfo
    email: str
    departmentId: 1
    isAdmin: bool
    # contacts: List[Contact]

@dataclass
class UserList:
    users: List[User]
    
    def add_user(self, user: User):
        self.users.append(User)
