from rest_framework import viewsets
from api.serializers import ChannelSerializer, CategorySerializer
from channels.models import Channel, Category
from rest_framework.decorators import detail_route, list_route

class ChannelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows channels to be viewed or edited.
    """
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    lookup_field = 'slug'

    @detail_route()
    def categories(self, request, slug=None):
        categories = self.get_object().categories.all()
        page = self.paginate_queryset(categories)
        if page is not None:
            serializer = CategorySerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    @detail_route()
    def parents(self, request, slug=None):
        parents = self.get_object().get_ancestors()
        page = self.paginate_queryset(parents)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(parents, many=True)
        return Response(serializer.data)

    @detail_route()
    def children(self, request, slug=None):
        children = self.get_object().get_descendants()
        page = self.paginate_queryset(children)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(parents, many=True)
        return Response(serializer.data)
