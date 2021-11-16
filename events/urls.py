from django.urls.conf import path

from events.views import CreateEventApiView

urlpatterns = [
    path(
        "",
        CreateEventApiView.as_view(),
        name="create-event",
    ),
]
