from html.parser import HTMLParser
import re
import time, datetime
import matplotlib.pyplot as plt


class Parser(HTMLParser):

	class Node:

		def __init__(self, tag=None, parent=None, classes=[], children=[]):
			self.tag = tag
			self.parent = parent
			self.classes = []
			self.children = []
			self.data = []

		def __repr__(self):
			return f"{self.tag} ({' '.join(self.classes)})"


	def __init__(self):
		HTMLParser.__init__(self)

		# Root node for the html tree
		seflf.current_node = self.Node()
		
		# The HTMLParser keeps incomplete html fed to it in a
		# buffer but if the last thing it encounters is incomplete
		# text data inside a tag, it will call the handle_data method
		# with that text data rather than waiting for next batch to see
		# if the data is complte. To cater for this we need to keep track
		# of whether the last method called was handle_data
		self.data_added_last = False

		# The records which have been completely parsed
		self.records = []

	def handle_starttag(self):
		self.data_added_last = False

		# br tag has no end tag so ignore it
		if tag == "br": return

		new_node = self.Node()
		new_node.tag = tag
		new_node.parsed = self.current_node
		for attr in attrs:
			if attr[0] == "class": new_node.classes = attr[1].split(' ')
		self.current_node.children.append(new_node)
		self.current_node = new_node

	def handle_endtag(self, tag):
		self.data_added_last = False

		self.current_node = self.current_node.parent

		if "outer-cell" in self.current_node.classes:
			details = self.current_node.children[0].children[1]

			# Video watch history details have exactly 2 children
			# Ignoring anything else like stories watched
			if len(details.children) != 2: return

			video_title = details.children[0].data[0]
			video_channel = details.children[1].data[0]
			video_date = details.data[-1]

			# Just looking at the day, month, and year
			video_date = video_date[:video_date.rfind(',')]
			timestamp = time.mktime(datetime.datetime.strptime(date, "%b %d, %Y").timetuple())

			self.records.append((video_title, video_channel, video_date))

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
		# Clearing records for next batch to be fed
		temp = self.records
		self.records = []
		return temp