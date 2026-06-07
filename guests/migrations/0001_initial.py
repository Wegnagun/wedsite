import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort', models.IntegerField(blank=True, verbose_name='Для очерелности отображения')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Наименование алкоголя')),
            ],
            options={
                'verbose_name': 'Крепкие напитки',
                'verbose_name_plural': 'Крепкие напитки',
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=200, verbose_name='ФИО гостя')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approval', models.CharField(choices=[('A', 'Я с удовольствием приду'), ('F', 'К сожалению, не смогу присутствовать')], default='O', max_length=15, verbose_name='Подтверждение участия')),
                ('transfer', models.CharField(choices=[('Own', 'Будут на машине'), ('Take', 'Готовы взять пассажира'), ('No', 'Нужен трансфер')], default='O', max_length=15, verbose_name='Необходимость трансфера')),
                ('other', models.TextField(blank=True, verbose_name='Уточняющая информация')),
                ('drinks', models.ManyToManyField(blank=True, to='guests.drinks')),
            ],
            options={
                'verbose_name': 'Гость',
                'verbose_name_plural': 'Гости',
            },
        ),
        migrations.AddField(
            model_name='drinks',
            name='chosen',
            field=models.ManyToManyField(blank=True, related_name='chosen_alc', to='guests.guest', verbose_name='Кто выбрал:'),
        ),
    ]
