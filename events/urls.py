from rest_framework.routers import DefaultRouter

from events.views import CreateEventViewSet

router = DefaultRouter()
router.register(r"", CreateEventViewSet, basename="event")

urlpatterns = router.urls
