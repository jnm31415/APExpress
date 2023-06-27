from django.contrib import admin
from django.urls import path,include
from .models import Auftrag
from .models import Auftragspositionen
from .models import Rechnungsempfänger
from .models import Adressen
from .models import Fahrer
from .models import Rechnung
from .models import Help



class MyAdminSite(admin.AdminSite):
    def get_urls(self):
        urlpatterns = super().get_urls()
        for model, model_admin in self._registry.items():
            urlpatterns += [
                path('%s/' % 'Aufträge/'+(model._meta.model_name), include(model_admin.urls)),
            ]
        return urlpatterns

admin_view = MyAdminSite()
admin_view.register(Auftrag)
admin_view.register(Auftragspositionen)
admin_view.register(Rechnungsempfänger)
admin_view.register(Adressen)
admin_view.register(Fahrer)
admin_view.register(Rechnung)
admin_view.register(Help)

'''
admin.site.register(Auftragspositionen)
admin.site.register(Auftrag)
admin.site.register(Adressen)
admin.site.register(Rechnungsempfänger)
admin.site.register(Fahrer)
admin.site.register(Help)
admin.site.register(Rechnung)
'''






