# Тестовое задание
> Примечание
- Знаю, что файл .env не надо загружать в git, но решил так сделать, чтобы проще проверять задание вам
- Понимаю, что выполнено не идеально, но был бы очень рад вашей конструктивной критике. Это поможет мне дальше расти как спецалист

## Задача: 
- Сделать сервис по заказу товаров и отслеживанию заказов

## Установка:

### 1 вариант:

1. `git clone https://github.com/romaha57/test_task_online_shop.git`
2. `pip install --upgrade pip`
3. `pip install -r requirements.txt`
4. `cd online_shop`
5. `python manage.py makemigrations`
6. `python manage.py migrate`
7. `python manage.py createsuperuser`


### 2 вариант:
1. `git clone https://github.com/romaha57/test_task_online_shop.git`
2. `docker-compose up -d --build`
3. `docker-compose run --rm django python online_shop/manage.py makemigrations` 
4. `docker-compose run --rm django python online_shop/manage.py migrate` 
5. `docker-compose run --rm django python online_shop/manage.py createsuperuser`
6. Создаем суперпользователя и заходим в админ: http://localhost:8000/admin



## Как работает сайт
- Документация OpenAPI в файлах openapi.json/openapi.yaml
- Устанавливаем себе на компьютер по инструкции выше
- Заходим на localhost:8000/admin и авторизуемся как суперпользователь
- Далее наш суперпользователь, созданный в начале имеет максимальные права и затем он раздает их другим пользователям (администраторам сайта)
- ![add_permissions](/online_shop/static/img/add_permission.png)
- Эти пользователи имеют возможность управлять товарами, корзинами и заказами(в частности, менять статус заказа)
- ![add_permissions](/online_shop/static/img/change_status_order.png)
- По нажатию на значок лупы откроется окно с пользователями сайта, нужно выбрать по фильтру администраторов и назначить администратора, который поменял статус заказа
- Также при отклонении заказа нужно написать комментарий к этому заказу, чтобы пользователь увидел причину( по умолчанию он видит 'Уточняется')
- Для теста функционала уже добавлена пару простых товаров
## Функционал

- Регистрация и авторизация
- Просмотр каталога товаров
- Формирование корзины товаров
- Сохранение заказа
- Отслеживание своих заказов
- Для администраторов: управление статусами заказа

## Структура БД

![database_structure](/online_shop/static/img/database_structure.png)

P.S. Если будут какие-то вопросы с радостью отвечу: https://t.me/romaha_57
