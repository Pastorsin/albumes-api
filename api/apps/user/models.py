from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

BaseUser = get_user_model()


class User(BaseUser):
    class Meta:
        proxy = True


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

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )


@receiver(post_save, sender=BaseUser)
def create_settings(sender, instance, created, **kwargs):
    if created:
        Settings.objects.create(user=instance)
