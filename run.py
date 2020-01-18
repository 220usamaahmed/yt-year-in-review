import config
from src import my_html_parser
from src import download_video_details
from src import comparison_over_time
from src import most_popular_channels
from src import category_frequencies
from src import top_channels_in_category
from src import total_over_time


def main():
	# my_html_parser.save_to_csv(config.HISTORY_HTML_FILE, config.HISTORY_CSV_FILE)	
	# download_video_details.download_video_details(config.API_KEY, config.HISTORY_CSV_FILE, config.DETAILS_JSON_DIR)
	# comparison_over_time.make_comparison(config.HISTORY_HTML_FILE, ["Liverpool"])
	# most_popular_channels.most_popular_channels(config.HISTORY_HTML_FILE)
	# category_frequencies.category_frequencies(config.DETAILS_JSON_DIR)
	# top_channels_in_category.top_channels_in_category(config.DETAILS_JSON_DIR, 24)
	# total_over_time.total_over_time(config.HISTORY_HTML_FILE, ["Linear Algebra", "Calculus"])


if __name__ == '__main__':
	main()