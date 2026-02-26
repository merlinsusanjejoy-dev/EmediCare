from django.db import models
from Guest.models import *
# Create your models here.
class tbl_medicine(models.Model):
    medicine_name=models.CharField(max_length=30)
    medicine_photo=models.FileField(upload_to="Assets/Pharmacy/photo/")
    medicine_description=models.CharField(max_length=30)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    medicine_rate=models.CharField(max_length=30)
    Pharmacy=models.ForeignKey(tbl_pharmacy,on_delete=models.CASCADE)
    medicine_status=models.IntegerField(default=0) 
class tbl_stock(models.Model):
    stock_count=models.CharField(max_length=30)
    medicine=models.ForeignKey(tbl_medicine,on_delete=models.CASCADE)
                                                             