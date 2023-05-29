# Places Remember

Веб-приложение, с помощью которого люди могут хранить свои впечатления о посещаемых местах.
# Установка

1. Клонируйте репоизторий:  

`git clone https://github.com/manjurulhoque/django-social-network.git`

2. Переместитесь в корневую диеркторию проекта:

 `cd places_remember`

3. Создайте файл .env и пропишите свои ключи (можно использовать те, что указаны ниже).
```
GOOGLE_MAPS_API_KEY = AIzaSyARKLq7vbL80ITOeznFxTf6QNAIgoLZs8s

GOOGLE_CLIENT_ID = 202502817145-eh37abt9ij2lcu49nkrinojg8fjt7tf9.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET = 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

VK_APP_ID = 51651708
VK_SECRET_KEY = tc0Y0oea4Ygt9ymBDF9k
VK_SERVICE_ACCESS_KEY = 01daa54e01daa54e01daa54ed102ce8132001da01daa54e65b25460222b471dff08d896
```
4. Установите виртуальное окружение:
`python3 -m venv my-project-env`
 
5. Активируйте виртуальное окружение
`. my-project-env/bin/activate`

6. Установите зависимости
`pip install -r req.txt`
 
7. Создайте миграции
```
python3 manage.py makemigrations
python manage.py migrate
```

8. Запустите сервер
`python3 manage.py runserver`

9. Откройте браузер и перейдите по ссылке: `http://127.0.0.1:8000/`
