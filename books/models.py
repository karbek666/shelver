from django.db import models


class Good(models.Model):
    name = models.CharField('Имя', max_length=20)
    anons = models.TextField('Писатель', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.name