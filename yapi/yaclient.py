import requests
import time
import pickle
import os
from .structures import Department, User, Org


class Client:
    def __init__(self, client_id, client_secret) -> None:
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__login_headers = {"Content-type": "application/x-www-form-urlencoded"}
        self.__baseurl = "https://api360.yandex.net"
        self.get_token()
        self.__apiheaders = {
            "Authorization": "Bearer "
            + self.__access_token,
            "Accept-Language": "ru"
        }


    def write_token_cache(self, data, filename="token_cache"):
        with open(filename, "wb") as file:
            pickle.dump(data, file)

    def read_token_cache(self, filename="token_cache"):
        if not os.path.isfile(filename) or os.stat(filename).st_size == 0:
            return None
        with open(filename, "rb") as file:
            data = pickle.load(file)
            if time.time() - data.get("timestamp") < data.get("expires_in"):
                return data
            return None

    def get_token(self):
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
        self.__access_token = auth.get('access_token')
        self.__auth = auth
        return auth

    def get_orgs(self):
        resp = requests.get(f'{self.__baseurl}/directory/v1/org', headers=self.__apiheaders)
        return resp.json()
    
    def get_org_by_name(self, **args):
        if ['name'] not in args:
            raise "Args should be defined"
        name = args.get('name')
    
    def get_orgstructures(self):
        pass
    
    def get_persons(self):
        pass
    



