from django.db import models
from django.utils.translation import gettext_lazy as _
from interview.models import Interview
from model_utils.models import SoftDeletableModel, TimeStampedModel
from sortedm2m.fields import SortedManyToManyField
from user.models import User


class Album(TimeStampedModel, SoftDeletableModel):
    class Corner(models.TextChoices):
        TOP_LEFT = 'TOP_LEFT', _('Top left')
        TOP_RIGHT = 'TOP_RIGHT', _('Top right')
        BOTTOM_LEFT = 'BOTTOM_LEFT', _('Bottom left')
        BOTTOM_RIGHT = 'BOTTOM_RIGHT', _('Bottom right')

    all_objects = models.Manager()

    name = models.CharField(max_length=255)

    qr_position = models.CharField(max_length=255, choices=Corner.choices)

    interviews = SortedManyToManyField(Interview)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name
