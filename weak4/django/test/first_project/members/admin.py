from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display=('first_name','second_name')
admin.site.register(Member,MemberAdmin)
