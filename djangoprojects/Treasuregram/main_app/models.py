from django.db import models

# Create your models here.
class Treasure(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
"""
treasures  = [
    Treasure(name ='Gold Nugget', value = 500.00,material= 'gold',location= "Curly's Creek, NM"),
    Treasure(name="Fool's Gold",value= 0, material='pyrite',location= "Fool's Falls, CO"),
    Treasure(name="Coffee Can",value=20.00,material= 'tin',location= 'Acme,CA')
]"""

