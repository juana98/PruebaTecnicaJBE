from django.db.models.expressions import RawSQL
from django.shortcuts import render
import requests
from api.models import Driver, Order, PickupLocation, DestLocation
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import DriverSerializer, OrderSerializer, PickupSerializer, DestSerializer
from datetime import datetime
from math import sqrt
import operator

class DriverAPIView(APIView):

    def get(self,request):
        drivers = Driver.objects.all()
        drivers_serializer = DriverSerializer(drivers, many = True)
        return Response(drivers_serializer.data)

    def put(self,request):
        drivers = Driver.objects.filter()
        drivers_serializer = DriverSerializer(drivers, many = True)
        return Response(drivers_serializer.data)
    
class OrderAPIView(APIView):
    
    def post(self, request):
        order_data = request.data

        new_pickup = PickupLocation.objects.create(x_pickup = order_data['pickup_location']['x_pickup'], y_pickup = order_data['pickup_location']['y_pickup'])
        new_pickup.save()

        new_dest = DestLocation.objects.create(x_dest = order_data['dest_location']['x_dest'], y_dest = order_data['dest_location']['y_dest'])
        new_dest.save()

        new_order = Order.objects.create(date = order_data["date"], driver = Driver.objects.get(id=order_data["driver"]), pickup_location = new_pickup, dest_location = new_dest )
        new_order.save()

        serializer = OrderSerializer(new_order)

        return Response(serializer.data)
    
    def get(self,request):
        orders = Order.objects.all()
        orders_serializer = OrderSerializer(orders, many = True)
        return Response(orders_serializer.data)
    
class SearchOrdersAPIView(APIView):
     
    def get(self,request, pk=None):
        data = pk.split('-')
        date_int = datetime(int(data[0]),int(data[1]),int(data[2]),00,00,00)
        print(date_int)
        date_end = datetime(int(data[0]),int(data[1]),int(data[2]),23,59,00)
        print(date_end)
        orders = Order.objects.filter(date__in = RawSQL("select date from api_order where date between %s and %s",(date_int,date_end)))
        orders_serializer = OrderSerializer(orders, many = True)
        return Response(orders_serializer.data)
    

class SearchDriverOrdersAPIView(APIView):

    def get(self,request, day=None, id=None):
        data = day.split('-')
        date_int = datetime(int(data[0]),int(data[1]),int(data[2]),00,00,00)
        print(date_int)
        date_end = datetime(int(data[0]),int(data[1]),int(data[2]),23,59,00)
        print(date_end)
        orders = Order.objects.filter(date__in = RawSQL("select date from api_order where driver_id = %s and date between %s and %s",(id, date_int,date_end)))
        orders_serializer = OrderSerializer(orders, many = True)
        return Response(orders_serializer.data)

class SearchDriverAPIView(APIView):

    def post(self, request):
        points = {}
        data = request.data
        date = data['date']
        point = data['point']
        
        drivers = Driver.objects.filter(last_update__in = RawSQL("select last_update from api_driver where last_update != %s and last_update > %s",(date,date))).values('id','x','y')
        for driver_point in drivers:
            d = sqrt((point['x']-driver_point['x'])**2 + (point['y']-driver_point['y'])**2)
            points[driver_point['id']] = d

        pt = sorted(points.items(), key=operator.itemgetter(1))
        print(pt)
        driver = Driver.objects.filter(id = pt[0][0])
        serializer = DriverSerializer(driver, many = True)
        return Response(serializer.data)
    


    
