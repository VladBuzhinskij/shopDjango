from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    address=models.TextField(blank=True,null=True,verbose_name='Адрес')
    
    class Meta:
        db_table = 'user'
        verbose_name ='Пользвателя'
        verbose_name_plural ='Пользователи'
    
    def __str__(self) -> str:
        return self.username
