from django.db import models

# Create your models here.


class Sites(models.Model):
    image = models.ImageField()
    description = models.TextField(max_length=500)


class Graphic(models.Model):
    img = models.ImageField()


class Defaultpic(models.Model):
    image = models.ImageField()

