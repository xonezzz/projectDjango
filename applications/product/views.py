from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from applications.product.models import Product
from applications.product.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


class ProductListCreateApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




# class ProductListApiView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer



# class ProductCreateApiView(CreateAPIView):
#     queryset = ProductSerializer
#     permission_classes = [IsAuthenticated]


# class ProductDetailApiView(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer