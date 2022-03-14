from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='profile',
    )
    picture = models.ImageField(_('Picture'), default='user_profile/img/default.png')

    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')
