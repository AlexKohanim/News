#!/usr/bin/env python3
import json
import requests
import sys
import colors
import os.path


base_url = "https://newsapi.org/v2/"
api_key = ""
file_location = "/home/alex/Documents/News/.api_key" if os.path.exists("/home/alex/Documents/News/.api_key") else  ".api_key"
try:
    with open(file_location, 'r') as api_file:
        api_key = api_file.readline().strip()
except FileNotFoundError:
    print("API key file not found, let's make it together")
    api_key = input("Please paste your key here: ")
    with open(file_location, "w") as newApiFile:
        newApiFile.write("apiKey="+api_key + "\n")
    print("API File created successfully at:", file_location)
        
arguments = len(sys.argv)
sort_type = "top-headlines" if arguments < 2 or sys.argv[1] == "top" else "everything"
source = 'hacker-news' if arguments < 3 else sys.argv[2]


composed_url = base_url + sort_type +"?sources=" + source + "&" + api_key  


response = requests.get(composed_url)
json_data = json.loads(response.text)

for article in json_data['articles']:
    try:
        pDate = article['publishedAt']
        content = article['content']
        url = article['url']
        print(colors.CRED + pDate, "\n" + colors.CGREEN2 + content, "\nRead More at:", colors.CBLUE2 +  url, end="\n\n")
    except TypeError as err:
        pass
