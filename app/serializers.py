from rest_framework import serializers
from .models import Customer , Plan , Payment ,Operator , Recharge
## customer serializer
class CustomerSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Customer
        fields = '__all__'


## plan serializer
class PlanSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Plan
        fields = '__all__'



## payment serializer
class PaymentSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Payment
        fields = '__all__'







##Operator

class OperatorSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Operator
        fields = '__all__'


##Recharge


class RechargeSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Recharge
        fields = '__all__'


