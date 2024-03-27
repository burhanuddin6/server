# This file is used to register the models in the Django admin panel.
from django.contrib import admin
from .models import Users, AccountTypes, Notifications, NotificationTypes, Recruiters, Organizations, Candidates, Salaries, Jobs, JobScreens, JobScreenInterviews, ProfileScore, CandidateApplications, CandidateJobScreenRelations, CandidateInterviews, Remarks

admin.site.register(Users)
admin.site.register(AccountTypes)
admin.site.register(Notifications)
admin.site.register(NotificationTypes)
admin.site.register(Recruiters)
admin.site.register(Organizations)
admin.site.register(Candidates)
admin.site.register(Salaries)
admin.site.register(Jobs)
admin.site.register(JobScreens)
admin.site.register(JobScreenInterviews)
admin.site.register(ProfileScore)
admin.site.register(CandidateApplications)
admin.site.register(CandidateJobScreenRelations)
admin.site.register(CandidateInterviews)
admin.site.register(Remarks)