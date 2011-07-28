from django.db import models


# here is my model
# seems to be nice right ? but useless, i don;t use this. 
class Light(models.Model):
    name = models.CharField(max_length=32)
    x = models.IntegerField()
    y = models.IntegerField()
    channel = models.IntegerField()
    channelsize = models.IntegerField()
    radius = models.IntegerField()
    red = models.IntegerField()
    blue = models.IntegerField()
    green = models.IntegerField()

# [{"red":0,"blue":0,"green":0,"channel":2,"name":"lampe1","x":535,"y":249,"radius":10,"channelsize":5}
# Create your models here.

