from django.urls import path, include
from rest_framework import routers

import ats.views as ats_views

router = routers.DefaultRouter()
# router.register(r'users', ats_views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
] 
