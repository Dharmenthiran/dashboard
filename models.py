from django.db import models
from datetime import datetime,date
# Create your models here.
class Mechine(models.Model):
    name=models.CharField(max_length=50,null=True)
    mechin_id=models.IntegerField(primary_key=True)
    created_at=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name

class Runned(models.Model):
    STATUS=(
        ('Mechine on','Mechin on'),
        ('Mechine off','Mechine off'),
        ('Mechine outoff service','Mechine outoff service')
    )
    mechine = models.ForeignKey(Mechine, null=True, on_delete=models.SET_NULL)
    status=models.CharField(max_length=50,null=True,choices=STATUS)
    Date = models.DateTimeField(auto_now_add=True)
    on_time = models.DateTimeField()
    off_time = models.DateTimeField()

    def __str__(self):
        return f"{self.get_status_display()} - {self.on_time} to {self.off_time}"