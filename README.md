# Ex02 Django ORM Web Application
## Date:23/10/2024 

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<Jahan png loan.png>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py

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

admin.py

from django.contrib import admin
from .models import Loan_Receiver,Loan_ReceiverAdmin
admin.site.register(Loan_Receiver,Loan_ReceiverAdmin)

```

## OUTPUT
![alt text](<Screenshot 2024-10-22 164716.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
