from django.db import models

FRAME_COLOR = (
    (0, 'żółty'),
    (1, 'niebieski'),
    (2, 'czerwony'),
    (3, 'zielony'),
    (4, 'brązowy'),
)

GLASS = (
    (0, 'matowe'),
    (1, 'przezroczyste')
)

PILLOW_COLOR = (
    (0, 'niebieski'),
    (1, 'czerwony'),
    (2, 'zielony'),
    (3, 'czarny'),
)

KIND_OF_PILLOW = (
    (0, 'zwykła'),
    (1, 'włochata'),
)


class User(models.Model):
    nick = models.CharField(max_length=64, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    password2 = models.CharField(max_length=128)
    address = models.TextField()


class Picture(models.Model):
    image = models.ImageField()
    frame_color = models.SmallIntegerField(choices=FRAME_COLOR)
    glass = models.SmallIntegerField(choices=GLASS)
    size = models.CharField(max_length=32)
    passe_partout = models.BooleanField(null=False)
    quantity = models.IntegerField()
    category = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=True, blank=True)


class Cushion(models.Model):
    image = models.ImageField()
    pillow_color = models.SmallIntegerField(choices=PILLOW_COLOR)
    kind = models.SmallIntegerField(choices=KIND_OF_PILLOW)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    # def __str__(self):
    #     return "{}".format(self.get_kind_display())

    ## cusion = Cushion.objects.get*(
    ## <img src="{{ cusion.image.url }}" />


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    pictures = models.ManyToManyField(Picture)
    cushions = models.ManyToManyField(Cushion)
    description = models.TextField(null=True, blank=True)

