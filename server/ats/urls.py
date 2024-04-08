from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountTypeViewSet, NotificationViewSet, NotificationTypeViewSet, RecruiterViewSet, OrganizationViewSet, CandidateViewSet, SalaryViewSet, JobsViewSet, JobScreenViewSet, JobScreenInterviewViewSet, ProfileScoreViewSet, CandidateApplicationViewSet, CandidateJobScreenRelationViewSet, CandidateInterviewViewSet, RemarkViewSet

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
    path('', include(router.urls)),
    # bootstrapping authentication: powerful, but not the focus of this project
    path('api/accounts/', include('authemail.urls')),
]