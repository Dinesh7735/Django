from django.db import models

# Create your models here.
class Students(models.Model):
    Rollno = models.IntegerField(primary_key=True)
    Sname = models.CharField(max_length=100)
    Sage = models.IntegerField(null=False)
    Perc = models.DecimalField(decimal_places=2,max_digits=2)

