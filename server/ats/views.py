# from django.shortcuts import render
from rest_framework import viewsets
from .models import User, AccountType, Notification, NotificationType, Recruiter, Organization, Candidate, Salary, Job, JobScreen, JobScreenInterview, ProfileScore, CandidateApplication, CandidateJobScreenRelation, CandidateInterview, Remark
from .serializer import AccountTypeSerializer, NotificationSerializer, NotificationTypeSerializer, RecruiterSerializer, OrganizationSerializer, CandidateSerializer, SalarySerializer, JobSerializer, JobScreenSerializer, JobScreenInterviewSerializer, ProfileScoreSerializer, CandidateApplicationSerializer, CandidateJobScreenRelationSerializer, CandidateInterviewSerializer, RemarkSerializer
# Create your views here.

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows user to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('user_id')
#     serializer_class = UserSerializer


class AccountTypeViewSet(viewsets.ModelViewSet):

    queryset = AccountType.objects.all().order_by('account_type_id')
    serializer_class = AccountTypeSerializer

class NotificationViewSet(viewsets.ModelViewSet):

    queryset = Notification.objects.all().order_by('notif_id')
    serializer_class = NotificationSerializer

class NotificationTypeViewSet(viewsets.ModelViewSet):
    
    queryset = NotificationType.objects.all().order_by('notif_type_id')
    serializer_class = NotificationTypeSerializer

    
class RecruiterViewSet(viewsets.ModelViewSet):
        
    queryset = Recruiter.objects.all().order_by('recruiter_id')
    serializer_class = RecruiterSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
                
    queryset = Organization.objects.all().order_by('org_id')
    serializer_class = OrganizationSerializer

class CandidateViewSet(viewsets.ModelViewSet):

    queryset = Candidate.objects.all().order_by('candidate_id')
    serializer_class = CandidateSerializer   

class SalaryViewSet(viewsets.ModelViewSet):

    queryset = Salary.objects.all().order_by('salary_id')
    serializer_class = SalarySerializer

class JobsViewSet(viewsets.ModelViewSet):
    
    queryset = Job.objects.all().order_by('job_id')
    serializer_class = JobSerializer

class JobScreenViewSet(viewsets.ModelViewSet):
        
    queryset = JobScreen.objects.all().order_by('job_screen_id')
    serializer_class = JobScreenSerializer

class JobScreenInterviewViewSet(viewsets.ModelViewSet):
                
    queryset = JobScreenInterview.objects.all().order_by('job_screen_interview_id')
    serializer_class = JobScreenInterviewSerializer


class ProfileScoreViewSet(viewsets.ModelViewSet):
    
    queryset = ProfileScore.objects.all().order_by('profile_score_id')
    serializer_class = ProfileScoreSerializer

class CandidateApplicationViewSet(viewsets.ModelViewSet):
            
    queryset = CandidateApplication.objects.all().order_by('candidate_id')
    serializer_class = CandidateApplicationSerializer


class CandidateJobScreenRelationViewSet(viewsets.ModelViewSet):
                    
    queryset = CandidateJobScreenRelation.objects.all().order_by('id')
    serializer_class = CandidateJobScreenRelationSerializer


class CandidateInterviewViewSet(viewsets.ModelViewSet):
                        
    queryset = CandidateInterview.objects.all().order_by('canditate_interview_id')
    serializer_class = CandidateInterviewSerializer


class RemarkViewSet(viewsets.ModelViewSet):
                                
    queryset = Remark.objects.all().order_by('remark_id')
    serializer_class = RemarkSerializer