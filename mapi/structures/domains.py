from dataclasses import dataclass
from types import List


@dataclass
class Domain:
    pass


class DomainList:
    domainList: List[Domain]
