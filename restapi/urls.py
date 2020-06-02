from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.urls import path
from rest_framework import routers, serializers, viewsets
from restapi.views import *
from cities_light.models import City



# Routers provide an easy way of automatically determining the URL conf.

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('city', CityViewSet)
router.register('product', ProductViewSet)
router.register('category', CategoryViewSet)
router.register('productOrder', ProductOrderViewSet)
router.register('faq', FaqViewSet)
router.register('subject', SubjectViewSet)
router.register('major', MajorViewSet)
router.register('condition', ConditionViewSet)
router.register('school', SchoolViewSet)
router.register('contactUser', ContactUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
 ]

