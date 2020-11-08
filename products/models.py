from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
# Create your models here.

class Brand(models.Model):
  brand = models.CharField(max_length=10)
  def __str__(self):
    return str(self.brand)
  
class Category(models.Model):
    category = models.CharField(max_length=10)
    def __str__(self):
      return str(self.category)   
    
class Type(models.Model):
    type = models.CharField(max_length=10)
    def __str__(self):
      return str(self.type)
 
class Model(models.Model):
    model = models.CharField(max_length=10)
    def __str__(self):
      return str(self.model)
    
class Size(models.Model):
    size = models.CharField(max_length=10)
    def __str__(self):
      return str(self.size)

""" class Product(models.Model):
    name = models.CharField(max_length=200)
    barcode = models.ImageField(upload_to='images/', blank=True)
    brand_id = models.CharField(max_length=2,null=True)
    category_id = models.CharField(max_length=3, null=True)
    type_id = models.CharField(max_length=3, null=True)
    model_id = models.CharField(max_length=2, null=True)
    size_id = models.CharField(max_length=2, null=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f'{self.brand_id}{self.category_id}{self.type_id}{self.model_id}{self.size_id}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save('barcode.png', File(buffer), save=False)
        return super().save(*args, **kwargs)

 """
    

