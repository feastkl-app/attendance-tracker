from django.contrib import admin
from .models import (
    MemberType,
    MemberProfile,
    MinistryType,
    Ministry,
    MinistryMember,
)

admin.site.register(MemberType)
admin.site.register(MemberProfile)
admin.site.register(MinistryType)
admin.site.register(Ministry)
admin.site.register(MinistryMember)
admin.site.site_header = 'FEKLATS'

# Register your models here.
