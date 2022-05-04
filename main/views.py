from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from main.serializer import *
from main.models import *

# Functions

# Logo Get

class LogoView(viewsets.ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer

    http_method_names = ['get']
    def list(self, request):
        logo = Logo.objects.last()
        log = LogoSerializer(logo)
        return Response(log.data)

# Slider Get

class SliderView(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

    http_method_names = ['get']
    def list(self, request):
        logo = Slider.objects.last()
        log = SliderSerializer(logo)
        return Response(log.data)

# Info Get

class InfoView(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

    http_method_names = ['get']
    def list(self, request):
        logo = Info.objects.last()
        log = InfoSerializer(logo)
        return Response(log.data)

# Video Get

class VideoView(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    http_method_names = ['get']
    def list(self, request):
        logo = Video.objects.last()
        log = VideoSerializer(logo)
        return Response(log.data)

# Categories GET

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AdvertisementView(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    http_method_names = ['get']
    def list(self, request):
        adver = Advertisement.objects.first()
        ad = AdvertisementSerializer(adver)
        return Response(ad.data)


class FoodView(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    # PROBLEEEm
    def create(self, request):
        try:
            category = request.POST.get('category')
            name = request.POST.get('name')
            price = request.POST.get('price')
            products = request.POST.get('products')
            image = request.FILES.get('image')
            title1 = request.POST.get('title1')
            title2 = request.POST.get('title2')
            stars = request.POST.get('stars')
            Food.objects.create(category_id=category, name=name, price=price, products=products, image=image, title1=title1, title2=title2, stars=stars)
            return Response({"Added"})
        except Exception as arr:
            data = {
                'error': f"{arr}"
            }
            return Response(data)

    @action(['GET'], detail=False)
    def find(self, request):
        category = request.GET.get("category")
        cat = Food.objects.filter(category_id=category)
        ct = FoodSerializer(cat, many=True)
        return Response(ct.data)
    # PROBLEEEm

class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CashView(viewsets.ModelViewSet):
    queryset = Cash.objects.all()
    serializer_class = CashSerializer

    http_method_names = ['get']


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request):
        try:
            client_id = request.POST.get("client")
            food_id = request.POST.get("food")
            quantity = request.POST.get("quantity")
            price = request.POST.get("price")
            Order.objects.create(client_id=client_id, food_id=food_id, quantity=quantity, price=price)
            client = Client.objects.get(id=client_id)
            client.debt += int(quantity)*int(price)
            client.save()
            return Response({"Ordered"})
        except Exception as arr:
            data = {
                "error": f"{arr}"
            }
            return Response(data)

    @action(['POST'], detail=False)
    def delete(self, request):
        client_id = request.POST.get("client")
        food_id = request.POST.get("food")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        price = request.POST.get("price")
        Order.objects.create(client_id=client_id, food_id=food_id, quantity=quantity,price=price)
        client = Client.objects.get(id=client_id)
        client.debt -= int(quantity)*int(price)        
        client.save()
        cash = Cash.objects.first()
        cash.cash += int(quantity)*int(price)
        cash.save()
        return Response("Deleted")
    @action(['GET'], detail=False)
    def sss(self, request):
        client = request.GET.get('client')
        order = Order.objects.filter(client_id=client)
        ord = OrderSerializer(order, many=True)
        return Response(ord.data)



class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    http_method_names = ['post']
    def create(self, request):
        date = request.data['date']
        time = request.data['time']
        reserv = request.data['reserv']
        Reservation.objects.create(date=date, time=time, reserv=reserv)
        return Response({"Booked"})


class AboutUsView(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer