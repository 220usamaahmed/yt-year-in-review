import os
import json
import matplotlib.pyplot as plt


plt.style.use("ggplot")


JSON_DUMP_DIR = "D:/yt-year-in-review/dataset/details/"


categories = {
	2: "Autos & Vehicles",
	1: "Film & Animation",
	10: "Music",
	15: "Pets & Animals",
	17: "Sports",
	18: "Short Movies",
	19: "Travel & Events",
	20: "Gaming",
	21: "Videoblogging",
	22: "People & Blogs",
	23: "Comedy",
	24: "Entertainment",
	25: "News & Politics",
	26: "Howto & Style",
	27: "Education",
	28: "Science & Technology",
	29: "Nonprofits & Activism",
	30: "Movies",
	31: "Anime/Animation",
	32: "Action/Adventure",
	33: "Classics",
	34: "Comedy",
	35: "Documentary",
	36: "Drama",
	37: "Family",
	38: "Foreign",
	39: "Horror",
	40: "Sci-Fi/Fantasy",
	41: "Thriller",
	42: "Shorts",
	43: "Shows",
	44: "Trailers"
}
frequencies = {}


def count_frequency(filename):
	# Forgot to actually save files as json while downloading so have to specify encoding
	with open(os.path.join(JSON_DUMP_DIR, filename), 'r', encoding="utf-8") as json_file:
		records = json.load(json_file)["items"]
		
		for record in records:
			category_id = int(record["snippet"]["categoryId"]) 
			if category_id in frequencies:
				frequencies[category_id] += 1
			else:
				frequencies[category_id] = 1


def main():

	global frequencies

	for filename in os.listdir(JSON_DUMP_DIR):
		print(f"Processing file {filename}")

		count_frequency(filename)
		
	frequencies = {categories[k]: v for k, v in sorted(frequencies.items(), key=lambda item: item[1], reverse=True)}
	print(frequencies)

	plt.barh(range(len(frequencies)), list(frequencies.values()), color=(255/255, 52/255, 100/255))
	plt.yticks(range(len(frequencies)), list(frequencies.keys()), color=(0.32, 0.32, 0.32))
	plt.gca().invert_yaxis()
	plt.suptitle("Categories Ranked", fontsize=36, color=(0.16, 0.16, 0.16), x=0.248)
	plt.title("Apr 5, 2018 to Jan 15, 2020\n", fontsize=18, color=(0.24, 0.24, 0.24), loc="left")
	plt.xlabel("Nonconsecutive Views of One Video", fontsize=16, color=(0.24, 0.24, 0.24))
	plt.show()


if __name__ == '__main__':
	main()

