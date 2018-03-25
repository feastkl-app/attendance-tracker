from django.contrib import admin
from .models import (
    MinistryType,
    Ministry,
    MinistryMember,
)

admin.site.register(MinistryType)
admin.site.register(Ministry)
admin.site.register(MinistryMember)

