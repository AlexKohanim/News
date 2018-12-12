#!/usr/bin/env python3
import json
import requests
import sys
import os.path

base_url = "https://newsapi.org/v2/"
api_key = ""
file_location = "/home/alex/Documents/News/.api_key" if os.path.exists("/home/alex/Documents/News/.api_key") else  ".api_key"
with open(file_location, 'r') as api_file:
    api_key = api_file.readline().strip()
arguments = len(sys.argv)

sort_type = "top-headlines" if arguments < 2 or sys.argv[1] == "top" else "everything"
source = 'hacker-news' if arguments < 3 else sys.argv[2]


composed_url = base_url + sort_type +"?sources=" + source + "&" + api_key  


response = requests.get(composed_url)#"https://newsapi.org/v2/top-headlines?sources=hacker-news&apiKey=740efc132a4849269a5843c422143500")
json_data = json.loads(response.text)

for article in json_data['articles']:
    try:
        pDate = article['publishedAt']
        content = article['content']
        url = article['url'] 
        print(pDate, "\n" + content, "\nRead More at:", url, end="\n\n")
    except TypeError as err:
        pass
