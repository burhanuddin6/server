import json
import os
from ats.resume_matcher.scripts.similarity.get_score import get_score
from ats.resume_matcher.scripts.utils import get_filenames_from_dir
from ats.resume_matcher.parse_resume import find_file_by_name

from django.conf import settings

MEDIA_ROOT = settings.MEDIA_ROOT
JSON_RESUME_DIR = os.path.join(MEDIA_ROOT, "resumes_parsed")
JSON_JD_DIR = os.path.join(MEDIA_ROOT, "job_descriptions")

def read_json(filename):
    with open(filename) as f:
        return json.load(f)

# def main():
#     resume_folder = "Data/Processed/Resumes"
#     job_description_folder = "Data/Processed/JobDescription"
#     output_file = "scores_output.txt"

#     resume_files = get_filenames_from_dir(resume_folder)
#     job_description_files = get_filenames_from_dir(job_description_folder)

#     # Assuming each resume is to be compared with each job description
#     with open(output_file, "w") as out_f:
#         for resume_filename in resume_files:
#             resume_data = read_json(os.path.join(resume_folder, resume_filename))
#             resume_keywords = " ".join(resume_data["extracted_keywords"])

#             for jd_filename in job_description_files:
#                 jd_data = read_json(os.path.join(job_description_folder, jd_filename))
#                 jd_keywords = " ".join(jd_data["extracted_keywords"])

#                 # Calculate the similarity score
#                 result = get_score(resume_keywords, jd_keywords)
#                 similarity_score = round(result[0].score * 100, 2)

#                 # Write the results
#                 out_f.write(f"Resume: {resume_filename}, Job Description: {jd_filename}, Score: {similarity_score}\n")

# if __name__ == "__main__":
#     main()

def score(candidate_id, job_description_id):
    resume_file = find_file_by_name(JSON_RESUME_DIR, candidate_id)
    jd_file = find_file_by_name(JSON_JD_DIR, job_description_id)

    if not resume_file:
        raise FileNotFoundError(f"File with candidate id {candidate_id} not found in {JSON_RESUME_DIR}")

    if not jd_file:
        raise FileNotFoundError(f"File with job description id {job_description_id} not found in {JSON_JD_DIR}")
    
    resume_data = read_json(resume_file)
    resume_keywords = " ".join(resume_data["extracted_keywords"])

    jd_data = read_json(jd_file)
    jd_keywords = " ".join(jd_data["extracted_keywords"])

    result = get_score(resume_keywords, jd_keywords)
    similarity_score = round(result[0].score * 100, 2)

    return similarity_score
