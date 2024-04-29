# from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

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

from .models import CandidateApplication
from .serializer import CandidateApplicationSerializer


# import settings
from django.conf import settings
#import status
from rest_framework import status

#import multipart parser
from rest_framework.parsers import MultiPartParser
from .resume_matcher.parse_jd import JobDescriptionProcessor
from pypdf import PdfReader

class CandidateApplicationDetailView(APIView):
    def get(self, request, pk, format=None):
        application = get_object_or_404(CandidateApplication, pk=pk)
        serializer = CandidateApplicationSerializer(application)
        return Response(serializer.data)

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
    parser_classes = (MultiPartParser,)
    def create(self, request, *args, **kwargs):
        job_description_file = request.FILES.get('job_description_file')
        instance = self.get_serializer(data=request.data)
        instance.is_valid(raise_exception=True)
        self.perform_create(instance)
        # Handle the case when a file is uploaded
        model_instance = instance.save()
        instance_id = model_instance.job_id
        if job_description_file:
            # Convert the job description file to JSON
            instance_id = str(instance_id)
            output = []
            try: 
                pdf_reader = PdfReader(job_description_file)
                count = len(pdf_reader.pages)
                for i in range(count):
                    page = pdf_reader.pages[i]
                    output.append(page.extract_text())
            except Exception as e:
                print(f"Error reading file {str(e)}")
            pdf_content = str(" ".join(output))
            job_processor = JobDescriptionProcessor(pdf_content, instance_id, True)
            job_processor.process()
            
        else:
            # Handle the case when no file is uploaded
            text = instance.data['job_description']
            job_processor = JobDescriptionProcessor(text, instance_id, True)
            job_processor.process()
        
        from ats.resume_matcher.score import read_json
        import os
        job_json = read_json(os.path.join(settings.MEDIA_ROOT, 'job_descriptions', str(instance_id) + '.json'))
        tags = job_json['extracted_keywords']
        job_instance = Job.objects.get(job_id=instance_id)
        job_instance.tags = tags
        job_instance.save()
        return Response(instance.data, status=status.HTTP_201_CREATED)

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

# a one of view to create candidate application and their account
# the data will have all the information including resume 
# and the job id to which the candidate is applying
from ats.resume_matcher.score import score
class CreateCandidateAPIView(APIView):
    def post(self, request, format=None):
        # Deserialize the request data
        candidate_serializer = CandidateSerializer(data=request.data)
        # check if candidate data is valid and save
        candidate_serializer.is_valid(raise_exception=True)
        candidate_instance = candidate_serializer.save()
        # associate the candidate with the application
        application_data = request.data
        application_data['candidate_id'] = candidate_instance.pk
        application_serializer = CandidateApplicationSerializer(data=application_data)
        application_serializer.is_valid(raise_exception=True)
        application_instance = application_serializer.save()
        resume_file = request.FILES.get('resume_file')
         
        from ats.resume_matcher.parse_resume import ResumeProcessor
        resume_processor = ResumeProcessor(str(candidate_instance.pk))
        resume_processor.process()

        resume_score = score(str(candidate_instance.pk), str(application_instance.job_id.job_id))
        profile_score_instance = ProfileScore.objects.create(resume_score=resume_score, candidate_application_id=application_instance)
        
        candidate_data = candidate_serializer.data
        application_data = application_serializer.data
        profile_score_data = ProfileScoreSerializer(profile_score_instance).data

        response_data = {
            'candidate': candidate_data,
            'application': application_data,
            'profile_score': profile_score_data
        }
        return Response(response_data, status=status.HTTP_201_CREATED)