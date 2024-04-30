from rest_framework import serializers

from .models import AccountType, Notification, NotificationType, Recruiter, \
Organization, Candidate, Salary, Job, JobScreen, JobScreenInterview, \
ProfileScore, CandidateApplication, CandidateJobScreenRelation, \
CandidateInterview, Remark

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


class CustomCandidateSerializer(serializers.ModelSerializer):
    applications = serializers.SerializerMethodField()
    job_screen_relations = serializers.SerializerMethodField()
    interviews = serializers.SerializerMethodField()
    remarks = serializers.SerializerMethodField()

    class Meta:
        model = Candidate
        fields = ['candidate_id', 'first_name', 'last_name', 'email', 'country', 'phone', 'linkedin_url', 'applications', 'job_screen_relations', 'interviews', 'remarks']

    def get_applications(self, obj):
        applications = CandidateApplication.objects.filter(candidate_id=obj)
        return CandidateApplicationSerializer(applications, many=True).data

    def get_job_screen_relations(self, obj):
        relations = CandidateJobScreenRelation.objects.filter(application_id__candidate_id=obj)
        return CandidateJobScreenRelationSerializer(relations, many=True).data

    def get_interviews(self, obj):
        interviews = CandidateInterview.objects.filter(candidate_application_id__candidate_id=obj)
        return CandidateInterviewSerializer(interviews, many=True).data

    def get_remarks(self, obj):
        remarks = Remark.objects.filter(candidate_job_screen_relation_id__application_id__candidate_id=obj)
        return RemarkSerializer(remarks, many=True).data
    

class CustomJobSerializer(serializers.ModelSerializer):
    recruiter = serializers.SerializerMethodField()
    job_screens = serializers.SerializerMethodField()
    candidate_applications = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = ['job_id', 'creater_id', 'job_title', 'overview', 'work_site', 'work_type', 'is_open', 'posted_on', 'recruiter', 'job_screens', 'candidate_applications']

    def get_recruiter(self, obj):
        recruiter = Recruiter.objects.get(recruiter_id=obj.creater_id_id)
        return RecruiterSerializer(recruiter).data

    def get_job_screens(self, obj):
        job_screens = JobScreen.objects.filter(job_id=obj)
        return JobScreenSerializer(job_screens, many=True).data

    def get_candidate_applications(self, obj):
        candidate_applications = CandidateApplication.objects.filter(job_id=obj)
        return CandidateApplicationSerializer(candidate_applications, many=True).data



class CustomCandidateApplicationSerializer(serializers.ModelSerializer):
    job_screen_relations = serializers.SerializerMethodField()
    interviews = serializers.SerializerMethodField()
    remarks = serializers.SerializerMethodField()

    class Meta:
        model = CandidateApplication
        fields = ['application_id', 'candidate_id', 'job_id', 'profile_score_id', 'resume_file', 'applied_on', 'job_screen_relations', 'interviews', 'remarks']

    def get_job_screen_relations(self, obj):
        relations = CandidateJobScreenRelation.objects.filter(application_id=obj)
        return CandidateJobScreenRelationSerializer(relations, many=True).data

    def get_interviews(self, obj):
        interviews = CandidateInterview.objects.filter(candidate_application_id=obj)
        return CandidateInterviewSerializer(interviews, many=True).data

    def get_remarks(self, obj):
        remarks = Remark.objects.filter(candidate_job_screen_relation_id__application_id=obj)
        return RemarkSerializer(remarks, many=True).data