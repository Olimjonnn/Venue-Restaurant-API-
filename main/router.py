from rest_framework import routers
from main.views import *

router = routers.DefaultRouter()

router.register('logo', LogoView)
router.register('slider', SliderView)
router.register('info', InfoView)
router.register('video', VideoView)
router.register('category', CategoryView)
router.register('food', FoodView)
router.register('advertisement', AdvertisementView)
router.register('client', ClientView)
router.register('order', OrderView)
router.register('reservation', ReservationView)
router.register('aboutus', AboutUsView)