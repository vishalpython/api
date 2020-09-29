from django.urls import path,include
from .views import HelloApiView,HelloViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("hello-api",HelloViewset, base_name = "hello-api")


urlpatterns = [
path('hello/',HelloApiView.as_view()),
path('',include(router.urls))
]
