
from django.urls import path,include
from .views import *
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'posts',PostsViewsSet)
print(router.urls)
urlpatterns = [
    path('', main,name="main"),
    path("api/",include(router.urls)),


]