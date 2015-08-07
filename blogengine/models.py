from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    text = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.title
