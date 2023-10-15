import requests
import time
import pickle
import os
from .structures import Department, User, Org, OrgList
from tempfile import gettempdir
from os import path


class Client:
    def __init__(self, client_id, client_secret, renew_token=False) -> None:
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__login_headers = {"Content-type": "application/x-www-form-urlencoded"}
        self.__baseurl = "https://api360.yandex.net"
        self.renew_token = renew_token
        self.get_token()
        self.__apiheaders = {
            "Authorization": "Bearer " + self.__access_token,
            "Accept-Language": "ru",
        }

    def write_token_cache(self, data, filename="token_cache"):
        filepath = path.join(gettempdir(), filename)
        with open(filepath, "wb") as file:
            pickle.dump(data, file)

    def read_token_cache(self, filename="token_cache"):
        filepath = path.join(gettempdir(), filename)
        if not os.path.isfile(filepath) or os.stat(filepath).st_size == 0:
            return None
        with open(filepath, "rb") as file:
            data = pickle.load(file)
            if time.time() - data.get("timestamp") < data.get("expires_in"):
                return data
            return None

    def get_token(self):
        if not self.renew_token:
            auth = self.read_token_cache()
        if not auth:
            code_url = f"https://oauth.yandex.ru/authorize?response_type=code&client_id={self.__client_id}"
            auth_url = "https://oauth.yandex.ru/token"
            print(f"Перейдите по ссылке {code_url}")
            access_code = input("Введите код: ")
            resp = requests.post(
                f"{auth_url}",
                headers=self.__login_headers,
                data={
                    "grant_type": "authorization_code",
                    "code": access_code,
                    "client_id": self.__client_id,
                    "client_secret": self.__client_secret,
                },
            )
            auth = {**resp.json(), "timestamp": time.time()}
            self.write_token_cache(auth)
        self.__access_token = auth.get("access_token")
        self.__auth = auth
        return auth

    def get_orgs(self):
        resp = requests.get(
            f"{self.__baseurl}/directory/v1/org", headers=self.__apiheaders
        )
        orgs = OrgList([])
        for item in resp.json().get('organizations', []):
            org = Org(item.get('id'), item.get('name'), item.get('email'), item.get('phone'), item.get('fax'), item.get('language'), item.get('subscriptionPlan'))
            orgs.add_org(org)
        return orgs

    def get_org_by_name(self, name):
        orgs = self.get_orgs().orgs
        for org in orgs:
            if org.name == name:
                return org

    def get_orgstructures(self):
        pass

    def get_users_by_org_name(self, name):
        org = self.get_org_by_name(name)
        org_id = org.id
        resp = requests.get(
            f"{self.__baseurl}/directory/v1/org/{org_id}/users", headers=self.__apiheaders, params={'perPage': 100}
        )
        return resp.json()
