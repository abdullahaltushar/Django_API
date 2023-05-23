
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

#create Router Object

router= DefaultRouter()

# register Student ViewSet

router.register('studentapi', views.StudentViewSet, basename='stu')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
