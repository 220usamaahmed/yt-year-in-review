from my_html_parser import MyHTMLParser
import matplotlib.pyplot as plt


plt.style.use("ggplot")


def contains(first, second):
	for part in first.lower().split(' '):
		if not part in second.lower():
			return False
	return True


def get_frequencies_over_time(records, search_terms, per_n_days=1):

	frequencies = {search_term: [0] for search_term in search_terms}

	first_record = next(records)
	current_timestamps = {search_term: first_record[2] for search_term in search_terms} 


	for search_term in frequencies:
		if contains(search_term, first_record[0]) or contains(search_term, first_record[1]):
			frequencies[search_term] = [1]

	for title, channel, timestamp in records:
		for search_term in frequencies:
			if timestamp == current_timestamps[search_term]:
				if contains(search_term, title) or contains(search_term, channel):
					# print(f"{channel}: {title}")
					frequencies[search_term][-1] += 1
			else:
				days_passed = int((current_timestamps[search_term] - timestamp) / 86400)
				frequencies[search_term] += [0] * days_passed
				current_timestamps[search_term] = timestamp

	if per_n_days != 1:
		per_n_days_frequencies = {}
		for search_term in frequencies:
			per_n_days_frequencies[search_term] = [sum(frequencies[search_term][i:i+per_n_days]) for i in range(0, len(frequencies[search_term]), per_n_days)]
		return per_n_days_frequencies

	return frequencies


def main():
	parser = MyHTMLParser("D:/yt-year-in-review/dataset/watch-history.html")
	# parser = MyHTMLParser("D:/yt-year-in-review/dataset/watch-history-small.html")
	# parser = MyHTMLParser("D:/yt-year-in-review/dataset/watch-history-bilal.html")
	records = parser.get_records()

	frequencies = get_frequencies_over_time(records, ["Corridor"], 7)
	for channel in frequencies:
		print(channel, frequencies[channel])
		plt.plot(frequencies[channel], label=channel)

	plt.suptitle("Frequency Comparisons", fontsize=36, color=(0.16, 0.16, 0.16), x=0.206)
	plt.title("Apr 5, 2018 to Jan 15, 2020\n", fontsize=18, color=(0.24, 0.24, 0.24), loc="left")
	plt.xlabel("Nonconsecutive Views of One Video per Week", fontsize=16, color=(0.24, 0.24, 0.24))
	plt.legend()
	plt.gca().invert_xaxis()
	plt.show()


if __name__ == '__main__':
	main()