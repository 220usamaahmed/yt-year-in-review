import datetime
import matplotlib.pyplot as plt
from src.my_html_parser import MyHTMLParser


plt.style.use("ggplot")


def contains(first, second):
	for part in first.lower().split(' '):
		if not part in second.lower():
			return False
	return True


def get_frequencies_over_time(records, search_terms, per_n_days=1):

	frequencies = {search_term: [0] for search_term in search_terms}

	first_record = next(records)
	first_timestamp = first_record[3]
	current_timestamps = {search_term: first_timestamp for search_term in search_terms}

	for search_term in frequencies:
		if contains(search_term, first_record[0]) or contains(search_term, first_record[1]):
			frequencies[search_term] = [1]

	for _, title, channel, timestamp in records:
		for search_term in frequencies:
			if timestamp == current_timestamps[search_term]:
				if contains(search_term, title) or contains(search_term, channel):
					# print(f"{channel}: {title}")
					frequencies[search_term][-1] += 1
			else:
				days_passed = int((current_timestamps[search_term] - timestamp) / 86400)
				frequencies[search_term] += [0] * days_passed
				current_timestamps[search_term] = timestamp

	last_timestamp = first_timestamp - len(frequencies[search_terms[0]]) * 86400

	if per_n_days != 1:
		per_n_days_frequencies = {}
		for search_term in frequencies:
			per_n_days_frequencies[search_term] = [sum(frequencies[search_term][i:i+per_n_days]) for i in range(0, len(frequencies[search_term]), per_n_days)]
		return first_timestamp, last_timestamp, per_n_days_frequencies

	return first_timestamp, last_timestamp, frequencies


def make_comparison(history_html_file, search_terms, over_n_days=7):
	
	if not search_terms: return

	parser = MyHTMLParser(history_html_file)
	records = parser.get_records()

	first_timestamp, last_timestamp, frequencies = get_frequencies_over_time(records, search_terms, over_n_days)

	for search_term in frequencies:
		print(search_term, frequencies[search_term])
		plt.plot(frequencies[search_term], label=search_term)

	x_ticks = [datetime.datetime.fromtimestamp(ts).strftime("%b %d, %Y") for ts in range(int(last_timestamp), int(first_timestamp) + 1, int((first_timestamp - last_timestamp) / 8))]
	num_buckets = len(frequencies[search_terms[0]])

	print(x_ticks)

	plt.suptitle("Frequency Comparisons", fontsize=36, color=(0.16, 0.16, 0.16))
	plt.xlabel("Nonconsecutive Views of One Video per Week", fontsize=16, color=(0.24, 0.24, 0.24))
	plt.xticks(list(range(0, num_buckets, int(num_buckets / 8))), list(reversed(x_ticks)))
	plt.legend()
	plt.gca().invert_xaxis()
	plt.show()