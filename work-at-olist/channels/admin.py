from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from channels.models import Channel, Category

admin.site.register(Channel, admin.ModelAdmin)
admin.site.register(Category, MPTTModelAdmin)
