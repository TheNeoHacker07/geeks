from django.db import models

from django.contrib.auth import get_user_model


class TodoModel(models.Model):
    title=models.CharField(max_length=12,verbose_name='заголовок')
    description=models.CharField(max_length=134,verbose_name='описание')
    completed=models.BooleanField(default=False,verbose_name='готово')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)


    def __str__(self):
        return self.title










# Create your models here.
