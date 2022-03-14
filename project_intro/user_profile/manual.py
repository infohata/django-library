from django.contrib.auth.models import User
from user_profile.models import UserProfile


users = User.objects.all()
for u in users:
    profile = UserProfile(user=u)
    try:
        profile.save()
    except:
        pass

