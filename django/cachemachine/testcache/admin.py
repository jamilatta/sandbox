from django.contrib import admin
from cachemachine.testcache.models import *
from django.core.cache import cache 

class ExampleAdmin(admin.ModelAdmin):
    model = Example

    def queryset(self, request):
        cache.clear()
        qs = super(admin.ModelAdmin, self).queryset(request)
        return qs 

admin.site.register(Example, ExampleAdmin)
