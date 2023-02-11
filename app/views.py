from django.shortcuts import render

# Create your views here.




from .models import Plan , Recharge
from .serializers import PlanSerializer , RechargeSerializer
from rest_framework import status, viewsets
from rest_framework import generics



class PlanListView(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer





class RechargeView(viewsets.ModelViewSet):
    queryset = Recharge.objects.all()
    serializer_class = RechargeSerializer


