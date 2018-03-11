from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

PASSWORD_PREFIX = 'feastkl' #FIX ME

def create_member_profile_user_account(sender, instance, created, **kwargs):
    if created:
        user = instance.create_account()
        instance.user = user
        instance.save()

def delete_member_profile_user_account(sender, instance, **kwargs):
    try:
        instance.user
    except User.DoesNotExist:
        pass
    else:
        instance.user.delete()


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

class MemberType(BaseType):
    # Ex: Member, Head
    pass

class MemberProfile(BaseDate):
    GENDER = ( ('M', 'Male'), ('F', 'Female') )
    MARITAL_STATUS = ( ('S', 'Single'), ('M', 'Married') )

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='member_profile')
    primary_role = models.ForeignKey(MemberType, related_name='primary_role') 
    firstname = models.CharField(max_length=32, blank=False)
    lastname = models.CharField(max_length=32, blank=False)
    middlename = models.CharField(max_length=32, blank=True)
    remarks = models.CharField(max_length=64, blank=True)
    email = models.EmailField(max_length=32, blank=True)
    contact_number1 = models.CharField(max_length=32, blank=True)
    contact_number2 = models.CharField(max_length=32, blank=True)
    gender = models.CharField(max_length=8, choices=GENDER) 
    birthdate = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=16, blank=True)
    marital_status = models.CharField(max_length=8, choices=MARITAL_STATUS) 
    member_since = models.DateField(null=True, blank=True)
    active_member = models.BooleanField(default=True)
    location = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name_plural = u"Feast Members"

    def __str__(self):
        return " ".join([self.firstname, self.lastname])

    def create_account(self):
        username = ''.join([self.firstname.lower().strip(), self.lastname.lower().strip()])

        user, created = User.objects.get_or_create(username=username) 
        if created:
            password = '-'.join([PASSWORD_PREFIX, username])
            user.set_password(password)
            print('creating account method')
            user.save()
        return user

post_save.connect(create_member_profile_user_account, sender=MemberProfile)
post_delete.connect(delete_member_profile_user_account, sender=MemberProfile)

class MinistryType(BaseType):
    # Ex: LG, Ministry, Council, 
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

