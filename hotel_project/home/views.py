from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.

def get_hotel(request):
    try:
        hotel_obj = Hotel.objects.all()

        if request.GET.get('sort_by'):
            sort_by_value = request.GET.get('sort_by')
            if sort_by_value == 'asc':
                hotel_obj = hotel_obj.order_by('hotel_price')
            elif sort_by_value == 'dsc':
                hotel_obj = hotel_obj.order_by('-hotel_price')
        
        if request.GET.get('amount'):
            amount = request.GET.get('amount')
            hotel_obj = hotel_obj.filter(hotel_price__lte=amount)
                                        

        payload = []

        for obj in hotel_obj:
            payload.append({'hotel_name':obj.hotel_name,
                            'hotel_price':obj.hotel_price,
                            'hotel_description':obj.hotel_description,
                            'banner_image':str(obj.banner_image),})

        return JsonResponse(payload,safe=False) 

    except Exception as e:
        print(e)
    
    return JsonResponse({'message':'Invalid'})
