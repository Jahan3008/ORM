from django.db import models
from django.contrib import admin
class Loan_Receiver (models.Model):
 rid=models.CharField(max_length=20,primary_key="rid")
 name=models.CharField(max_length=100)
 loan_amount=models.IntegerField()
 dob=models.IntegerField()
 receiver_referance=models.IntegerField()

class Loan_ReceiverAdmin(admin.ModelAdmin):
   list_display=('rid','name','loan_amount','dob','receiver_referance')