from django.db import models


# Create your models here.


class System(models.Model):
    system_name = models.CharField(max_length=128)


class Army(models.Model):
    system = models.ForeignKey(System, related_name="system")
    army_name = models.CharField(max_length=128)


class Miniatures(models.Model):
    army = models.ForeignKey(Army, related_name="army")
    miniature_name = models.CharField(max_length=128)
    mini_image = models.ImageField(null=True, blank=True)


class Colors(models.Model):
    color_name = models.CharField(max_length=64)
    miniatures = models.ManyToManyField(Miniatures, related_name="miniatures")


class PaintManufacturer(models.Model):
    manufacturer = models.CharField(max_length=64)
    colors = models.ForeignKey(Colors, related_name="color")
