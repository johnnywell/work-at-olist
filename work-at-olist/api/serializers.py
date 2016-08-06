from channels.models import Channel, Category
from rest_framework import serializers

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ('url', 'name')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    channel = serializers.HyperlinkedRelatedField(view_name='channel-detail', queryset=Channel.objects.all(), lookup_field='slug')
    parent = serializers.HyperlinkedRelatedField(lookup_field='slug', view_name='category-detail', queryset=Category.objects.all())
    class Meta:
        model = Category
        fields = ('url', 'name', 'channel', 'parent')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
