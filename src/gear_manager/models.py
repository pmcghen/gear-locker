from django.db import models


class CustomUser(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    primary_sport = models.CharField(max_length=30, null=True, blank=True)
    default_measurement_system = models.CharField(max_length=10, choices=[('imperial', 'Imperial'), ('metric', 'Metric')], default='metric')

    def __str__(self):
        return self.user.username


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    parent_list = models.ManyToManyField('GearList', blank=True)
    entered_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class GearListItem(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    is_worn = models.BooleanField(default=False)
    is_consumable = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    url = models.URLField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    entered_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class GearList(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    entered_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    categories = models.ManyToManyField(Category)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name
