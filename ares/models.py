from django.db import models
from autoslug import AutoSlugField
from PIL import Image
from os import name
from io import BytesIO
from django.core.files import File

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

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image_data:
                self.thumbnail = self.make_thumbnail(self.image_data)
                self.save()
                return self.thumbnail.url
            
            else:
                # Default Image
                return 'https://via.placeholder.com/240x180.jpg'
    
    # Generating Thumbnail - Thumbnail is created when get_thumbnail is called
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
    


