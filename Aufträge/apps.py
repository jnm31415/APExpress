from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class AufträgeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Aufträge'

class MyAdminConfig(AdminConfig):
    default_site = 'myproject.admin.MyAdminSite'
