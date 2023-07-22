from django.urls import path
from . import views

from rest_framework import routers


app_name = 'users'
router = routers.DefaultRouter()

router.register('api/users', views.UserListView, basename='user')


urlpatterns = router.urls