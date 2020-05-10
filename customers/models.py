from django.db import models

# Create your models here.
class customers(models.Model):
    cus_name = models.CharField(max_length = 20)
    cus_mob = models.CharField(max_length = 20)
    cus_time = models.CharField(max_length = 20)
    cus_country = models.CharField(max_length = 20)
    class Meta:
        db_table = 'customers'
        managed = True
    def __str__(self):
        return self.cus_name
    

