from django.contrib import admin
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
                path('%s/' % (model._meta.model_name), include(model_admin.urls)),
            ]
        return urlpatterns

# Register your models here.
admin.site.register(Auftragspositionen)
admin.site.register(Auftrag)
admin.site.register(Adressen)
admin.site.register(Rechnungsempfänger)
admin.site.register(Fahrer)
admin.site.register(Help)
admin.site.register(Rechnung)







