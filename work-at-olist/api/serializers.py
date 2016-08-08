from channels.models import Channel, Category
from rest_framework import serializers

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    categories = serializers.HyperlinkedIdentityField(view_name='channel-categories', read_only=True, lookup_field='slug')

    class Meta:
        model = Channel
        fields = ('url', 'name', 'categories')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    channel = serializers.HyperlinkedRelatedField(view_name='channel-detail', queryset=Channel.objects.all(), lookup_field='slug')
    parent = serializers.HyperlinkedRelatedField(lookup_field='slug', required=False, view_name='category-detail', queryset=Category.objects.all())
    parents = serializers.HyperlinkedIdentityField(view_name='category-parents', lookup_field='slug', read_only=True)
    children = serializers.HyperlinkedIdentityField(view_name='category-children', lookup_field='slug', read_only=True)

    class Meta:
        model = Category
        fields = ('url', 'name', 'channel', 'parent', 'parents', 'children')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
