from dataclasses import dataclass

@dataclass
class Org:
    id: int
    name: str
    email: str
    phone: str
    fax: str
    language: str
    subscriptionPlan: str
