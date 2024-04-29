from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from .views import AccountTypeViewSet, NotificationViewSet, \
NotificationTypeViewSet, RecruiterViewSet, OrganizationViewSet, \
CandidateViewSet, SalaryViewSet, JobsViewSet, JobScreenViewSet, \
JobScreenInterviewViewSet, ProfileScoreViewSet, CandidateApplicationViewSet, \
CandidateJobScreenRelationViewSet, CandidateInterviewViewSet, RemarkViewSet, CreateCandidateAPIView

from .views import CandidateApplicationDetailView


router = DefaultRouter()
router.register(r'account_types', AccountTypeViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'notification_types', NotificationTypeViewSet)
router.register(r'recruiters', RecruiterViewSet)
router.register(r'organizations', OrganizationViewSet)
router.register(r'candidates', CandidateViewSet)
router.register(r'salaries', SalaryViewSet)
router.register(r'jobs', JobsViewSet)
router.register(r'job_screens', JobScreenViewSet)
router.register(r'job_screen_interviews', JobScreenInterviewViewSet)
router.register(r'profile_score', ProfileScoreViewSet)
router.register(r'candidate_applications', CandidateApplicationViewSet)
router.register(r'candidate_job_screen_relations', CandidateJobScreenRelationViewSet)
router.register(r'candidate_interviews', CandidateInterviewViewSet)
router.register(r'remarks', RemarkViewSet)





urlpatterns = [
    path('api/', include(router.urls)),
    # bootstrapping authentication: powerful, but not the focus of this project
    path('api/accounts/', include('authemail.urls')),
    path('api/candidate_applications_detail/<int:pk>/', CandidateApplicationDetailView.as_view(), name='candidate_application_detail'),
    path('api/create-candidate/', CreateCandidateAPIView.as_view(), name='create_candidate'),
]