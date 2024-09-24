from django.http import JsonResponse
from .serializers import DrinkSerializer
from .models import Drink
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

# for authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated


class DrinkList(ListAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class CreateDrink(CreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class UpdateDrink(UpdateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class DeleteDrink(DestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    


class UserLoginView(CreateAPIView):
    serializer_class = DrinkSerializer