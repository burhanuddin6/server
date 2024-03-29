# from django.shortcuts import render
from rest_framework import viewsets
from .models import Users, AccountTypes, Notifications, NotificationTypes, Recruiters, Organizations, Candidates, Salaries, Jobs, JobScreens, JobScreenInterviews, ProfileScore, CandidateApplications, CandidateJobScreenRelations, CandidateInterviews, Remarks
from .serializer import UsersSerializer, AccountTypesSerializer, NotificationsSerializer, NotificationTypesSerializer, RecruitersSerializer, OrganizationsSerializer, CandidatesSerializer, SalariesSerializer, JobsSerializer, JobScreensSerializer, JobScreenInterviewsSerializer, ProfileScoreSerializer, CandidateApplicationsSerializer, CandidateJobScreenRelationsSerializer, CandidateInterviewsSerializer, RemarksSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all().order_by('user_id')
    serializer_class = UsersSerializer


class AccountTypesViewSet(viewsets.ModelViewSet):

    queryset = AccountTypes.objects.all().order_by('account_type_id')
    serializer_class = AccountTypesSerializer

class NotificationsViewSet(viewsets.ModelViewSet):

    queryset = Notifications.objects.all().order_by('notif_id')
    serializer_class = NotificationsSerializer

class NotificationTypesViewSet(viewsets.ModelViewSet):
    
    queryset = NotificationTypes.objects.all().order_by('notif_type_id')
    serializer_class = NotificationTypesSerializer

    
class RecruitersViewSet(viewsets.ModelViewSet):
        
    queryset = Recruiters.objects.all().order_by('recruiter_id')
    serializer_class = RecruitersSerializer

class OrganizationsViewSet(viewsets.ModelViewSet):
                
    queryset = Organizations.objects.all().order_by('org_id')
    serializer_class = OrganizationsSerializer

class CandidatesViewSet(viewsets.ModelViewSet):

    queryset = Candidates.objects.all().order_by('candidate_id')
    serializer_class = CandidatesSerializer   

class SalariesViewSet(viewsets.ModelViewSet):

    queryset = Salaries.objects.all().order_by('salary_id')
    serializer_class = SalariesSerializer

class JobsViewSet(viewsets.ModelViewSet):
    
    queryset = Jobs.objects.all().order_by('job_id')
    serializer_class = JobsSerializer

class JobScreensViewSet(viewsets.ModelViewSet):
        
    queryset = JobScreens.objects.all().order_by('job_screen_id')
    serializer_class = JobScreensSerializer

class JobScreenInterviewsViewSet(viewsets.ModelViewSet):
                
    queryset = JobScreenInterviews.objects.all().order_by('job_screen_interview_id')
    serializer_class = JobScreenInterviewsSerializer


class ProfileScoreViewSet(viewsets.ModelViewSet):
    
    queryset = ProfileScore.objects.all().order_by('profile_score_id')
    serializer_class = ProfileScoreSerializer

class CandidateApplicationsViewSet(viewsets.ModelViewSet):
            
    queryset = CandidateApplications.objects.all().order_by('candidate_id')
    serializer_class = CandidateApplicationsSerializer


class CandidateJobScreenRelationsViewSet(viewsets.ModelViewSet):
                    
    queryset = CandidateJobScreenRelations.objects.all().order_by('id')
    serializer_class = CandidateJobScreenRelationsSerializer


class CandidateInterviewsViewSet(viewsets.ModelViewSet):
                        
    queryset = CandidateInterviews.objects.all().order_by('canditate_interview_id')
    serializer_class = CandidateInterviewsSerializer


class RemarksViewSet(viewsets.ModelViewSet):
                                
    queryset = Remarks.objects.all().order_by('remark_id')
    serializer_class = RemarksSerializer