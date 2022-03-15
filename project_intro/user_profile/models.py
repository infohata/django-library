from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db import models
from PIL import Image

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='profile',
    )
    picture = models.ImageField(_('Picture'), default='user_profile/img/default.png')

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)

    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')
