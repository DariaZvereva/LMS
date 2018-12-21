# LMS

[![Build Status][travis-badge]][travis-url]
[![Coverage][coverage-image]][coverage-url]

Learning Management System [REST API]

LMS (англ. _learning management system_) — [система управления обучением].

В качестве финального проекта по курсу [PPPoSD] мы разработали модельную версию LMS для вузов.

Авторы: [Daria Zvereva], [Bobrovskaya Nataliya]

## Краткое описание

Разработанный LMS предоставляет методы:
Для администратора
- Предварительная регистрация
- Добавление учебного курса
- Добавление учебной группы
- Запись группы на курс
- Просмотр всех групп, курсов, студентов, пользователей

Для пользователя (студент, преподаватель) :
- Регистрация по валидационному коду, полученному от администратора

Для залогинившегося пользователя (студент, преподаватель) :
- Просмотр информации о других пользователях (кроме образования)
- Редактирование информации о себе (кроме фио, email, образования)
- Просмотр своих курсов (студент)
- Просмотр своих одногруппников (студент)

[PPPoSD]: https://khashaev.ru/courses/ppposd
[система управления обучением]: https://ru.wikipedia.org/wiki/%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0_%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F_%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC
[Daria Zvereva]: https://github.com/DariaZvereva
[Bobrovskaya Nataliya]: https://github.com/bobrovskayaa

## Copyright

Copyright © 2018 Daria Zvereva, Bobrovskaya Nataliya. See [license] for details.

[license]: LICENSE
[travis-url]: https://travis-ci.com/DariaZvereva/LMS
[travis-badge]: https://travis-ci.com/DariaZvereva/LMS.svg?branch=master
[coverage-image]: https://codecov.io/gh/DariaZvereva/LMS/branch/master/graph/badge.svg
[coverage-url]: https://codecov.io/gh/DariaZvereva/LMS
