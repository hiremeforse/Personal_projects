from django.contrib import admin
from .models import Youtuber

# Register your models here.

class Ytadmin(admin.ModelAdmin):
    list_display = ('id','name','subs_count')
    serach_fields = ('name','camera_type')
    list_filter = ('city', )
    list_display_links = ('id', 'name')


admin.site.register(Youtuber, Ytadmin)
