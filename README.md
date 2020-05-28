# Каталог книг

Сервис каталога книг.

## Использование Docker

### Настройка проекта

Создайте `.env` файл в корне репозитория:

```bash
cp .env.sample .env
```

Внесите при необходимости корректировки в переменные окружения.

### Сборка образов

В корне репозитория выполните команду:

```bash
docker build .
```

Затем команду:

```bash
docker-compose build
```

### Запуск контейнеров

Для запуска контейнеров выполните команду:

```bash
docker-compose up -d
```

### Инициализация проекта

Команды выполняются внутри контейнера приложения:

```bash
docker-compose exec app bash
```

#### Применение миграций:

```bash
python manage.py migrate
```

#### Сборка статики:

```bash
python manage.py collectstatic
```

#### Создание суперпользователя

```bash
python manage.py createsuperuser
```

#### Добавление фикстур

```bash
python manage.py loaddata author publishing_house book
```

Проект доступен по адресу http://127.0.0.1:8000
