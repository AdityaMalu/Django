from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    typ = models.CharField(max_length=200,default='action')
    image = models.ImageField(upload_to='images/',default='images/None/default.jpg')

    def __str__(self):
        return self.name