import json
import urllib.request
from os import path


API_KEY = "AIzaSyCUdDLxadafzIGyw6xkpvwICLMd4Xt5SHw"
CSV_FILE = "D:/yt-year-in-review/dataset/watch-history.csv"
JSON_DUMP_DIR = "D:/yt-year-in-review/dataset/details/"


def download_details(records, save_as):
	video_ids = ",".join([record[0] for record in records])
	url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_ids}&key={API_KEY}"

	json_url = urllib.request.urlopen(url)
	data = json.loads(json_url.read())

	with open(path.join(JSON_DUMP_DIR, save_as), 'w') as json_file:
		json.dump(data, json_file)


def main():
	with open(CSV_FILE, 'r', encoding="utf-8") as csv_file:
		records = csv_file.readlines()

		records = [x.strip().split(',') for x in records] 

	for b, i in enumerate(range(93*50, len(records), 50)):
		print(f"Downloading batch{b+94:003}")
		download_details(records[i:i+50], f"batch_{b+94:03}.json")
		

if __name__ == '__main__':
 	# main() 