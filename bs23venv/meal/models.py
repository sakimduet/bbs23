from django.db import models
from django.utils import timezone

# Create your models here.
class Registrationf(models.Model):
      firstName=models.CharField(max_length=200)
      lastName=models.CharField(max_length=200)
      email=models.EmailField(max_length=200)
      phnNum=models.DecimalField(max_digits=200,decimal_places=10)
      password=models.CharField(max_length=200)

      def _str_(self):
          return self.firstName