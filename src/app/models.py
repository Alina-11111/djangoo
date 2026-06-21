from django.db import models


class Customer(models.Model):
    firstname = models.CharField('Имя', max_length=255)
    lastname = models.CharField('Фамилия', max_length=255)
    age = models.PositiveIntegerField('Возраст')
    profession = models.CharField('Профессия', max_length=255)
    
    #Магический метод чтобы выводилось в терминале нормальыне выводы
    def __str__(self):
        return f"{self.firstname} {self.lastname}"