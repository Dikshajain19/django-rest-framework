import json
from django.http import JsonResponse,HttpResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request,*args,**kwargs):
    """
    DRF API view
    """
    
    # instance=Product.objects.all().order_by("?").first()
    # data={}
    # if instance:
    #     data=ProductSerializer(instance).data
 
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        data=serializer.data

        return Response(serializer.data)
    # return HttpResponse(json_data_str,headers={"content-type":"application/json"})