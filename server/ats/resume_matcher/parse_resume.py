import json
import pathlib
import os

from ats.resume_matcher.scripts.parsers import ParseResume
from ats.resume_matcher.scripts.ReadPdf import read_single_pdf

# import settings
from django.conf import settings
# get media path from settings
MEDIA_ROOT = settings.MEDIA_ROOT
INPUT_DIR = os.path.join(MEDIA_ROOT, "resumes")
OUTPUT_DIR = os.path.join(MEDIA_ROOT, "resumes_parsed")


def find_file_by_name(directory, filename):
    # Iterate over files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the filename matches the known name
            if file.startswith(filename):
                # Return the full path of the file
                return os.path.join(root, file)
    # If file not found, return None
    return None

class ResumeProcessor:
    def __init__(self, candidate_id):
        # find the input file in input dir the resume will have candidate_id as name but ext is unknown
        self.input_file = find_file_by_name(INPUT_DIR, candidate_id)
        self.output_file_name = str(candidate_id)
        if not self.input_file:
            raise FileNotFoundError(f"File with candidate id {candidate_id} not found in {INPUT_DIR}")
        self.input_file_name = os.path.join(self.input_file)

    def process(self) -> bool:
        try:
            resume_dict = self._read_resumes()
            self._write_json_file(resume_dict)
            return True
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False

    def _read_resumes(self) -> dict:
        data = read_single_pdf(self.input_file_name)
        output = ParseResume(data).get_JSON()
        return output

    def _write_json_file(self, resume_dictionary: dict):
        file_name = str( 
            self.output_file_name
            + ".json"
        )
        save_directory_name = pathlib.Path(OUTPUT_DIR) / file_name
        # remove any existing file
        if os.path.exists(save_directory_name):
            os.remove(save_directory_name)
        json_object = json.dumps(resume_dictionary, sort_keys=True, indent=14)
        with open(save_directory_name, "w+") as outfile:
            outfile.write(json_object)
