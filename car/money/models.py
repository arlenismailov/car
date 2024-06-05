from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)


class CarorSpareparts(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


# сатуучуга
class Brand(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Model(models.Model):
    title = models.CharField(max_length=32)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Product(models.Model):
    price = models.IntegerField(default=0)
    title = models.CharField(max_length=32)
    brand = models.ForeignKey(Brand, related_name='reviews', on_delete=models.CASCADE)
    model = models.ForeignKey(Model, related_name='reviews', on_delete=models.CASCADE)
    year = models.IntegerField(default=2000)
    mileage = models.IntegerField(default=0)
    body_color = models.CharField(max_length=20)
    interior_color = models.CharField(max_length=20)
    engine = models.CharField(max_length=40)
    transmission = models.CharField(max_length=40)
    place = models.CharField(max_length=32, default='Bishkek')


class PhotoEvents(models.Model):
    events = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/product/', null=True, blank=True)
    video = models.FileField(upload_to='videos/product/', null=True, blank=True)


class CarBet(models.Model):
    number = models.IntegerField(default=0)
    total_number = models.IntegerField(default=0)
    buy_now = models.IntegerField(default=0)
    start_date = models.DateTimeField
    end_date = models.DateField()