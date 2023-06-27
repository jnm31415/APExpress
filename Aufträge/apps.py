from django.apps import AppConfig
from django.contrib.admin import AdminConfig

class AufträgeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Aufträge'

class MyAdminConfig(AdminConfig):
    default_site = 'Aufträge.admin.MyAdminSite'
