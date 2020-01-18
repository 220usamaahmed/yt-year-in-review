# YouTube Year In Review
Analytics performed on YouTube history data taken from Google Takeout.

## How to Use
The package provides several functions to calculate statistics based on the History Data.
In order to utilize these functions follow the following steps:
1. Download Youtube History Data from https://myaccount.google.com/ > Data & Personalization > Download your Data > YouTube. Make sure to download the data in HTML format.
2. Unzip the downloaded file and place the watch-history.html file in the dataset folder.
3. Open *run.py* and uncomment Step 1. Run this file. This will convert the HTML file into a CSV file
4. Register a YouTube Data API Key and paste it in the client_secret.txt file.
5. Open *run.py* and comment out Step 1. Then uncomment Step 2. Run this file. It will download additional details from YouTube for each video.
6. Comment Step 2.
7. Uncomment any of the examples to generate the graphs for that statistic

## Examples
1. __comparison_over_time__: A plot of videos watched over time.
```python	
# The second parameter is a list of search terms to compare
comparison_over_time.make_comparison(config.HISTORY_HTML_FILE, ["Coldplay", "Imagine Dragons"])
```

2. __most_popular_channels__: A bar chart of the channel with most videos viewed.
```python	
most_popular_channels.most_popular_channels(config.HISTORY_HTML_FILE)
```

3. __category_frequencies__: A bar chart of different categories watched.
```python
category_frequencies.category_frequencies(config.DETAILS_JSON_DIR)
```

4. __top_channels_in_category__: A bar chart of the top channels which have published a video of a certain category.
```python
# The second parameter is the category id. Pick this from the table provided below.
top_channels_in_category.top_channels_in_category(config.DETAILS_JSON_DIR, 24)
```
| ID | Category             |
|----|----------------------|
| 2  | Autos & Vehicles 	|
| 1  | Film & Animation 	|
| 10 | Music 				|
| 15 | Pets & Animals 		|
| 17 | Sports 				|
| 18 | Short Movies 		|
| 19 | Travel & Events 		|
| 20 | Gaming 				|
| 21 | Videoblogging 		|
| 22 | People & Blogs 		|
| 23 | Comedy 				|
| 24 | Entertainment 		|
| 25 | News & Politics 		|
| 26 | Howto & Style 		|
| 27 | Education 			|
| 28 | Science & Technology |
| 29 | Nonprofits & Activism|
| 30 | Movies 				|
| 31 | Anime/Animation 		|
| 32 | Action/Adventure 	|
| 33 | Classics 			|
| 34 | Comedy 				|
| 35 | Documentary 			|
| 36 | Drama 				|
| 37 | Family 				|
| 38 | Foreign 				|
| 39 | Horror 				|
| 40 | Sci-Fi/Fantasy 		|
| 41 | Thriller 			|
| 42 | Shorts 				|
| 43 | Shows 				|
| 44 | Trailer 				|

5. __total_over_time__: A bar chart to compare the total number of videos watched which contain a particular key term.

```python
total_over_time.total_over_time(config.HISTORY_HTML_FILE, ["Linear Algebra", "Calculus"])
```