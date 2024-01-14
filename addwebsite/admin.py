from django.contrib import admin
from addwebsite.models import Addweb
# Register your models here.

class AddwebAdmin(admin.ModelAdmin):

    list_display = ('web_name','web_description','web_url')

admin.site.register(Addweb,AddwebAdmin)