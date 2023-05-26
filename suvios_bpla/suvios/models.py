
from django.contrib.auth.models import User
from django.db import models

class Chapter(models.Model):
    chapter_number = models.IntegerField()
    chapter_title = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
class AttemptChapter(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='attempts')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='attempts_chapter')


