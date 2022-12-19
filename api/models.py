from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Venue(models.Model):
  image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)
  name = models.CharField(max_length=150, null=False, blank=False)
  description = models.TextField(null=True, blank=True)
  address = models.CharField(max_length=250, null=True, blank=True)
  phone_number= models.CharField(max_length=150, null=False, blank=False)
  website = models.CharField(max_length=150, null=False, blank=False)
  def __str__(self):
      return self.name

class Show(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='shows')
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    price_min = models.DecimalField(max_digits = 6,decimal_places=2, null=False, blank=False, default= 0.00)
    price_max = models.DecimalField(max_digits = 6, decimal_places=2, null=True, blank=True)
    month = models.IntegerField(null=False, blank=False)
    day = models.IntegerField(null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    door_time= models.CharField(max_length=100, null=False, blank=False)
    tickets_url = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)
    def __str__(self):
        return self.title