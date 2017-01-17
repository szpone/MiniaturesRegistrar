from django.contrib import admin
from minis.models import System, Army, Miniatures, PaintManufacturer, Colors

# Register your models here.


@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ("system_name", )


@admin.register(Army)
class ArmyAdmin(admin.ModelAdmin):
    list_display = ("army_name", )


@admin.register(Miniatures)
class MiniaturesAdmin(admin.ModelAdmin):
    list_display = ("miniature_name", "mini_image")


@admin.register(PaintManufacturer)
class PaintManufacturerAdmin(admin.ModelAdmin):
    list_display = ("colors", )


@admin.register(Colors)
class Colors(admin.ModelAdmin):
    list_display = ("color_name", )
