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
    (8, "Shoes"),
    (9, "Golden_elements"),
    (10, "Bone_elements"),
    (11, "Base")
    )

# a wargame - set of rules, a wargame can have many armies


class System(models.Model):
    system_name = models.CharField(max_length=128)

    def __str__(self):
        return self.system_name

# Army model - one system can have many armies


class Army(models.Model):
    system = models.ForeignKey(System, related_name="system")
    army_name = models.CharField(max_length=128)

    def __str__(self):
        return self.army_name

# Miniatures can belong only to one army


class Miniatures(models.Model):
    army = models.ForeignKey(Army, related_name="army")
    miniature_name = models.CharField(max_length=128)
    mini_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.miniature_name

# paint colors


class Colors(models.Model):
    color_name = models.CharField(max_length=64)
    miniatures = models.ManyToManyField(Miniatures, related_name="miniatures")

    def __str__(self):
        return self.color_name

# paint producers


class PaintManufacturer(models.Model):
    manufacturer = models.CharField(max_length=64)
    colors = models.ForeignKey(Colors, related_name="color")

    def __str__(self):
        return self.manufacturer


class ElementsColor(models.Model):
    paints = models.ForeignKey(Colors, related_name="color_elements")
    miniatures = models.ForeignKey(Miniatures, related_name="minis")
    elements = models.IntegerField(choices=MINIATURE_ELEMENTS)
