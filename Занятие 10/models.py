from django.db import models

# модули для настройки методов админки
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils import timezone # для времени
from django.utils.html import format_html # для создания строки html

User = get_user_model()

# venv/Scripts/activate
# py manage.py makemigrations
# py manage.py migrate
# заголовок - описание - цена - дата создания - дата обновления - тогр
class Advertisements(models.Model):
    title = models.CharField('заголовок',max_length=130)
    description = models.TextField('описание')
    price = models.DecimalField('цена',max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text='Отмените, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField("изображение", upload_to='advertisements/', black=True)


    # представление в виде строки
    def __str__(self):
        return f"Advertisements(id = {self.id}, title = {self.title}, price = {self.price})"

    # настройки для таблицы
    class Meta:
        db_table = 'advertisements' # переименовали таблицу 

    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
                               )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description='дата обновления')
    def updated_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: red; font-weight: bold;">Сегодня в {}</span>', updated_time
                )
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description='изображение')
    def image_display(self):
        if self.image:
            return format_html(
                '<img src="{}" style="width: 60px;">', self.image.url
            )
        else:
            return 'No Image'
    

