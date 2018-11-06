import json

LABS_FILENAME = "labs.json"

def load_lab_data():
	labs_file_string = open(LABS_FILENAME).read()
	lab_json = json.loads(labs_file_string)
	return lab_json