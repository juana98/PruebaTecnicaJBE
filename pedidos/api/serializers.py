from rest_framework.serializers import ModelSerializer
from api.models import Driver, Order, PickupLocation, DestLocation

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['date','driver', 'pickup_location', 'dest_location']
        depth = 1

class DriverSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'x', 'y', 'last_update']


class PickupSerializer(ModelSerializer):
    class Meta:
        model = PickupLocation
        fields = '__all__'

class DestSerializer(ModelSerializer):
    class Meta:
        model = DestLocation
        fields = '__all__'

