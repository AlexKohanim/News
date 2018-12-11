# News
Get Headline News Using this API: https://newsapi.org/

To use this script:

1. Change the file Path:
	
	I made a symbolic link for the python file, so I had to make an absolute
	
	File path for the .api_key file
	
	For me it is ~/Documents/News/.api_key

	If you don't plan on adding a symbolic link you can just make the file path
	
	.api_key


2. Preliminary step, get your own API key from: https://newsapi.org/register:

	then create a file ".api_key" at the same level as the "get_news.py" file

	make sure the first line looks like this

	apiKey=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

	the rest of the lines don't really matter, but I wouldn't add more "

3. use default config ("hacker-news, top")

	./get_news.py

4. run with new content instead of top (put anything other than top all is prefered)

	./get_news.py all

5. run with custom news source:

	./get_news.py top techcrunch


Link to all sources available: https://newsapi.org/sources

