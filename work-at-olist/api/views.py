from rest_framework import viewsets
from api.serializers import ChannelSerializer, CategorySerializer
from channels.models import Channel, Category

class ChannelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows channels to be viewed or edited.
    """
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    lookup_field = 'slug'


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
