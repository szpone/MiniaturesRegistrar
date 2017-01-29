from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

MINIATURE_ELEMENTS = (
    (0, "Skin"),
    (1, "Weapon_wood"),
    (2, "Eyes"),
    (3, "Armor"),
    (4, "Weapon_steel"),
    (5, "Clothes_upper"),
    (6, "Clothes_lower"),
    (7, "Boots"),
    (8, "Golden_elements"),
    (9, "Bone_elements"),
    (10, "Base")
)


class System(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Army(models.Model):
    system = models.ForeignKey(System)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Paint(models.Model):
    name = models.CharField(max_length=64)
    manufacturer = models.ForeignKey("PaintManufacturer")

    def __str__(self):
        return self.name


class Miniature(models.Model):
    army = models.ForeignKey(Army)
    name = models.CharField(max_length=128)
    mini_image = models.ImageField(null=True, blank=True,
                                   upload_to='images/%m/%d')
    paint = models.ManyToManyField(Paint)
    comment = models.TextField(blank=True)
    user = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.name


class PaintManufacturer(models.Model):
    manufacturer = models.CharField(max_length=64)

    def __str__(self):
        return self.manufacturer


class Element(models.Model):
    paints = models.ManyToManyField(Paint)
    miniature = models.ForeignKey(Miniature, related_name='elements')
    number = models.IntegerField(choices=MINIATURE_ELEMENTS)
