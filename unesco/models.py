from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class States(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Iso(models.Model):
    name= models.CharField(max_length=128)

    def __str__(self) :
        return self.name


# class Region(models.Model):
#     name = models.CharField(max_length=128)
#     state = models.ManyToManyField('States', through='Category')

#     def __str__(self) :
#         return self.name

class Category(models.Model) :
    name = models.CharField(max_length=128)
    # region = models.ForeignKey(Region, on_delete=models.CASCADE)
    # states =models.ForeignKey(States, on_delete=models.CASCADE)
    # iso = models.ForeignKey(Iso, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    description = models.CharField(max_length=1024)
    justification = models.CharField(max_length=1024,null=True, blank=True)
    longitude=models.DecimalField(max_digits=19, decimal_places=10,null=True)
    latitude=models.DecimalField(max_digits=19, decimal_places=10,null=True)
    area_hectares=models.DecimalField(max_digits=19, decimal_places=10,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    states = models.ForeignKey(States, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)


    def __str__(self) :
        return self.name




