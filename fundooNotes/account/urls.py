from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'accounts', views.AccountView)

urlpatterns = [
    path('', include(router.urls)),
    path('account-auth', include('rest_framework.urls', namespace='rest_framework'))
]
