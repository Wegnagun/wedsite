from django.db import models
from django.utils import timezone


APPROVAL_CHOICES = (('A', 'Я с удовольствием приду'), ('F', 'К сожалению, не смогу присутствовать'))
TRANSFER_CHOICES = (('Own', 'Будут на машине'), ('Take', 'Готовы взять пассажира'), ('No', 'Нужен трансфер'))

class Guest(models.Model):
    """ Модель гостей """
    fio = models.CharField(max_length=200, verbose_name='ФИО гостя')
    created_date = models.DateTimeField(default=timezone.now)
    approval = models.CharField(max_length=15, choices=APPROVAL_CHOICES, default='O', verbose_name='Подтверждение участия')
    transfer = models.CharField(max_length=15, choices=TRANSFER_CHOICES, default='O', verbose_name='Необходимость трансфера')
    other = models.TextField(blank=True, verbose_name='Уточняющая информация')
    verbose_name = 'Гость'
    drinks = models.ManyToManyField('Drinks', blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.fio
    
    class Meta:
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'    


class Drinks(models.Model):
    """ Модель вида алкоголя """
    sort = models.IntegerField(verbose_name = 'Для очерелности отображения', blank=True)
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Наименование алкоголя'
    )
    chosen = models.ManyToManyField(Guest, related_name="chosen_alc", blank=True, verbose_name='Кто выбрал:')
    verbose_name = 'Крепкие напитки'

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Крепкие напитки'
        verbose_name_plural = 'Крепкие напитки'    


