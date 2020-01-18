from src.my_html_parser import MyHTMLParser
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


def total_over_time(history_html_file, keywords):
	parser = MyHTMLParser(history_html_file)
	records = parser.get_records()

	totals = get_frequency(records, keywords)

	plt.barh(range(len(totals)), list(totals.values()), color=(255/255, 52/255, 100/255))
	plt.yticks(range(len(totals)), list(totals.keys()), color=(0.32, 0.32, 0.32))
	plt.gca().invert_yaxis()
	plt.suptitle("Top in Music", fontsize=36, color=(0.16, 0.16, 0.16))
	plt.xlabel("Nonconsecutive Views of One Video", fontsize=16, color=(0.24, 0.24, 0.24))
	plt.show()