from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#For more information on SQL Db Query refer to Part 5.

class Post(models.Model):

    title = models.CharField(max_length = 100)
    content = models.TextField()
#Change time but also not update every time a modification to the post has been made.
    date_posted = models.DateTimeField(default=timezone.now)
#If user = deleted, all posts from User also deleted (Not vice-versa)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


