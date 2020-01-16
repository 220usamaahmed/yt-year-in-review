from my_html_parser import MyHTMLParser
import matplotlib.pyplot as plt


plt.style.use('ggplot')


def get_channel_view_counts(records, ordered=True, n=None):
	
	view_counter = {}

	for _, channel, _ in records:
		if channel in view_counter:
			view_counter[channel] += 1
		else:
			view_counter[channel] = 1

	if ordered: return {k: v for k, v in sorted(view_counter.items(), key=lambda item: item[1], reverse=True)[:n]}
	else: return view_counter


def main():
	parser = MyHTMLParser("D:/yt-year-in-review/dataset/watch-history-small.html")
	records = parser.get_records()

	channel_view_counts = get_channel_view_counts(records, n=16)
	# for channel in channel_view_counts:
	# 	print(channel, channel_view_counts[channel])

	plt.barh(range(len(channel_view_counts)), list(channel_view_counts.values()))
	plt.yticks(range(len(channel_view_counts)), list(channel_view_counts.keys()))
	plt.gca().invert_yaxis()
	plt.show()


if __name__ == '__main__':
	main()