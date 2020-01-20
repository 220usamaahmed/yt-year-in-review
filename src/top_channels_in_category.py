import os
import json
import matplotlib.pyplot as plt
import config


"""
2:  Autos & Vehicles
1:  Film & Animation
10: Music
15: Pets & Animals
17: Sports
18: Short Movies
19: Travel & Events
20: Gaming
21: Videoblogging
22: People & Blogs
23: Comedy
24: Entertainment
25: News & Politics
26: Howto & Style
27: Education
28: Science & Technology
29: Nonprofits & Activism
30: Movies
31: Anime/Animation
32: Action/Adventure
33: Classics
34: Comedy
35: Documentary
36: Drama
37: Family
38: Foreign
39: Horror
40: Sci-Fi/Fantasy
41: Thriller
42: Shorts
43: Shows
44: Trailer

"""
channels = {}


def find_channels(filepath, category_filter):
	# Forgot to actually save files as json while downloading so have to specify encoding
	with open(filepath, 'r', encoding="utf-8") as json_file:
		records = json.load(json_file)["items"]
		
		for record in records:
			category_id = int(record["snippet"]["categoryId"]) 
			channel_title = record["snippet"]["channelTitle"]

			if channel_title == "Favorite Videos": continue

			if category_id == category_filter:
				if channel_title in channels:
					channels[channel_title] += 1
				else:
					channels[channel_title] = 1


def top_channels_in_category(category_id):

	global channels

	for filename in os.listdir(config.DETAILS_JSON_DIR):
		print(f"Processing file {filename}")

		find_channels(os.path.join(config.DETAILS_JSON_DIR, filename), category_id)

	channels = {k: v for k, v in sorted(channels.items(), key=lambda item: item[1], reverse=True)[:25]}
	
	for channel in channels:
		print(f"{channel:48}:{channels[channel]}")

	plt.barh(range(len(channels)), list(channels.values()), color=(255/255, 52/255, 100/255))
	plt.yticks(range(len(channels)), list(channels.keys()), color=(0.32, 0.32, 0.32))
	plt.gca().invert_yaxis()
	plt.suptitle("Top In a Particular Category", fontsize=36, color=(0.16, 0.16, 0.16), x=0.206)
	plt.xlabel("Nonconsecutive Views of One Video", fontsize=16, color=(0.24, 0.24, 0.24))
	plt.show()


if __name__ == '__main__':
	main()
