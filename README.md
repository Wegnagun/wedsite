# Wedding Site ✨

Современный свадебный сайт на Django с контейнеризацией через Docker. Проект включает бэкенд (Django), веб‑сервер (Nginx) и готовую структуру для статического контента и медиа.

## Обзор

Проект позволяет быстро развернуть свадебный сайт с:
- **Динамическим контентом** через админ-панель Django
- **Статическими страницами** (о паре, программа, карта и т. д.)
- **Галереей фотографий** и другими медиа
- **Формой обратной связи** для гостей
- **Оптимизированной отдачей статики** через Nginx

## Технологии

- **Backend**: Python 3.11, Django 4.x
- **Веб‑сервер**: Nginx (для статики и проксирования)
- **Контейнеризация**: Docker, Docker Compose
- **База данных**: SQLite (для разработки)

## Скриншот (пример)

> *Здесь вы можете разместить скриншот интерфейса сайта после первого запуска.*

![Wedding Site Screenshot](docs/screenshot.jpg)

## Установка и запуск

- sudo docker container ls
- sudo docker exec -it idконтейнера /bin/sh
- python manage.py migrate
- python manage.py collectstatic
- python manage.py createsuperuser
- python manage.py create_sample_drinks или python manage.py create_sample_drinks --file=path/to/your/file.json для указания другого файла
send_mail(subject='Тема письма',message='Текст письма',from_email=settings.DEFAULT_FROM_EMAIL,recipient_list=['recipient@example.com'],fail_silently=False,
)

export EMAIL_PASSWORD="ваш_новый_16_значный_пароль"
echo $EMAIL_PASSWORD
python manage.py sendtestemail wegnagun@bk.ru