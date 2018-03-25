from django.db import models
from account_members.models import MemberProfile, MemberType
from utility.models import AbstractBaseDate, AbstractBaseType

# Create your models here.
class MinistryType(AbstractBaseType):
    # Ex: LG, Ministry, Council, 
    pass

class Ministry(AbstractBaseType):
    is_active = models.BooleanField(default=True)
    ministry_type = models.ForeignKey(MinistryType, related_name='ministry_type')

    class Meta:
        verbose_name_plural = u"Ministries"

class MinistryMember(AbstractBaseDate):
    member = models.ForeignKey(MemberProfile, related_name='ministry_member')
    ministry = models.ForeignKey(Ministry, related_name='ministry')
    member_type = models.ForeignKey(MemberType, related_name='ministry_member_type')

    def __str__(self):
        return "Ministry"

