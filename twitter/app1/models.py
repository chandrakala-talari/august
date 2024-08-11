from django.db import models

# Create your models here.
class tweet(models.Model):
    username=models.CharField(max_length=20)
    date=models.DateTimeField(auto_now_add=True)
    post=models.CharField(max_length=200)

    def __str__(self):
        return self.username