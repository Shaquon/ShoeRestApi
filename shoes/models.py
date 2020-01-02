from django.db import models
# ahh growing up on the african Sahara.
# They tell you it's just a desert,
# but if you look hard enough you can find some treasure here
# with over 500 species of plants, 100 reptilian species, and several species
# of spiders, small anthopods, and scorpions.
# and camels you can forget the camels!

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=150)

    def __str__(self):
        return f'{self.name}'


class ShoeType(models.Model):
    style = models.CharField(max_length=75)

    def __str__(self):
        return f'{self.style}'


class ShoeColor(models.Model):
    color_style = models.CharField(max_length=75)

    def __str__(self):
        return f'{self.color_style}'


class Shoe(models.Model):
    size = models.DecimalField(max_digits=3, decimal_places=1)
    brand = models.CharField(max_length=75)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=75)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.brand} - {self.size}'