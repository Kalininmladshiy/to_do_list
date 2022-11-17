# Сервис Список дел

Данный сервис предназначен для планирования дел. Он реализован на базе Django и предоставляет пользователю возможность добавлять дела через панель администратора, а так же через запросы непосредственно с сайта.

## Установка:

### 1. Копируем содержимое проекта себе в рабочую директорию

### 2. Разворачиваем внутри скопированного проекта виртуальное окружение:
```
python -m venv <название виртуального окружения>
```

### 3. Устанавливаем библиотеки:
```
pip install -r requirements.txt
```

### 4. Для хранения переменных окружения создаем файл .env:
```
touch .env
```
Генерируем секретный ключ DJANGO в интерактивном режиме python:
* `python`
* `import django`
* `from django.core.management.utils import get_random_secret_key`
* `print(get_random_secret_key())`
    
Копируем строку в `.env` файл: `DJANGO_KEY='ваш ключ'` 


### 5. Переходим в директорию проекта и выполняем миграции в БД: 
```
cd womanup/

python manage.py makemigrations

python manage.py migrate
```

## Использование:

### 1. Создаем панель администратора:

```
python manage.py createsuperuser
```


### 2. Запускаем сервер:

```
python manage.py runserver
```


### 3. Переходим на http://127.0.0.1:8000/ и видим интерфейс добавления заданий:

![изображение](https://user-images.githubusercontent.com/106922768/202460731-d448cd0a-33d6-4aa7-8380-a9787f3e375b.png)

### 4. Так же задания можно добавлять через панель администратора. Переходим на http://127.0.0.1:8000/admin/ и видим модель заданий:

![изображение](https://user-images.githubusercontent.com/106922768/202461186-848229c0-0d92-4a66-8bb2-62e84aa88014.png)

Задания можно фильтровать по дате задания, дате завершения и потому сделаны они или нет.

### 5. Создание задания:
![изображение](https://user-images.githubusercontent.com/106922768/202461660-fec3fa09-8199-4062-adc1-6d7f1d650956.png)


## Цели проекта

Код написан в тестовых целях на вакансию компании [WOMANUP](https://womanup.online/). 

 
