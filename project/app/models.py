from django.db import models


class Eat(models.Model):

    title = models.CharField(max_length=50)
    about = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Order(models.Model):
    product = models.CharField(max_length=30)
    quantity = models.IntegerField(max_length=1000)
    price = models.IntegerField(max_length=100000)

    def __str__(self):
        return self.product
