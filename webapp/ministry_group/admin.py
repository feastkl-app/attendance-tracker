from django.contrib import admin
from .models import (
    MinistryType,
    Ministry,
    MinistryMember,
    MinistryMemberGroup,
)

admin.site.register(MinistryType)
admin.site.register(Ministry)
admin.site.register(MinistryMember)
admin.site.register(MinistryMemberGroup)

