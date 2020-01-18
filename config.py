import os


PROJECT_PATH = os.getcwd()

DATASET_PATH = os.path.join(PROJECT_PATH, "dataset")

HISTORY_HTML_FILE = os.path.join(DATASET_PATH, "watch-history.html")

HISTORY_CSV_FILE = os.path.join(DATASET_PATH, "watch-history.csv")

DETAILS_JSON_DIR = os.path.join(DATASET_PATH, "details")


with open("client_secret.txt", 'r') as client_secret_file:
	API_KEY = client_secret_file.read()


if not os.path.isdir(DATASET_PATH):
	os.mkdir(DATASET_PATH)

if not os.path.isdir(DETAILS_JSON_DIR):
	os.mkdir(DETAILS_JSON_DIR)