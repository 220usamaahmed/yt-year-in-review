import json
import urllib.request
from os import path


def download_details_for_batch(api_key, records, save_as):
	video_ids = ",".join([record[0] for record in records])
	url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_ids}&key={api_key}"

	json_url = urllib.request.urlopen(url)
	data = json.loads(json_url.read())

	with open(save_as, 'w') as json_file:
		json.dump(data, json_file)


def download_video_details(api_key, csv_filepath, details_json_dir):
	with open(csv_filepath, 'r', encoding="utf-8") as csv_file:
		records = csv_file.readlines()

		records = [x.strip().split(',') for x in records]

	for b, i in enumerate(range(0, len(records), 50)):
		print(f"Downloading batch{b+1:003}")
		download_details_for_batch(api_key, records[i:i+50], path.join(details_json_dir, f"batch_{b+1:03}.json"))