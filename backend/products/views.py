from django.test import TestCase
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ProductCreateAPIView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title=serializer.validated_data.get("title")
        content=serializer.validated_data.get("content")
        if content is None:
            content=title
        serializer.save(content=content)



product_create_view=ProductCreateAPIView.as_view()


class ProductDeatialAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # lookup_field='pk'

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    def perform_update(self, serializer):
        instance=serializer.save()
        if not instance.content:
            instance.comtemt=instance.title


product_update_view=ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
      
        super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()





#creating out own create and list and detail api 
@api_view(["GET", "POST"])
def product_alt_view(request,pk=None,*args,**kwargs):
    if request.method == 'POST':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title=serializer.validated_data.get("title")
            content=serializer.validated_data.get("content")
            if content is None:
                content=title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid":"not good data"},status=404)
        
        

    if request.method == 'GET':
        if pk is not None:
            obj=get_object_or_404(Product,pk=pk)
            data=ProductSerializer(obj,many=False).data
            return Response(data)
        else:
            qs=Product.objects.all()
            data=ProductSerializer(qs,many=True).data
            return Response(data)


        


