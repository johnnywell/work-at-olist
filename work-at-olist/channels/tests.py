from django.test import TestCase
from channels.models import Channel, Category
from django.utils.text import slugify

class ChannelTestCase(TestCase):

    def test_slug_creation_rule(self):
        """
        The slug is very important on this application,
        so we must garantee its formation rule is correct.
        """
        name = "Amazon"
        channel = Channel.objects.create(name=name)
        self.assertEqual(channel.slug, self.construct_slug(channel))

    def construct_slug(self, channel):
        return slugify(channel.name)


class CategoryTestCase(TestCase):

    def setUp(self):
        channel = Channel.objects.create(name="Amazon")

    def test_slug_creation_rule(self):
        name = 'Science Fiction'
        channel = Channel.objects.get(name="Amazon")
        parent = Category.objects.create(name="Books", channel=channel)
        self.assertEqual(parent.slug, self.construct_slug(parent))
        category = Category.objects.create(name=name, channel=channel, parent=parent)
        self.assertEqual(category.slug, self.construct_slug(category))

    def construct_slug(self, category):
        if category.parent:
            slug = "{}-{}-{}".format(category.channel, category.parent.name, category.name)
        else:
            slug = "{}-{}".format(category.channel, category.name)
        return slugify(slug)
