from html.parser import HTMLParser
import re
import time, datetime


class MyHTMLParser(HTMLParser):

	class Node:

		def __init__(self, tag=None, parent=None, classes=[], children=[]):
			self.tag = tag
			self.parent = parent
			self.attributes = {}
			self.children = []
			self.data = []

		def __repr__(self):
			return self.tag


	def __init__(self, filepath):
		HTMLParser.__init__(self)

		self.filepath = filepath

		# Root node for the html tree
		self.current_node = self.Node()
		
		# The HTMLParser keeps incomplete html fed to it in a
		# buffer but if the last thing it encounters is incomplete
		# text data inside a tag, it will call the handle_data method
		# with that text data rather than waiting for next batch to see
		# if the data is complte. To cater for this we need to keep track
		# of whether the last method called was handle_data
		self.data_added_last = False

		# The records which have been completely parsed
		self.records = []

	def handle_starttag(self, tag, attrs):
		self.data_added_last = False

		# br tag has no end tag so ignore it
		if tag == "br": return

		new_node = self.Node()
		new_node.tag = tag
		new_node.parent = self.current_node
		for attr in attrs:
			new_node.attributes[attr[0]] = attr[1]
		self.current_node.children.append(new_node)
		self.current_node = new_node

	def handle_endtag(self, tag):
		self.data_added_last = False

		self.current_node = self.current_node.parent

		if "class" in self.current_node.attributes and "outer-cell" in self.current_node.attributes["class"]:
			details = self.current_node.children[0].children[1]

			# Video watch history details have exactly 2 children
			# Ignoring anything else like stories watched
			if len(details.children) != 2: return

			video_id = details.children[0].attributes["href"].split("=")[1]
			video_title = details.children[0].data[0]
			video_channel = details.children[1].data[0]
			video_date = details.data[-1]

			# Just looking at the day, month, and year
			video_date = video_date[:video_date.rfind(',')]
			timestamp = time.mktime(datetime.datetime.strptime(video_date, "%b %d, %Y").timetuple())

			self.records.append((video_id, video_title, video_channel, timestamp))

	def handle_data(self, data):
		if self.data_added_last: self.current_node.data[-1] += data
		else: self.current_node.data.append(data)

		self.data_added_last = True

	def print_tree(self):

		def print_node(node, indentation=0):
			if node.children:
				for child in node.children:
					print('\t' * indentation, child)
					print_node(child, indentation + 1)

		print_node(self.current_node)

	def get_records(self):

		BUFFER_SIZE = 4 * 2**20 # 4MB

		with open(self.filepath, 'r', encoding="utf-8") as file:
			while True:
				data = file.read(BUFFER_SIZE)
				if not data: break

				self.feed(data)

				for record in self.records:
					yield record

				self.records = []


def save_to_csv(html_filepath, csv_filepath):
	"""
	Parse HTML file taken from Google Takeout and save its
	content in a csv file

	Args:
		html_filepath: filepath of the raw data taken from Google Takeout
		csv_filepath: filepath of the csv file in which to save the data
	"""

	parser = MyHTMLParser(html_filepath)
	
	csv_file = open(csv_filepath, 'w', encoding="utf-8")

	for video_id, video_title, video_channel, video_date in parser.get_records():
		print(video_id)
		csv_file.write(f"{video_id},{video_title},{video_channel},{video_date}\n")

	csv_file.close()
