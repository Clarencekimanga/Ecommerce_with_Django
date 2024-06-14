from django.db import models

# Create your models here.
class product(models.mode):
    name = models.chartfield(max_length=300)
    description = models.textfield()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='products/')
    
    class Details(models.Model):
        pass

    
