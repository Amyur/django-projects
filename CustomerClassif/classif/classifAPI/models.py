from django.db import models

# Create your models here.
class Customer(models.Model):
    Fresh = models.IntegerField()
    Milk = models.IntegerField()
    Grocery = models.IntegerField()
    Frozen = models.IntegerField()
    Detergents_Paper = models.IntegerField()
    Delicassen = models.IntegerField()
    Channel_1 = models.IntegerField(default=0)
    Channel_2 = models.IntegerField(default=0)
    Region_1 = models.IntegerField(default=0)
    Region_2 = models.IntegerField(default=0)
    Region_3 = models.IntegerField(default=0)



