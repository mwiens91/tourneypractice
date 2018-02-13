from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    wins = models.PositiveIntegerField()


class Matches(models.Model):
    winner = models.OneToOneField(Profile, on_delete=models.CASCADE)
    player1 = models.CharField(max_length=30)
    player2 = models.CharField(max_length=30)
    game-id = models.PositiveIntegerField()

class Tourney(models.Model):

    size = models.PositiveIntegerField()
    name = models.CharField(max_length=30,blank=True)
    winner = models.CharField(max_length=30,blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()





