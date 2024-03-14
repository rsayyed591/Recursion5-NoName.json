from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Report(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    file=models.FileField(upload_to='reports/',null=True,blank=True)
    date=models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username
    

class ReportDetail(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    report=models.ForeignKey(Report,on_delete=models.CASCADE)
    doctor_name=models.CharField(max_length=100,null=True,blank=True)
    hemoglobin=models.CharField(max_length=100,null=True,blank=True)
    rbc=models.CharField(max_length=100,null=True,blank=True)
    mch=models.CharField(max_length=100,null=True,blank=True)
    mcv=models.CharField(max_length=100,null=True,blank=True)
    bilirubin_total=models.CharField(max_length=100,null=True,blank=True)
    bilirubin_direct=models.CharField(max_length=100,null=True,blank=True)
    bilirubin_indirect=models.CharField(max_length=100,null=True,blank=True)
    protien=models.CharField(max_length=100,null=True,blank=True)
    urea=models.CharField(max_length=100,null=True,blank=True)
    uric_acid=models.CharField(max_length=100,null=True,blank=True)
    sodium=models.CharField(max_length=100,null=True,blank=True)
    pottasium=models.CharField(max_length=100,null=True,blank=True)
    chloride=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self) -> str:
        return self.user.username



class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)


