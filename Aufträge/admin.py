from django.contrib import admin
from .models import Auftrag
from .models import Auftragspositionen
from .models import Rechnungsempfänger
from .models import Adressen
from .models import Fahrer
from .models import Rechnung
from .models import Help

# Register your models here.
admin.site.register(Auftragspositionen)
admin.site.register(Auftrag)
admin.site.register(Adressen)
admin.site.register(Rechnungsempfänger)
admin.site.register(Fahrer)
admin.site.register(Help)
admin.site.register(Rechnung)
