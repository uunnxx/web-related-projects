from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    profile_pic = models.ImageField(null=True, blank=True, default='Default.png', upload_to='images/')

    # FK

    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)












