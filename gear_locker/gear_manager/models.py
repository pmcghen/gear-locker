from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    entered_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class GearListItem(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    is_worn = models.BooleanField(default=False)
    is_consumable = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    url = models.URLField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class GearList(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    entered_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    items = models.ManyToManyField(GearListItem, through='Item')
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name
