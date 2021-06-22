from django.db import models
from django.utils.translation import gettext_lazy as _


class Settings(models.Model):
    class ColorMode(models.TextChoices):
        ORIGINAL = 'ORIGINAL', _('Original')
        COLOR_BLIND = 'COLOR_BLIND', _('Color blind')

    class FontSize(models.TextChoices):
        SMALL = 'SMALL', _('Small')
        MEDIUM = 'MEDIUM', _('Medium')
        LARGE = 'LARGE', _('Large')

    class ElementsPerPage(models.IntegerChoices):
        FEW = 4
        INTERMEDIATE = 8
        MANY = 16

    color_mode = models.CharField(
        max_length=255,
        choices=ColorMode.choices,
        default=ColorMode.ORIGINAL,
    )

    font_size = models.CharField(
        max_length=255,
        choices=FontSize.choices,
        default=FontSize.MEDIUM,
    )

    elements_per_page = models.IntegerField(
        choices=ElementsPerPage.choices,
        default=ElementsPerPage.FEW
    )
