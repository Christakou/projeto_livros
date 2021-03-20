from django.contrib import admin
from .models import Book, Influencer, Tag
# Register your models here.


@admin.register(Influencer)
class InfluencerAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Book)
admin.site.register(Tag)