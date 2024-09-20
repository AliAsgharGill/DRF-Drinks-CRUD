from django.http import JsonResponse
from .serializers import DrinkSerializer
from .models import Drink

def drink_list(request):
    
    #getting all the drinks
    drinks = Drink.objects.all()
    # serializing the drink data
    serializer = DrinkSerializer(drinks, many=True)
    # returning json 
    return JsonResponse({"drinks":serializer.data}) # if we need to send data other then object then we need to pass another argument safe=False