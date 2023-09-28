from typing import List
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


@dataclass
class OrgList:
    orgs: List[Org]

    def add_org(self, org: Org):
        self.orgs.append(org)
