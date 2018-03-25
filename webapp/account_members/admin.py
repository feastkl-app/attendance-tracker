from django.contrib import admin
from .models import (
    MemberType,
    MemberProfile,
)

admin.site.register(MemberType)
admin.site.register(MemberProfile)
admin.site.site_header = 'Feast KL Attendance Tracking System (FEKLATS)'

