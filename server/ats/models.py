from django.db import models

# Create your models here.
class Users(models.Model):
    "The users that are part of the ATS."
    user_id = models.AutoField(primary_key=True)
    account_type_id = models.ForeignKey("AccountTypes", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    profile_picture = models.CharField(max_length=256, null = False)
    timezone = models.CharField(max_length=256, null = False)


class AccountTypes(models.Model):
    "The types of accounts that can be created."
    account_type_id = models.AutoField(primary_key=True, null=False)
    account_type = models.CharField(max_length=256, null = False)


class Notifications(models.Model):
    "The notifications that are sent to the users."
    notif_id = models.AutoField(primary_key=True)
    notif_type_id = models.IntegerField(null = False)
    creation_date = models.DateTimeField(null = False)
    creation_time = models.TimeField(null = False)
    additional_info = models.TextField(null = False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

class NotificationTypes(models.Model):
    "The types of notifications that can be sent to users."
    notif_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, null = False)
    description = models.TextField(null = False)
    template = models.TextField(null = False)
    is_email_notif = models.BooleanField(null = False)
    account_type_id = models.ForeignKey(AccountTypes, on_delete=models.CASCADE)


class Organizations(models.Model):
    "The organizations that are using the ATS."
    org_id = models.CharField(max_length=16, primary_key=True)
    org_name = models.CharField(max_length=64)
    admin_id = models.ForeignKey("Recruiters", on_delete=models.CASCADE)

class Recruiters(models.Model):
    "Recruiters that are part of the organization."
    recruiter_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey(Organizations, on_delete=models.CASCADE)
    user_id = models.ForeignKey("Users", on_delete=models.CASCADE)



class Candidates(models.Model):
    "Candidates that are applying for jobs."
    candidate_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    email = models.CharField(max_length=64, null = False)
    country = models.CharField(max_length=64, null = False)
    phone = models.CharField(max_length=64)
    country = models.CharField(max_length=64, null = False)
    linkedin_url = models.CharField(max_length=256, null = False)


class Salaries(models.Model):
    "The salary range for a job."
    salary_id = models.AutoField(primary_key=True)
    min_salary = models.IntegerField(null = False)
    max_salary = models.IntegerField(null = False)


class Jobs(models.Model):
    "The jobs that are posted by the recruiters."
    job_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey(Organizations, on_delete=models.CASCADE, null = False)
    creater_id = models.ForeignKey(Recruiters, on_delete=models.CASCADE, null = False)
    job_title = models.CharField(max_length=64, null = False)
    overview = models.CharField(max_length = 1024)
    responsibilities = models.CharField(max_length = 1024)
    qualifications = models.CharField(max_length = 1024)
    work_site = models.CharField(max_length=64, null = False)
    work_type = models.CharField(max_length=64, null = False)
    is_open = models.BooleanField(null = False)
    posted_on = models.DateTimeField(null = False)
    salary = models.ForeignKey(Salaries, on_delete=models.CASCADE, null = False)

class JobScreens(models.Model):
    "The screens that are part of the job application process."
    job_screen_id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey(Jobs, on_delete=models.CASCADE, null = False)
    screen_number = models.IntegerField(null = False)
    last_screen = models.BooleanField(null = False)


class JobScreenInterviews(models.Model):
    "The interviews that are part of the job application process."
    job_screen_interview_id = models.AutoField(primary_key=True)
    job_screen_id = models.ForeignKey(JobScreens, on_delete=models.CASCADE, null = False)
    creater_id = models.ForeignKey(Recruiters, on_delete=models.CASCADE, null = False)
    are_candidates_notified = models.BooleanField(null = False)
    are_all_interviews_done = models.BooleanField(null = False)
    last_interveiw_date = models.DateTimeField(null = False)


class ProfileScore(models.Model):
    "The score of the candidate's profile."
    profile_score_id = models.AutoField(primary_key=True)
    resume_score = models.IntegerField(null = False)
    relevance_score = models.IntegerField(null = False)

class CandidateApplications(models.Model):
    "The applications that the candidates have submitted."
    application_id = models.AutoField(primary_key=True)
    candidate_id = models.ForeignKey(Candidates, on_delete=models.CASCADE, null = False)
    job_id = models.ForeignKey(Jobs, on_delete=models.CASCADE, null = False)
    profile_score_id = models.ForeignKey(ProfileScore, on_delete=models.CASCADE, null = False)
    resume_file = models.CharField(max_length=256, null = False)


class CandidateJobScreenRelations(models.Model):
    "The relation between the candidate, the job screen, and the result of the screen."
    id = models.AutoField(primary_key=True)
    application_id = models.ForeignKey(CandidateApplications, on_delete=models.CASCADE, null = False)
    job_screen_id = models.ForeignKey(JobScreens, on_delete=models.CASCADE, null = False)
    is_screen_passed = models.BooleanField(null = False)

class CandidateInterviews(models.Model):
    "The interviews that the candidates have with the recruiters."
    canditate_interview_id = models.AutoField(primary_key=True)
    candidate_application_id = models.ForeignKey(CandidateApplications, on_delete=models.CASCADE, null = False)
    job_screen_interview_id = models.ForeignKey(JobScreenInterviews, on_delete=models.CASCADE, null = False)
    interview_date = models.DateTimeField(null = False)
    interview_time = models.TimeField(null = False)
    candidate_application_id = models.ForeignKey(CandidateApplications, on_delete=models.CASCADE, null = False)


class Remarks(models.Model):
    "The remarks that the recruiters have about the candidates."
    remark_id = models.AutoField(primary_key=True)
    candidate_job_screen_relation_id = models.ForeignKey(CandidateJobScreenRelations, 
                                                         on_delete=models.CASCADE, null = False)
    recruiter_id = models.ForeignKey(Recruiters, on_delete=models.CASCADE, null = False)