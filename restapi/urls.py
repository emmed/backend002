from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.urls import path
from restapi.views import *


# Routers provide an easy way of automatically determining the URL conf.

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('product', ProductViewSet)
router.register('category', CategoryViewSet)
router.register('productOrder', ProductOrderViewSet)
router.register('faq', FaqViewSet)
#router.register('stateCount', StateCountViewSet)
router.register('subject', SubjectViewSet)
router.register('major', MajorViewSet)
router.register('condition', ConditionViewSet)
router.register('location', LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #path('state/count/:state_id', StateCountViewSet, name='states-count')
 ]
