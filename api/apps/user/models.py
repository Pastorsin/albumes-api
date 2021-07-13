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
        HIGH_CONTRAST = 'HIGH_CONTRAST', _('High contrast')

    color_mode = models.CharField(
        max_length=255,
        choices=ColorMode.choices,
        default=ColorMode.ORIGINAL,
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )


@receiver(post_save, sender=BaseUser)
def create_settings(sender, instance, created, **kwargs):
    if created:
        Settings.objects.create(user=instance)
