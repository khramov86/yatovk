#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from yapi.yaclient import Client
from pprint import pprint

load_dotenv()


YA_CLIENT_ID = os.getenv("YA_CLIENT_ID")
YA_CLIENT_SECRET = os.getenv("YA_CLIENT_SECRET")
YA_ORG = os.getenv("YA_ORG")

if YA_CLIENT_ID is None or YA_CLIENT_SECRET is None:
    raise ValueError(
        "YA_CLIENT_ID и YA_CLIENT_SECRET должны быть определены\n\
                    перейдите по ссылки для генерации https://yandex.ru/dev/api360/doc/concepts/access.html"
    )

yaclient = Client(YA_CLIENT_ID, YA_CLIENT_SECRET)
orgs = yaclient.get_orgs()
pprint(orgs)
org = yaclient.get_org_by_name(YA_ORG)
users = yaclient.get_users_by_org_name(YA_ORG)
# pprint(org)
pprint(users)