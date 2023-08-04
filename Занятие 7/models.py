from django.db import models

# модули для настройки методов админки
from django.contrib import admin
from django.utils import timezone # для времени
from django.utils.html import format_html # для создания строки html


# Create your models here.
# тестовый класс
class Cats(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.CharField(max_length=50)


# главный

# venv/Scripts/activate
# py manage.py makemigrations
# py manage.py migrate
# заголовок - описание - цена - дата создания - дата обновления - тогр
class Advertisements(models.Model):
    title = models.CharField('заголовок',max_length=100)
    description = models.TextField('описание')
    price = models.DecimalField('цена',max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text='Возможен торг или нет',default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    # представление в виде строки
    def str(self) -> str:
        return f"Advertisements(id = {self.id}, title = {self.title}, price = {self.price})"

    # настройки для таблицы
    class Meta:
        db_table = 'advertisements' # переименовали таблицу 



from app_advertisements.models import Advertisements

adv1 = Advertisements (title = 'Молоко', descriptoin = 'Свежее молоко', price = 100, auction = True)   # создаю запись
adv1.save()  # сохраняю

from django.db import connection

connection.queries  # получаю все запросы к sql

