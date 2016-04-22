import json, requests

#Importing data throught APIs
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
content = response.content

#Retrieving elements from an HTML Page

from bs4 import BeautifulSoup

# Initialize the parser, and pass in the content we grabbed earlier.
parser = BeautifulSoup(content, 'html.parser')

# Get the body tag from the document.
# Since we passed in the top level of the document to the parser, we need to pick a branch off of the root.
# With beautifulsoup, we can access branches by simply using tag types as 
body = parser.body

# Get the p tag from the body.
p = body.p

# Print the text of the p tag.
# Text is a property that gets the inside text of a tag.
print(p.text)

head = parser.head
title_text = head.title.text

#Using find_all method to find all occurences of a tag 

parser = BeautifulSoup(content, 'html.parser')

# Get a list of all occurences of the body tag in the element.
body = parser.find_all("body")

# Get the paragraph tag
p = body[0].find_all("p")

# Get the text
print(p[0].text)

head = parser.find_all("head")
title = head[0].find_all("title")
title_text = title[0].text

#Element IDs

# Get the page content and setup a new parser.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_ids.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Pass in the id attribute to only get elements with a certain id.
first_paragraph = parser.find_all("p", id="first")[0]
print(first_paragraph.text)

second_paragraph = parser.find_all("p", id="second")[0]
second_paragraph_text = second_paragraph.text

#Element Classes

# Get the website that contains classes.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Get the first inner paragraph.
# Find all the paragraph tags with the class inner-text.
# Then take the first element in that list.
first_inner_paragraph = parser.find_all("p", class_="inner-text")[0]
print(first_inner_paragraph.text)

second_inner_paragraph = parser.find_all("p", class_="inner-text")[1]
second_inner_paragraph_text = second_inner_paragraph.text

first_outer_paragraph = parser.find_all("p", class_="outer-text")[0]
first_outer_paragraph_text = first_outer_paragraph.text

#CSS Selectors

# Get the website that contains classes and ids
response = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Select all the elements with the first-item class
first_items = parser.select(".first-item")

# Print the text of the first paragraph (first element with the first-item class)
print(first_items[0].text)

outer_text = parser.select(".outer-text")
first_outer_text = outer_text[0].text

second_id = parser.select("#second")
second_text = second_id[0].text

#Working with Reddit API

params = {"t" : "day"}
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
response = requests.get("https://oauth.reddit.com/r/python/top",headers=headers,params = params)
python_top = response.json()

#Getting the most upvoted article

children = python_top['data']
python_top_articles = children['children']
#print(python_top_articles)
most_ups = 0
most_upvoted = 0
for row in python_top_articles:
    if row['data']['ups'] > most_ups:
        most_ups = row['data']['ups']
        most_upvoted = row['data']['id']
    else:
        pass
print(most_upvoted)

#Getting article comments

response = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u",headers=headers)
comments = response.json()

#Getting the most upvoted comment

comments_list = comments[1]['data']['children']
print(comments_list)
most_upvoted_comment = ""
maximum = 0 
for row in comments_list:
    if row['data']['ups'] > maximum:
        maximum = row['data']['ups']
        most_upvoted_comment = row['data']['id']
    else:
        pass


#Upvoting a comment

payload = {"dir" : 1, "id" : "d16y4ry"}
response = requests.post("https://oauth.reddit.com/api/vote",json = payload,headers=headers)
status = response.status_code


