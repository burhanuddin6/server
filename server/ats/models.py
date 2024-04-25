from django.db import models

from authemail.models import EmailUserManager, EmailAbstractUser

# class MyUser(EmailAbstractUser):
    

# Create your models here.
class User(EmailAbstractUser):
    "The user that are part of the ATS."
    objects = EmailUserManager()
    # user_id = models.AutoField(primary_key=True)
    # account_type_id = models.ForeignKey("AccountType", on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=256)
    # last_name = models.CharField(max_length=256)
    # profile_picture = models.ImageField(upload_to='profile_pictures/', null = True)
    # timezone = models.CharField(
    #     max_length=64,
    #     choices=[(tz, tz) for tz in pytz.all_timezones]
    # )


class AccountType(models.Model):
    '''
    The types of accounts that can be created.
    The primary account types are member, member_admin, member_super_admin
    These account types are preexisting in the database
    '''
    account_type_id = models.AutoField(primary_key=True, null=False)
    account_type = models.CharField(max_length=256, null = False)
    
    def __str__(self):
        return self.account_type
    
class Notification(models.Model):
    "The notification that are sent to the user."
    notif_id = models.AutoField(primary_key=True)
    notif_type_id = models.ForeignKey("NotificationType", on_delete=models.CASCADE)
    creation_date = models.DateTimeField(null = False)
    creation_time = models.TimeField(null = False)
    additional_info = models.TextField(null = False)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE, default=None)

class NotificationType(models.Model):
    "The types of notification that can be sent to user."
    notif_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, null = False)
    description = models.TextField(null = False)
    template = models.TextField(null = False)
    is_email_notif = models.BooleanField(null = False)

    def __str__(self) -> str:
        return self.name

class Organization(models.Model):
    "The organization that are using the ATS."
    org_id = models.CharField(max_length=16, primary_key=True)
    org_name = models.CharField(max_length=64, unique=True, null = False)

class Recruiter(models.Model):
    "Recruiter that are part of the organization."
    recruiter_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE, to_field='org_name', unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)



class Salary(models.Model):
    "The salary range for a job."
    salary_id = models.AutoField(primary_key=True)
    min_salary = models.IntegerField(null = False)
    max_salary = models.IntegerField(null = False)


class Job(models.Model):
    "The jobs that are posted by the recruiter."
    job_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE, null = False, to_field='org_name')
    creater_id = models.ForeignKey(Recruiter, on_delete=models.CASCADE, null = False, to_field='recruiter_id')
    job_title = models.CharField(max_length=64, null = False)
    overview = models.CharField(max_length = 1024)
    responsibilities = models.CharField(max_length = 1024)
    qualifications = models.CharField(max_length = 1024)
    work_site = models.CharField(max_length=64, null = False)
    work_type = models.CharField(max_length=64, null = False)
    is_open = models.BooleanField(null = False)
    posted_on = models.DateTimeField(null = False)
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE, null = False)

class Candidate(models.Model):
    "Candidate that are applying for jobs."
    candidate_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=64, null = True)
    last_name = models.CharField(max_length=64, null = True)
    email = models.CharField(max_length=64, null = False)
    country = models.CharField(max_length=64, null = False)
    phone = models.CharField(max_length=64)
    linkedin_url = models.CharField(max_length=256, null = False)



class JobScreen(models.Model):
    "The screens that are part of the job application process."
    job_screen_id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, null = False)
    screen_number = models.IntegerField(null = False)
    last_screen = models.BooleanField(null = False)


class JobScreenInterview(models.Model):
    "The interviews that are part of the job application process."
    job_screen_interview_id = models.AutoField(primary_key=True)
    job_screen_id = models.ForeignKey(JobScreen, on_delete=models.CASCADE, null = False)
    creater_id = models.ForeignKey(Recruiter, on_delete=models.CASCADE, null = False)
    are_candidate_notified = models.BooleanField(null = False)
    are_all_interviews_done = models.BooleanField(null = False)
    last_interveiw_date = models.DateTimeField(null = False)


class ProfileScore(models.Model):
    "The score of the candidate's profile."
    profile_score_id = models.AutoField(primary_key=True)
    resume_score = models.IntegerField(null = False)
    relevance_score = models.IntegerField(null = False)

class CandidateApplication(models.Model):
    "The applications that the candidate have submitted."
    application_id = models.AutoField(primary_key=True)
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE, null = False)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, null = False)
    profile_score_id = models.ForeignKey(ProfileScore, on_delete=models.CASCADE, null = False)
    resume_file = models.CharField(max_length=256, null = False)



class CandidateJobScreenRelation(models.Model):
    "The relation between the candidate, the job screen, and the result of the screen."
    id = models.AutoField(primary_key=True)
    application_id = models.ForeignKey(CandidateApplication, on_delete=models.CASCADE, null = False)
    job_screen_id = models.ForeignKey(JobScreen, on_delete=models.CASCADE, null = False)
    is_screen_passed = models.BooleanField(null = False)

class CandidateInterview(models.Model):
    "The interviews that the candidate have with the recruiter."
    canditate_interview_id = models.AutoField(primary_key=True)
    candidate_application_id = models.ForeignKey(CandidateApplication, on_delete=models.CASCADE, null = False)
    job_screen_interview_id = models.ForeignKey(JobScreenInterview, on_delete=models.CASCADE, null = False)
    interview_date = models.DateTimeField(null = False)
    interview_time = models.TimeField(null = False)
    candidate_application_id = models.ForeignKey(CandidateApplication, on_delete=models.CASCADE, null = False)


class Remark(models.Model):
    "The remark that the recruiter have about the candidate."
    remark_id = models.AutoField(primary_key=True)
    candidate_job_screen_relation_id = models.ForeignKey(CandidateJobScreenRelation, 
                                                         on_delete=models.CASCADE, null = False)
    recruiter_id = models.ForeignKey(Recruiter, on_delete=models.CASCADE, null = False)