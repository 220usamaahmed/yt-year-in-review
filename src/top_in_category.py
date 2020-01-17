from my_html_parser import MyHTMLParser
import matplotlib.pyplot as plt


plt.style.use("ggplot")


def contains(first, second):
	for part in first.lower().split(' '):
		if not part in second.lower():
			return False
	return True 	


def get_frequency(records, search_terms, ordered=True):
	
	view_counter = {search_term: 0 for search_term in search_terms}

	for _, title, channel, _ in records:
		for search_term in view_counter:
			if contains(search_term, title) or contains(search_term, channel):
				view_counter[search_term] += 1

	if ordered: return {k: v for k, v in sorted(view_counter.items(), key=lambda item: item[1], reverse=True)}
	else: return view_counter


def main():
	# parser = MyHTMLParser("D:/yt-year-in-review/dataset/watch-history.html")
	parser = MyHTMLParser("D:/yt-year-in-review/dataset/watch-history-small.html")
	# parser = MyHTMLParser("D:/yt-year-in-review/dataset/watch-history-bilal.html")
	records = parser.get_records()

	# Top Music
	keywords = [
		"Linkin Park",
		"Coldplay",
		"Taylor Swift",
		"twenty one pilots",
		"Mike Shinoda",
		"Imagine Dragons",
		"One Republic",
		"Adele",
		"Tessa Violet ",
		"Sigrid",
		"Ariana Grande",
		"Lana Del Rey",
		"Chvrches",
		"Fort Minor",
		"Ed Sheeran",
		"Arctic Monkeys",
		"Lorde",
		"Kodaline",
		"The Weeknd",
		"Bastille",
		"Sia",
		"Chainsmokers",
		"Paramore",
		"Eminem",
		"Selena Gomez",
		"Radiohead",
		"ODESZA",
		"Billie Eilish",
		"Harry Styles",
		"Bruno Mars",
		"The Script",
		"Muse",
		"Kendrick Lamar",
		"Alan Walker",
		"Seafret",
		"Lana Del Rey",
		"Logic",
		"Fun." ]

	top_music = get_frequency(records, keywords)

	plt.barh(range(len(top_music)), list(top_music.values()), color=(255/255, 52/255, 100/255))
	plt.yticks(range(len(top_music)), list(top_music.keys()), color=(0.32, 0.32, 0.32))
	plt.gca().invert_yaxis()
	plt.suptitle("Top in Music", fontsize=36, color=(0.16, 0.16, 0.16), x=0.206)
	plt.title("Apr 5, 2018 to Jan 15, 2020\n", fontsize=18, color=(0.24, 0.24, 0.24), loc="left")
	plt.xlabel("Nonconsecutive Views of One Video", fontsize=16, color=(0.24, 0.24, 0.24))
	plt.show()

if __name__ == '__main__':
	main()