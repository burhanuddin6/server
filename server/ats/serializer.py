from rest_framework import serializers

from .models import User, AccountType, Notification, NotificationType, Recruiter, Organization, Candidate, Salary, Job, JobScreen, JobScreenInterview, ProfileScore, CandidateApplication, CandidateJobScreenRelation, CandidateInterview, Remark

# class UserSerializer(serializers.ModelSerializer):
#     "User serializer"
#     class Meta:
#         model = User
#         fields = '__all__'


class AccountTypeSerializer(serializers.ModelSerializer):
    "AccountType serializer"
    class Meta:
        model = AccountType
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    "Notification serializer"
    class Meta:
        model = Notification
        fields = '__all__'

    
class NotificationTypeSerializer(serializers.ModelSerializer):
    "NotificationType serializer"
    class Meta:
        model = NotificationType
        fields = '__all__'


class RecruiterSerializer(serializers.ModelSerializer):
    "Recruiter serializer"
    class Meta:
        model = Recruiter
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    "Organization serializer"
    class Meta:
        model = Organization
        fields = '__all__'


class CandidateSerializer(serializers.ModelSerializer):
    "Candidate serializer"
    class Meta:
        model = Candidate
        fields = '__all__'


class SalarySerializer(serializers.ModelSerializer):
    "Salary serializer"
    class Meta:
        model = Salary
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    "Job serializer"
    class Meta:
        model = Job
        fields = '__all__'


class JobScreenSerializer(serializers.ModelSerializer):
    "JobScreen serializer"
    class Meta:
        model = JobScreen
        fields = '__all__'


class JobScreenInterviewSerializer(serializers.ModelSerializer):
    "JobScreenInterview serializer"
    class Meta:
        model = JobScreenInterview
        fields = '__all__'


class ProfileScoreSerializer(serializers.ModelSerializer):
    "ProfileScore serializer"
    class Meta:
        model = ProfileScore
        fields = '__all__'

    
class CandidateApplicationSerializer(serializers.ModelSerializer):
    "CandidateApplications serializer"
    class Meta:
        model = CandidateApplication
        fields = '__all__'


class CandidateJobScreenRelationSerializer(serializers.ModelSerializer):

    "CandidateJobScreenRelation serializer"
    class Meta:
        model = CandidateJobScreenRelation
        fields = '__all__'


class CandidateInterviewSerializer(serializers.ModelSerializer):
    "CandidateInterview serializer"
    class Meta:
        model = CandidateInterview
        fields = '__all__'


class RemarkSerializer(serializers.ModelSerializer):
    "Remark serializer"
    class Meta:
        model = Remark
        fields = '__all__'


