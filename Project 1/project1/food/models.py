from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name
    
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=1000,default="https://media.istockphoto.com/id/938742222/photo/cheesy-pepperoni-pizza.jpg?s=1024x1024&w=is&k=20&c=OKXH55QwDa6L3cY2pTTz1DKVT2clqW3zcVaJVaU-N_U=")


    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
    