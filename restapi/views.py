from django.shortcuts import render
from  rest_framework import viewsets, status
from rest_framework.decorators import api_view
from .models import *
from django.contrib.auth.models import User
from .serializer import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.pagination import LimitOffsetPagination


class ProductViewPagination(LimitOffsetPagination):
    default_limit = 8
    max_limit = 12


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    product_count = Product.objects.count()
    authentication_classes = (TokenAuthentication,)
    permission_calsses = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['=title','=category__name','=major__major', '=subject__subject', "=condition__condition", '=location__location', 'school']
    filterset_fields = ['category__name', 'major__major','subject__subject', 'school']
    pagination_class = ProductViewPagination

    
#**********************

    # @api_view(['PUT', ])
    # def put(request):
    #     if request.method == 'PUT':
    #         product = Product.Objects.all()
    #         serializer = ProductSerializer(product, data=request.data)
    #         data = {}
    #         if serializer.is_valid():
    #             serializer.save()
    #             data["success"] = "update successful"
    #             return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductOrderViewSet(viewsets.ModelViewSet):
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer
    permission_calsses = (IsAuthenticated,)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_calsses = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('=name', 'id')

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('=subject',)

class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('=condition',)

class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('=major',)

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('=location',)

class FaqViewSet(viewsets.ModelViewSet):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('=location',)


# class StateCountViewSet(viewsets.ModelViewSet):
#     queryset = State.objects.all()
#     serializer_class = StateSerializer
#     permission_calsses = (IsAuthenticated,)
    
#     def get(self, request, format=None):
#         state_count = State.objects.count()
#         content = {'state_count' : state_count}
#         return Response(content)


class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
  search_fields = ['=id', '=username', '=email']


# @api_view(['POST',])
# def registration_view(request):

#     if request.method == 'POST':
#         serializer = RegristrationSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             user = serialzer.save()
#             data['response'] = "successfully registered a new userrrR"
#             data['username'] = user.username
#         else:
#                 data = serializer.errors
#                 return user
