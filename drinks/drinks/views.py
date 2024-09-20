from django.http import JsonResponse
from .serializers import DrinkSerializer
from .models import Drink

def drink_list(request):
    
    #getting all the drinks
    drinks = Drink.objects.all()
    # serializing the drink data
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse({"drinks":serializer.data},safe=False)