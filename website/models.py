from django.db import models

# Create your models here.

# record model/database
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=8)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")