from my_html_parser import MyHTMLParser
import matplotlib.pyplot as plt


plt.style.use("ggplot")


def get_channel_view_counts(records, ordered=True, n=None):
	
	view_counter = {}

	for _, channel, _ in records:
		if len(channel) > 24: channel = channel[:24] + "..."
		if channel == "Favorite Videos": continue
		if channel in view_counter:
			view_counter[channel] += 1
		else:
			view_counter[channel] = 1

	if ordered: return {k: v for k, v in sorted(view_counter.items(), key=lambda item: item[1], reverse=True)[:n]}
	else: return view_counter


def main():
	parser = MyHTMLParser("D:/yt-year-in-review/dataset/watch-history.html")
	# parser = MyHTMLParser("D:/yt-year-in-review/dataset/watch-history-small.html")
	# parser = MyHTMLParser("D:/yt-year-in-review/dataset/watch-history-bilal.html")
	records = parser.get_records()

	channel_view_counts = get_channel_view_counts(records, n=25)
	for channel in channel_view_counts:
		print(channel, channel_view_counts[channel])

	plt.barh(range(len(channel_view_counts)), list(channel_view_counts.values()), color=(255/255, 52/255, 100/255))
	plt.yticks(range(len(channel_view_counts)), list(channel_view_counts.keys()), color=(0.32, 0.32, 0.32))
	plt.gca().invert_yaxis()
	plt.suptitle("Top 25 YouTube Channels", fontsize=36, color=(0.16, 0.16, 0.16), x=0.295)
	plt.title("Apr 5, 2018 to Jan 15, 2020\n", fontsize=18, color=(0.24, 0.24, 0.24), loc="left")
	plt.xlabel("Nonconsecutive Views of One Video", fontsize=16, color=(0.24, 0.24, 0.24))
	plt.show()

if __name__ == '__main__':
	main()