from rest_framework.routers import DefaultRouter

from api.views import UserModelViewSet, HotelModelViewSet, RoomModelViewSet, BookingModelViewSet

router = DefaultRouter()
router.register('user', UserModelViewSet)
router.register('hotels', HotelModelViewSet)
router.register('rooms', RoomModelViewSet)
router.register('bookings', BookingModelViewSet)

urlpatterns = [

]

urlpatterns.extend(router.urls)