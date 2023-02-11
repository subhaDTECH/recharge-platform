from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db import models
import uuid


## base model
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True , editable=False , default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    class Meta:
        abstract = True 


## mobile operator type 
class Operator(models.Model):
    opertor_name=models.CharField(max_length=255)
    location=models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.opertor_name




## plans Table 
class Plan(BaseModel):
    operator=models.ForeignKey(Operator, on_delete=models.CASCADE , related_name='plan')
    price=models.IntegerField()
    is_valid=models.BooleanField()
    exprire_date=models.DateTimeField()
    data=models.CharField(max_length=255 , default="1gb")
    message=models.CharField(max_length=255, default="100 Messages")
    is_unlimited=models.BooleanField(default=False)


    def __str__(self) -> str:
        return str(self.price  )

    




## recharge Model

class Recharge(BaseModel):
     user=models.ForeignKey(User, on_delete=models.CASCADE , related_name='customer_data')
     operator=models.ForeignKey(Operator,on_delete=models.CASCADE, related_name='oprator_type')
     Plan=models.ForeignKey(Plan,on_delete=models.CASCADE, related_name='rechage_user')


     def __str__(self) -> str:
        return str(self.user)






## customer Table
class Customer(BaseModel):
    user=models.ForeignKey(User, on_delete=models.CASCADE , related_name='customer_user')
    operator=models.ForeignKey(Operator,on_delete=models.CASCADE, related_name='oprator_user')
    Plan=models.ManyToManyField(Plan)
    address=models.CharField(max_length=255)
    Phone=models.CharField(max_length=10)


    def __str__(self) -> str:
        return str(self.user)
    



## payment information 

class Payment(BaseModel):
    user=models.ForeignKey(User, on_delete=models.CASCADE , related_name='payment_user')
    plan=models.ForeignKey(Plan, on_delete=models.CASCADE , related_name='User_plan') 
    signature_ID=models.IntegerField()
    Payment_ID=models.IntegerField()


    def __str__(self) -> str:
        return str(self.payment_ID)




