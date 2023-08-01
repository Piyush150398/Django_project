from django.db import models

# Create your models here.
class Item(models.Model):
    
    def __str__(self):           # __str__ helps us to return the same of item_name as it is or else it will show like "food item 1"
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg")
    


