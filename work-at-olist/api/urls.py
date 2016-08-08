from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'channels', views.ChannelViewSet)
router.register(r'categories', views.CategoryViewSet)

channel_categories = views.ChannelViewSet.as_view({'get': 'categories'})

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^/channels/(?P<slug>[\w-]+)/categories/$', channel_categories, name='channel-categories')
]
