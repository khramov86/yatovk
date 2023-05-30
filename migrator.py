#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from yapi.yaclient import Client

load_dotenv()


YA_CLIENT_ID = os.getenv("YA_CLIENT_ID")
YA_CLIENT_SECRET = os.getenv("YA_CLIENT_SECRET")


yaclient = Client(YA_CLIENT_ID, YA_CLIENT_SECRET)
org = yaclient.get_org_by_name('infolinkcomp.ru')
print(org)
