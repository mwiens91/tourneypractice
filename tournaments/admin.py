from django.contrib import admin

# Register your models here.
from .models import Profile, Tourney, Match

admin.site.register(Profile)
admin.site.register(Tourney)
admin.site.register(Match)
