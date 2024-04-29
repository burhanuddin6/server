# parse job description given in text or pdf

import json
import os.path
import pathlib

# from scripts.parsers import ParseJobDesc
from ats.resume_matcher.scripts.parsers import ParseJobDesc
from ats.resume_matcher.scripts.ReadPdf import read_single_pdf

# import settings
from django.conf import settings
# get media path from settings
MEDIA_ROOT = settings.MEDIA_ROOT
INPUT_DIR = os.path.join(MEDIA_ROOT, "temp", "job_descriptions")
OUTPUT_DIR = os.path.join(MEDIA_ROOT, "job_descriptions")

class JobDescriptionProcessor:
    def __init__(self, input_file : str, output_file_name : str, file_is_text: bool, input_dir=INPUT_DIR, output_dir=OUTPUT_DIR):
        self.input_file = input_file
        self.output_dir = output_dir
        self.output_file_name = str(output_file_name)
        self.is_file_text = file_is_text
        if self.is_file_text:
            self.input_file_path = None
        else:
           self.input_file_path = os.path.join(input_dir + self.input_file)

    def process(self) -> bool:
        try:
            resume_dict = self._read_job_desc()
            self._write_json_file(resume_dict)
            return True
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False

    def _read_job_desc(self) -> dict:
        if self.is_file_text:
            data = self.input_file
        else:
            data = read_single_pdf(self.input_file_path)
        output = ParseJobDesc(data).get_JSON()
        return output

    def _write_json_file(self, resume_dictionary: dict):
        file_name = str(
            # "JobDescription-"
            # + self.input_file
            # + resume_dictionary["unique_id"]
            self.output_file_name
            + ".json"
        )
        save_directory_name = pathlib.Path(self.output_dir) / file_name
        # remove any existing file
        if os.path.exists(save_directory_name):
            os.remove(save_directory_name)
        json_object = json.dumps(resume_dictionary, sort_keys=True, indent=14)
        with open(save_directory_name, "w+") as outfile:
            outfile.write(json_object)
