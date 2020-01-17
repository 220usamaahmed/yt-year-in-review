import os
import json
import matplotlib.pyplot as plt


JSON_DUMP_DIR = "D:/yt-year-in-review/dataset/details/"


channels = {}


def find_channels(filename, category_filters=[]):
	# Forgot to actually save files as json while downloading so have to specify encoding
	with open(os.path.join(JSON_DUMP_DIR, filename), 'r', encoding="utf-8") as json_file:
		records = json.load(json_file)["items"]
		
		for record in records:
			category_id = int(record["snippet"]["categoryId"]) 
			channel_title = record["snippet"]["channelTitle"]

			if channel_title == "Favorite Videos": continue

			if category_id in category_filters:
				if channel_title in channels:
					channels[channel_title] += 1
				else:
					channels[channel_title] = 1


def main():

	global channels

	for filename in os.listdir(JSON_DUMP_DIR):
		print(f"Processing file {filename}")

		find_channels(filename, [1])

	channels = {k: v for k, v in sorted(channels.items(), key=lambda item: item[1], reverse=True)[:25]}
	
	for channel in channels:
		print(f"{channel:48}:{channels[channel]}")

	plt.barh(range(len(channels)), list(channels.values()), color=(255/255, 52/255, 100/255))
	plt.yticks(range(len(channels)), list(channels.keys()), color=(0.32, 0.32, 0.32))
	plt.gca().invert_yaxis()
	# plt.suptitle("Top in Music", fontsize=36, color=(0.16, 0.16, 0.16), x=0.206)
	# plt.title("Apr 5, 2018 to Jan 15, 2020\n", fontsize=18, color=(0.24, 0.24, 0.24), loc="left")
	# plt.xlabel("Nonconsecutive Views of One Video", fontsize=16, color=(0.24, 0.24, 0.24))
	plt.show()


if __name__ == '__main__':
	main()
