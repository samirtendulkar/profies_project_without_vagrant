from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, base_name="hello-viewset")
router.register("profile", views.UserProfileViewSets)
router.register("login", views.LoginViewSet, base_name="login")
router.register("feed", views.UserProfileFeedViewSets)


urlpatterns = [
    url(r'^hello-view/$', views.HelloApiView.as_view(), name="hello_view"),
    url(r'', include(router.urls))
]

