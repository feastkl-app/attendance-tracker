from django.contrib.auth.models import User
from django.db import models

class BaseDate(models.Model):
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class BaseType(BaseDate):
    name = models.CharField(max_length=32, blank=False)
    remarks = models.CharField(max_length=64, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class MemberProfile(BaseDate):
    GENDER = ( ('M', 'Male'), ('F', 'Female') )
    MARITAL_STATUS = ( ('S', 'Single'), ('M', 'Married') )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=32, blank=True)
    lastname = models.CharField(max_length=32, blank=True)
    middlename = models.CharField(max_length=32, blank=True)
    remarks = models.CharField(max_length=64, blank=True)
    gender = models.CharField(max_length=8, choices=GENDER) 
    birthdate = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=16, blank=True)
    marital_status = models.CharField(max_length=8, choices=MARITAL_STATUS) 
    member_since = models.DateField(null=True, blank=True)
    active_member = models.BooleanField(default=True)
    location = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name = u"Feast Members"

    def __str__(self):
        return " ".join([self.firstname, self.lastname])

class MemberType(BaseType):
    pass

class MinistryType(BaseType):
    pass

class Ministry(BaseType):
    is_active = models.BooleanField(default=True)
    ministry_type = models.ForeignKey(MinistryType, related_name='ministry')

class MinistryMember(BaseDate):
    member = models.ForeignKey(MemberProfile, related_name='ministry_member')
    ministry = models.ForeignKey(Ministry, related_name='ministry')
    member_type = models.ForeignKey(MemberProfile, related_name='ministry_member_type')

    def __str__(self):
        return "Ministry"

