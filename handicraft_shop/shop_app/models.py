from django.contrib.auth.models import User
from django.db import models

FRAME_COLOR = (
    (-1, 'bez ramki'),
    (0, 'żółty'),
    (1, 'niebieski'),
    (2, 'czerwony'),
    (3, 'zielony'),
    (4, 'brązowy'),
    (5, 'czarny'),
)

GLASS = (
    (-1, 'brak szkła'),
    (0, 'zwykłe'),
    (1, 'antyrefleksyjne')
)

PILLOW_COLOR = (
    (0, 'niebieski'),
    (1, 'czerwony'),
    (2, 'zielony'),
    (3, 'czarny'),
    (4, 'różowy'),
    (5, 'jasnozielony'),
    (6, 'granatowy'),
)

KIND_OF_PILLOW = (
    (0, 'zwykła'),
    (1, 'włochata'),
)

CATEGORY = (
    (0, 'Metryczki'),
    (1, 'Ślubne'),
    (2, 'Religijne'),
    (3, 'Przyroda'),
    (4, 'inne'),
)


class Address(models.Model):
    address = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Picture(models.Model):
    image = models.ImageField()
    frame_color = models.SmallIntegerField(choices=FRAME_COLOR)
    glass = models.SmallIntegerField(choices=GLASS)
    size = models.CharField(max_length=32)
    passe_partout = models.BooleanField(null=False)
    quantity = models.IntegerField()
    category = models.SmallIntegerField(choices=CATEGORY)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=True, blank=True)


class Cushion(models.Model):
    image = models.ImageField()
    pillow_color = models.SmallIntegerField(choices=PILLOW_COLOR)
    kind = models.SmallIntegerField(choices=KIND_OF_PILLOW)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=True, blank=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    pictures = models.ManyToManyField(Picture)
    cushions = models.ManyToManyField(Cushion)
    description = models.TextField(null=True, blank=True)

