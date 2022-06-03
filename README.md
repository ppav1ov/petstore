# 1. Краткое описание
Техническое демо проекта автотестов с парой функциональных 
тестов на методы:
GET, POST, PUT, DELETE.

Задание: есть сервис petstore, он поднят тут 
https://petstore.swagger.io/v2 

У него есть спецификация 
OAS3 файлик petstory.yaml - это единственное, что у тебя 
есть из входных параметров.

Есть ограничения:

    Python3
    Pytest   (https://github.com/pytest-dev/pytest)
    requests (https://github.com/psf/requests)

# 2. Работа с проектом
1. Скачать или клонировать целиком код проекта.
2. Выполнить для запуска тестов из директории проекта:

pytest tests/ --html=report.html --self-contained-html

3. Открыть report.html в браузере для отчета

ВНИМАНИЕ: в проекте добавлена небольшая 
исследовательская часть в виде тестов с использованием
пакета schemathesis. 
Для их запуска выполнить:

pytest tests_schemathesis/ --html=report.html --self-contained-html

ОСТОРОЖНО, эти тесты идут долго!!
