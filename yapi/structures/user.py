from typing import List


class UserInfo:
    first: str
    last: str
    middle: str

class Contact:
    alias: bool
    main: bool
    syntetic: bool
    type: str
    value: str

class User:
    id: str
    about: str
    birthday: str
    isRobot: bool
    isEnabled: bool
    language: str
    name: str
    contacts: List[Contact]
    email: str
    departmentId: 1
    isAdmin: bool

class Users:
    userlist: List[User]
