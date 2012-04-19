from django.contrib import admin
from related1n.models import Publisher, Book

class PublisherAdmin(admin.ModelAdmin):
    pass

admin.site.register(Publisher, PublisherAdmin)

class BookAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)

