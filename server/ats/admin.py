# This file is used to register the models in the Django admin panel.
from django.contrib import admin
from django.contrib.auth import get_user_model
from authemail.admin import EmailUserAdmin
from .models import User, AccountType, Notification, NotificationType, Recruiter, Organization, Candidate, Salary, Job, JobScreen, JobScreenInterview, ProfileScore, CandidateApplication, CandidateJobScreenRelation, CandidateInterview, Remark

# admin.site.register(User)
admin.site.register(AccountType)
admin.site.register(Notification)
admin.site.register(NotificationType)
admin.site.register(Recruiter)
admin.site.register(Organization)
admin.site.register(Candidate)
admin.site.register(Salary)
admin.site.register(Job)
admin.site.register(JobScreen)
admin.site.register(JobScreenInterview)
admin.site.register(ProfileScore)
admin.site.register(CandidateApplication)
admin.site.register(CandidateJobScreenRelation)
admin.site.register(CandidateInterview)
admin.site.register(Remark)



class MyUserAdmin(EmailUserAdmin):
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Personal Info', {'fields': ('first_name', 'last_name')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 
									   'is_superuser', 'is_verified', 
									   'groups', 'user_permissions')}),
		('Important dates', {'fields': ('last_login', 'date_joined')}),
		('Custom info', {'fields': ('date_of_birth',)}),
	)

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), MyUserAdmin)