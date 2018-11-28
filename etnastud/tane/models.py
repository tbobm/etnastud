from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Student(models.Model):
    promotion = models.IntegerField()
    login = models.CharField(max_length=10)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
    )
    promotion = models.ForeignKey(
        'Promotion',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '{} - {}'.format(self.login, self.promotion.name)


class Promotion(models.Model):
    promo_id = models.IntegerField()
    name = models.CharField(max_length=50)


class Project(models.Model):
    project_id = models.IntegerField()
    name = models.CharField(max_length=256)
    promotion = models.OneToOneField(
        Promotion,
        on_delete=models.CASCADE,
        blank=True,
    )

