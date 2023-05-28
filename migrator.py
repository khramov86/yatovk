import requests
import os
import base64
from dotenv import load_dotenv
import time
import pickle
from yapi.yaclient import Client

load_dotenv()


YA_CLIENT_ID = os.getenv("YA_CLIENT_ID")
YA_CLIENT_SECRET = os.getenv("YA_CLIENT_SECRET")


yaclient = Client(YA_CLIENT_ID, YA_CLIENT_SECRET)
orgs = yaclient.get_orgs()
print(orgs)
