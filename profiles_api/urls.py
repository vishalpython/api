from django.urls import path,include
from .views import HelloApiView,HelloViewset,UserProfileViewset,ObtainAuthToken,UserLoginApiView,UserProfileFeedViewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("hello-api",HelloViewset, base_name = "hello-api")
router.register("profile",UserProfileViewset)
router.register("feed",UserProfileFeedViewsets)


urlpatterns = [
path('hello/',HelloApiView.as_view()),
path('login/',UserLoginApiView.as_view()),
path('',include(router.urls))
]
