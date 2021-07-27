"""pedidos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
#router.register(r'drivers', views.DriverViewSet)

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('drivers/', views.DriverAPIView.as_view(), name='drivers'),
    path('orders/', views.OrderAPIView.as_view(), name='orders'),
    path('driver/', views.SearchDriverAPIView.as_view(), name='driver_search'),
    path('orders/<str:pk>/', views.SearchOrdersAPIView.as_view(), name='orders_search'),
    path('orders/<str:day>/driver/<int:id>', views.SearchDriverOrdersAPIView.as_view(), name='driver_orders_search')
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
