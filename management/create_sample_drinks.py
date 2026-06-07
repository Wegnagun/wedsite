import json

from django.core.management.base import BaseCommand
from models import Drinks


TABLES = [
    (Drinks, 'ingredients.json')
]


class Command(BaseCommand):
    help = 'Создаёт примерные записи напитков в базе данных из JSON-файлов с использованием bulk_create'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            dest='dry_run',
            help='Только показать, какие записи будут созданы (без сохранения в БД)',
        )
        parser.add_argument(
            '--file',
            type=str,
            default='data/drinks.json',
            help='Путь к JSON-файлу с данными (по умолчанию: drinks.json)',
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        json_file = options['file']

        # Загружаем данные из JSON-файла
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                sample_drinks_data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Файл {json_file} не найден!'))
            return
        except json.JSONDecodeError as e:
            self.stdout.write(self.style.ERROR(f'Ошибка в JSON-файле: {e}'))
            return

        created_count = 0
        existing_count = 0

        self.stdout.write(
            self.style.SUCCESS(f'Загружено {len(sample_drinks_data)} записей из {json_file} (dry-run: {dry_run})')
        )

        # Фильтруем существующие записи по полю name
        existing_names = set(
            Drinks.objects.filter(
                name__in=[item['name'] for item in sample_drinks_data]
            ).values_list('name', flat=True)
        )

        # Подготавливаем объекты для bulk_create
        new_drinks = []
        for drink_data in sample_drinks_data:
            if drink_data['name'] in existing_names:
                self.stdout.write(
                    self.style.WARNING(f'Запись уже существует: {drink_data["name"]}')
                )
                existing_count += 1
                continue

            new_drinks.append(Drinks(**drink_data))

        # Выполняем bulk_create, если не dry-run
        if new_drinks:
            if not dry_run:
                try:
                    created_objects = Drinks.objects.bulk_create(new_drinks)
                    created_count = len(created_objects)
                    self.stdout.write(
                        self.style.SUCCESS(f'Успешно создано {created_count} новых записей')
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Ошибка при bulk_create: {e}'))
                    return
            else:
                # В режиме dry-run просто показываем, что будет создано
                for drink in new_drinks:
                    self.stdout.write(
                        f'Будет создана запись: {drink.name} (sort={drink.sort})'
                    )
                created_count = len(new_drinks)
        else:
            self.stdout.write(self.style.NOTICE('Нет новых записей для создания'))

        # Финальный отчёт
        if not dry_run:
            self.stdout.write(
                self.style.SUCCESS(
                    f'Готово! Создано: {created_count}, уже существовало: {existing_count}'
                    ))
        else:
            self.stdout.write(
                f'Режим dry-run завершён. Планировалось создать: {created_count}, '
                f'уже существует: {existing_count}'
            )
