
# Музыкальная библиотека - API

Пользователи могут получать информацию о испольнителях, их альбомах и композициях в альбоме.


## Технологии


**Server:** Python, Django, DRF


## Установка

Скачайте репозиторий с исходным кодом

```bash
git clone git@github.com:sibwinter/misic-library-api.git
```
Установите виртуальное  окружение
```bash
virtualenv venv.
```
Активируйте окружение.

Для linux:
```bash
. venv\bin\activate
```
Для Windows:
```bash
. venv\Scripts\activate
```

Установите зависимости
```bash
pip install -r requirements.txt
```
Установите миграции
```bash
cd music_library_api
python manage.py migrate
```
Добавьте пользователя-админа
```bash
python manage.py createsuperuser
```
Запустите проект
```bash
python manage.py runserver
```
## API Reference

#### Ссылка на Swagger API 

```http
http://127.0.0.1:8000/swagger/
```


#### DRF OpenAPI

```http
http://127.0.0.1:8000
```

