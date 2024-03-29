from rest_framework import serializers
from .models import Users
from .models import AccountTypes
from .models import Notifications
from .models import NotificationTypes, Recruiters, Organizations, Candidates, Salaries, Jobs, JobScreens, JobScreenInterviews, ProfileScore, CandidateApplications, CandidateJobScreenRelations, CandidateInterviews, Remarks

class UsersSerializer(serializers.ModelSerializer):
    "Users serializer"
    class Meta:
        model = Users
        fields = '__all__'


class AccountTypesSerializer(serializers.ModelSerializer):
    "AccountTypes serializer"
    class Meta:
        model = AccountTypes
        fields = '__all__'


class NotificationsSerializer(serializers.ModelSerializer):
    "Notifications serializer"
    class Meta:
        model = Notifications
        fields = '__all__'

    
class NotificationTypesSerializer(serializers.ModelSerializer):
    "NotificationTypes serializer"
    class Meta:
        model = NotificationTypes
        fields = '__all__'


class RecruitersSerializer(serializers.ModelSerializer):
    "Recruiters serializer"
    class Meta:
        model = Recruiters
        fields = '__all__'


class OrganizationsSerializer(serializers.ModelSerializer):
    "Organizations serializer"
    class Meta:
        model = Organizations
        fields = '__all__'


class CandidatesSerializer(serializers.ModelSerializer):
    "Candidates serializer"
    class Meta:
        model = Candidates
        fields = '__all__'


class SalariesSerializer(serializers.ModelSerializer):
    "Salaries serializer"
    class Meta:
        model = Salaries
        fields = '__all__'


class JobsSerializer(serializers.ModelSerializer):
    "Jobs serializer"
    class Meta:
        model = Jobs
        fields = '__all__'


class JobScreensSerializer(serializers.ModelSerializer):
    "JobScreens serializer"
    class Meta:
        model = JobScreens
        fields = '__all__'


class JobScreenInterviewsSerializer(serializers.ModelSerializer):
    "JobScreenInterviews serializer"
    class Meta:
        model = JobScreenInterviews
        fields = '__all__'


class ProfileScoreSerializer(serializers.ModelSerializer):
    "ProfileScore serializer"
    class Meta:
        model = ProfileScore
        fields = '__all__'

    
class CandidateApplicationsSerializer(serializers.ModelSerializer):
    "CandidateApplications serializer"
    class Meta:
        model = CandidateApplications
        fields = '__all__'


class CandidateJobScreenRelationsSerializer(serializers.ModelSerializer):

    "CandidateJobScreenRelations serializer"
    class Meta:
        model = CandidateJobScreenRelations
        fields = '__all__'


class CandidateInterviewsSerializer(serializers.ModelSerializer):
    "CandidateInterviews serializer"
    class Meta:
        model = CandidateInterviews
        fields = '__all__'


class RemarksSerializer(serializers.ModelSerializer):
    "Remarks serializer"
    class Meta:
        model = Remarks
        fields = '__all__'


