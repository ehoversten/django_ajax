from django.db import models

# Create your models here.
class Post(models.Model):
    title   = models.CharField(max_length=120)
    message = models.CharField(max_length=255)


    def __str__(self):
        return self.title + " - " + self.message

    def __repr__(self):
        return "<Title: {} | {}>".format(self.title, self.message)
