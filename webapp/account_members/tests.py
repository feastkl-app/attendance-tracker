from django.test import TestCase

from utility.factories import MemberProfileFactory 

from .models import MemberProfile


class CreateMemberProfileTests(TestCase):

    def test_create_member_profile_via_pk(self):
        member_profile = MemberProfileFactory()
        member_profile_obj = MemberProfile.objects.get(pk=member_profile.pk)
        self.assertEquals(member_profile.pk, member_profile_obj.pk)

    def test_create_single_member_profile(self):
        member_profile = MemberProfileFactory()
        count = MemberProfile.objects.count()
        self.assertEquals(count, 1)

        


