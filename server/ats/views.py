# from django.shortcuts import render
from rest_framework import viewsets

from .models import AccountType, Notification, NotificationType, \
Recruiter, Organization, Candidate, Salary, Job, JobScreen, \
JobScreenInterview, ProfileScore, CandidateApplication, \
CandidateJobScreenRelation, CandidateInterview, Remark

from .serializer import AccountTypeSerializer, NotificationSerializer, \
NotificationTypeSerializer, RecruiterSerializer, OrganizationSerializer, \
CandidateSerializer, SalarySerializer, JobSerializer, JobScreenSerializer, \
JobScreenInterviewSerializer, ProfileScoreSerializer, \
CandidateApplicationSerializer, CandidateJobScreenRelationSerializer, \
CandidateInterviewSerializer, RemarkSerializer

class AccountTypeViewSet(viewsets.ModelViewSet):
    '''Default viewset for AccountType model.'''
    queryset = AccountType.objects.all().order_by('account_type_id')
    serializer_class = AccountTypeSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    '''Default viewset for Notification model.'''
    queryset = Notification.objects.all().order_by('notif_id')
    serializer_class = NotificationSerializer

class NotificationTypeViewSet(viewsets.ModelViewSet):
    '''Default viewset for NotificationType model.'''
    queryset = NotificationType.objects.all().order_by('notif_type_id')
    serializer_class = NotificationTypeSerializer

    
class RecruiterViewSet(viewsets.ModelViewSet):
    '''Default viewset for Recruiter model.'''
    queryset = Recruiter.objects.all().order_by('recruiter_id')
    serializer_class = RecruiterSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    '''Default viewset for Organization model.'''
    queryset = Organization.objects.all().order_by('org_id')
    serializer_class = OrganizationSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    '''Default viewset for Candidate model.'''
    queryset = Candidate.objects.all().order_by('candidate_id')
    serializer_class = CandidateSerializer   

class SalaryViewSet(viewsets.ModelViewSet):
    '''Default viewset for Salary model.'''
    queryset = Salary.objects.all().order_by('salary_id')
    serializer_class = SalarySerializer

class JobsViewSet(viewsets.ModelViewSet):
    '''Default viewset for Job model.'''
    queryset = Job.objects.all().order_by('job_id')
    serializer_class = JobSerializer

class JobScreenViewSet(viewsets.ModelViewSet):
    '''Default viewset for JobScreen model.'''
    queryset = JobScreen.objects.all().order_by('job_screen_id')
    serializer_class = JobScreenSerializer

class JobScreenInterviewViewSet(viewsets.ModelViewSet):
    '''Default viewset for JobScreenInterview model.'''
    queryset = JobScreenInterview.objects.all().order_by('job_screen_interview_id')
    serializer_class = JobScreenInterviewSerializer


class ProfileScoreViewSet(viewsets.ModelViewSet):
    '''Defualt viewset for ProfileScore model'''
    queryset = ProfileScore.objects.all().order_by('profile_score_id')
    serializer_class = ProfileScoreSerializer

class CandidateApplicationViewSet(viewsets.ModelViewSet):
    '''Defualt viewset for CandidateApplication viewset'''
    queryset = CandidateApplication.objects.all().order_by('candidate_id')
    serializer_class = CandidateApplicationSerializer


class CandidateJobScreenRelationViewSet(viewsets.ModelViewSet):
    '''Defualt viewset for CandidateJobScreenRelation viewset'''
    queryset = \
    CandidateJobScreenRelation.objects.all().order_by('id')
    serializer_class = CandidateJobScreenRelationSerializer


class CandidateInterviewViewSet(viewsets.ModelViewSet):
    '''Default viewset for CandidateInterview model.'''
    queryset = \
    CandidateInterview.objects.all().order_by('canditate_interview_id')
    serializer_class = CandidateInterviewSerializer


class RemarkViewSet(viewsets.ModelViewSet):
    '''Default viewset for Remark model'''
    queryset = Remark.objects.all().order_by('remark_id')
    serializer_class = RemarkSerializer