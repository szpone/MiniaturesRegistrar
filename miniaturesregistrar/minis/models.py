from django.db import models


# Create your models here.

MINIATURE_ELEMENTS = (
    (1, "Skin"),
    (2, "Weapon_wood"),
    (3, "Eyes"),
    (4, "Armor"),
    (5, "Weapon_steel"),
    (6, "Clothes_upper"),
    (7, "Clothes_lower"),
    (8, "Boots"),
    (9, "Golden_elements"),
    (10, "Bone_elements"),
    (11, "Base")
    )

# a wargame - set of rules, a wargame can have many armies


class System(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

# Army model - one system can have many armies


class Army(models.Model):
    system = models.ForeignKey(System)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

# Miniatures can belong only to one army



# paint colors

class Paint(models.Model):
    name = models.CharField(max_length=64)
    manufacturer = models.ForeignKey("PaintManufacturer")

    def __str__(self):
        return self.name


class Miniature(models.Model):
    army = models.ForeignKey(Army)
    name = models.CharField(max_length=128)
    mini_image = models.ImageField(null=True, blank=True)
    paint = models.ManyToManyField(Paint)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.name


# paint producers


class PaintManufacturer(models.Model):
    manufacturer = models.CharField(max_length=64)

    def __str__(self):
        return self.manufacturer

# model for adding specific colors to miniatures elements


class Element(models.Model):
    paints = models.ManyToManyField(Paint)
    miniature = models.ForeignKey(Miniature, related_name='elements')
    number = models.IntegerField(choices=MINIATURE_ELEMENTS)
