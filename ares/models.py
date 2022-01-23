from django.db import models
from autoslug import AutoSlugField

#Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='product_name')
    spec = models.TextField()
    image_data = models.ImageField(upload_to="images/")
    rent_price = models.IntegerField(default=200)
    buy_price = models.IntegerField(default=600)

    def __str__(self):
        return self.product_name


