from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

class Channel(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    slug = models.SlugField(unique=True, blank=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

    def create_categories_from_list(self, categories):
        parent = None
        for category in categories:
            parent, created = Category.objects.get_or_create(name=category,
                channel=self, parent=parent)


class Category(MPTTModel):
    name = models.CharField(max_length=50)
    channel = models.ForeignKey(Channel, related_name='categories')
    parent = TreeForeignKey('self', null=True, blank=True,
    related_name='children', db_index=True)
    slug = models.SlugField(unique=True, blank=False, db_index=True)

    def save(self, *args, **kwargs):
        if self.parent:
            slug = "{}-{}-{}".format(self.channel, self.parent.name, self.name)
        else:
            slug = "{}-{}".format(self.channel, self.name)
        self.slug = slugify(slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return "{}: {}".format(self.channel, self.name)

    class Meta:
        unique_together = ('channel', 'name', 'parent')
        verbose_name_plural = _('Categories')

    class MPTTMeta:
        order_insertion_by = ['name']
