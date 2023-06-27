from django.apps import AppConfig
from django.contrib.admin import apps

class AufträgeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Aufträge'
    verbose_name = 'Auftraege'


'''
class MyAdminConfig(apps.AdminConfig):
    default_site = 'Aufträge.admin.MyAdminSite'
'''
