# customadminapp/admin.py
from django.contrib import admin

class CustomAdminSite(admin.AdminSite):
    site_header = 'Custom Admin Panel'
    site_title = 'Custom Admin'
    index_title = 'Welcome to the Custom Admin Panel'

custom_admin_site = CustomAdminSite(name='customadmin')
