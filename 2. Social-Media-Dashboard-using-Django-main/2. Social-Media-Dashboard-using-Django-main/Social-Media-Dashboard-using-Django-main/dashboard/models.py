from django.db import models

# Create your models here.
# dashboard/models.py
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other profile fields if needed, e.g., bio, profile picture

    def __str__(self):
        return self.user.username

    def get_social_accounts(self):
        # This method can retrieve connected social accounts via django-allauth
        return SocialAccount.objects.filter(user=self.user)

# Example for linking social accounts (allauth handles most of this)
# You might want to store specific tokens or user IDs if allauth doesn't cover it
class SocialMediaAccount(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50) # e.g., 'Twitter', 'Facebook'
    access_token = models.CharField(max_length=255)
    # Add other fields like refresh token, platform user ID, etc.

    def __str__(self):
        return f"{self.profile.user.username}'s {self.platform} Account"