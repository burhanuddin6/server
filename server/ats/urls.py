from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AccountTypesViewSet, NotificationsViewSet, NotificationTypesViewSet, RecruitersViewSet, OrganizationsViewSet, CandidatesViewSet, SalariesViewSet, JobsViewSet, JobScreensViewSet, JobScreenInterviewsViewSet, ProfileScoreViewSet, CandidateApplicationsViewSet, CandidateJobScreenRelationsViewSet, CandidateInterviewsViewSet, RemarksViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'account_types', AccountTypesViewSet)
router.register(r'notifications', NotificationsViewSet)
router.register(r'notification_types', NotificationTypesViewSet)
router.register(r'recruiters', RecruitersViewSet)
router.register(r'organizations', OrganizationsViewSet)
router.register(r'candidates', CandidatesViewSet)
router.register(r'salaries', SalariesViewSet)
router.register(r'jobs', JobsViewSet)
router.register(r'job_screens', JobScreensViewSet)
router.register(r'job_screen_interviews', JobScreenInterviewsViewSet)
router.register(r'profile_score', ProfileScoreViewSet)
router.register(r'candidate_applications', CandidateApplicationsViewSet)
router.register(r'candidate_job_screen_relations', CandidateJobScreenRelationsViewSet)
router.register(r'candidate_interviews', CandidateInterviewsViewSet)
router.register(r'remarks', RemarksViewSet)




urlpatterns = [
    path('', include(router.urls)),
]