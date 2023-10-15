# Мигратор с Yandex на Mail

## Использование

Установить зависимости
```
pip3 install -r requirements.txt
```
Получить токен https://oauth.yandex.ru/

Создать файл .env
```
YA_CLIENT_ID=client_id
YA_CLIENT_SECRET=secret_key
YA_ORG=domain.name
```

## TODO
- [ ] Yandex API
    - [x] Реализовать получение токенов
    - [x] Реализовать кэширование токенов
    - [x] Реализовать получение организаций, пользователей
    - [ ] Реализовать поддержку получения групп
- [ ] Mail API
    - [ ] Реализовать получение токенов
    - [ ] Реализовать заведение пользователей и структурных подразделений
    - [ ] Реализовать миграцию по CSV-файлу + imapsync

## Ссылки
* Описание API Yandex
  * Админка для учетных записей 
    https://admin.yandex.ru
  * Получить токены
    https://oauth.yandex.ru/
  * Описание API
    https://yandex.ru/dev/api360/doc/concepts/intro.html
    
    https://yandex.ru/dev/api360/doc/concepts/access.html

    https://yandex.ru/dev/id/doc/ru/codes/code-url

    https://yandex.ru/dev/api360/doc/ref/OrganizationsService/OrganizationsService_List.html

* Описание API Mail