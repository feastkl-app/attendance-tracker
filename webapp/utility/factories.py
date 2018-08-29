import factory
from faker import Factory

from account_members.models import MemberProfile, MemberType 

faker = Factory.create()


class MemberTypeFactory(factory.DjangoModelFactory):
    class Meta:
        model = MemberType

    name = u'Regular Member'
    remarks = ' '.join(faker.words())


class MemberProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = MemberProfile

    primary_role = factory.SubFactory(MemberTypeFactory)
    firstname = factory.LazyAttribute(lambda _: faker.first_name())
    lastname = faker.last_name()
    contact_number1 = faker.phone_number()
    contact_number2 = faker.phone_number()
    email = faker.email()
    gender = u'Male' 
    birthdate = faker.date_this_century(before_today=True, after_today=False)
    nationality = u'Filipino'
    marital_status = u'Single'
    location = faker.street_address()
    member_since = faker.date_this_century(before_today=True, after_today=False)
#    factory.LazyAttribute(lambda _: faker.word())

    #user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='member_profile')
    #primary_role = models.ForeignKey(MemberType, related_name='primary_role') 
    #firstname = models.CharField(max_length=32, blank=False)
    #lastname = models.CharField(max_length=32, blank=False)
    #middlename = models.CharField(max_length=32, blank=True)
    #remarks = models.CharField(max_length=64, blank=True)
    #email = models.EmailField(max_length=32, blank=True)
    #contact_number1 = models.CharField(max_length=32, blank=True)
    #contact_number2 = models.CharField(max_length=32, blank=True)
    #gender = models.CharField(max_length=8, choices=GENDER) 
    #birthdate = models.DateField(null=True, blank=True)
    #nationality = models.CharField(max_length=16, blank=True)
    #marital_status = models.CharField(max_length=8, choices=MARITAL_STATUS) 
    #member_since = models.DateField(null=True, blank=True)
    #active_member = models.BooleanField(default=True)
    #location = models.CharField(max_length=64, blank=True)
