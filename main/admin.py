from django.contrib import admin
from .models import Book, Influencer, Tag
# Register your models here.


@admin.register(Influencer)
class InfluencerAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['title_pt','title_en']

admin.site.register(Tag)