# LMS

[![Build Status][travis-badge]][travis-url]
[![Coverage][coverage-image]][coverage-url]

Learning Management System [REST API]

LMS (англ. _learning management system_) — [система управления обучением].

В качестве финального проекта по курсу [PPPoSD] мы разработали модельную версию LMS для вузов.

Авторы: [Daria Zvereva], [Bobrovskaya Nataliya]

## Краткое описание

Разработанный LMS предоставляет методы:

Для администратора:
- Предварительная регистрация
- Добавление учебного курса
- Добавление учебной группы
- Запись группы на курс
- Просмотр всех групп, курсов, студентов, пользователей

Для пользователя (студент, преподаватель):
- Регистрация по валидационному коду, полученному от администратора

Для залогинившегося пользователя (студент, преподаватель):
- Просмотр информации о других пользователях (кроме образования)
- Редактирование информации о себе (кроме фио, email, образования)
- Просмотр своих курсов (студент)
- Просмотр своих одногруппников (студент)

[PPPoSD]: https://khashaev.ru/courses/ppposd
[система управления обучением]: https://ru.wikipedia.org/wiki/%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0_%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F_%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC
[Daria Zvereva]: https://github.com/DariaZvereva
[Bobrovskaya Nataliya]: https://github.com/bobrovskayaa

## Инструкции по запуску

1. Скачивание/клонирование репозитория
2. Убедитесь, что у вас установлен python: `python --version`. Требуется Python 3. Желательно 3.7.1.
3. Установка пакетов: `pip install -r requirements.txt`
4. `export FLASK_APP=app.py ` (для windows `set FLASK_APP=app.py`)
5. Инициализация бд из папки lms: `flask db upgrade`
6. Инициализация учетной записи админа из корневой папки: `python script_add_admin.py`.

Если выскакивает ошибка на строчке `answer['error_message'] = str(exception)`, то согласно [stackoverflow] проблема может быть в версии Python 

7. Запуск сервера из папки lms: `flask run`

[stackoverflow]: https://stackoverflow.com/questions/42695670/handling-exceptions-in-python-3-6

## Запуск тестов

```
chmod +x setup.py
./setup.py test
```

## Copyright

Copyright © 2018 Daria Zvereva, Bobrovskaya Nataliya. See [license] for details.

[license]: LICENSE
[travis-url]: https://travis-ci.com/DariaZvereva/LMS
[travis-badge]: https://travis-ci.com/DariaZvereva/LMS.svg?branch=master
[coverage-image]: https://codecov.io/gh/DariaZvereva/LMS/branch/master/graph/badge.svg
[coverage-url]: https://codecov.io/gh/DariaZvereva/LMS
