# Тестовое задание
> Примечание
- Знаю, что файл .env не надо загружать в git, но решил так сделать, чтобы проще проверять задание вам
- Понимаю, что выполнено не идеально, но был бы очень рад вашей конструктивной критике. Это поможет мне дальше расти как спецалист

## Задача: 
- Сделать сервис по заказу товаров и отслеживанию заказов

## Установка:

1. `git clone https://github.com/romaha57/test_task_online_shop.git`
2. `pip install -r requirements.txt`
3. `cd online_shop`
4. `python manage.py makemigrations`
5. `python manage.py migrate`
6. `python manage.py createsuperuser`

## Функционал

- Регистрация и авторизация
- Просмотр каталога товаров
- Формирование корзины товаров
- Сохранение заказа
- Отслеживание своих заказов
- Для администраторов: управление статусами заказа

## Структура БД

![database_structure](/online_shop/static/img/database_structure.png)
