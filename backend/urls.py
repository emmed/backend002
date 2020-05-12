
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf.urls import include

from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.views.static import serve

# check this https://www.youtube.com/watch?v=QvTyqta3OJo&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=2
# this urls are  redirected to hithe urls.py of the restapi app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restapi.urls')),
    path('auth/', obtain_auth_token),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
