from .models import *
from .serializer import *
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
 


class myPag(PageNumberPagination):
     page_size = 8

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    product_count = Product.objects.count()
    authentication_classes = (TokenAuthentication,)
    permission_calsses = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title']
    # search_fields = ['title','=category__name','=major__major', '=subject__subject', "=condition__condition" 'school', '=city__name']
    filterset_fields = ['id','user','category__name', 'major__major','subject__subject', 'school__school','condition__condition', 'city__name','title']
    pagination_class = myPag

 
 
class ProductOrderViewSet(viewsets.ModelViewSet):
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer
    permission_calsses = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['buyer','seller']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_calsses = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('=name', 'id')
    filterset_fields = ['id', 'name']

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


class FaqViewSet(viewsets.ModelViewSet):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
      

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('=name',)


class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
  search_fields = ['=id', '=username', '=email']

# from django.shortcuts import render
# from backend.settings import EMAIL_HOST_USER
# from .forms import restapi
# from django.core.mail import send_mail
# # Create your views here.
# #DataFlair #Send Email
# def subscribe(request):
#     sub = forms.Subscribe()
#     if request.method == 'POST':
#         sub = forms.Subscribe(request.POST)
#         subject = 'Welcome to DataFlair'
#         message = 'Hope you are enjoying your Django Tutorials'
#         recepient = str(sub['Email'].value())
#         send_mail(subject, 
#             message, EMAIL_HOST_USER, [recepient], fail_silently = False)
#         return render(request, 'subscribe/success.html', {'recepient': recepient})
#     return render(request, 'subscribe/index.html', {'form':sub})
 