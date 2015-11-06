from django.db import models
from django.utils.translation import ugettext_lazy as _
from .base import BaseModel
from .images import BaseImage
from .hearing import Hearing


class Introduction(BaseModel):
    abstract = models.TextField(verbose_name=_('Abstract'))
    content = models.TextField(verbose_name=_('Content'))
    hearing = models.ForeignKey(
        Hearing, related_name='introductions', on_delete=models.SET_NULL, null=True)


class IntroductionImage(BaseImage):
    hearing = models.ForeignKey(Introduction, related_name="images")
