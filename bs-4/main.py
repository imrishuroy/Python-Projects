from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
# print(response.text)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.findAll(name="a", class_="storylink")
article_texts = []
articles_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    articles_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.findAll(name="span", class_="score")]

print(article_texts)
print(articles_links)
print(article_upvotes)

# points = []
#
# for item in article_upvotes:
#     points.append(int(item[0:1]))
#
# print(points)

max_point_index = article_upvotes.index(max(article_upvotes))
print(max_point_index)

print(article_texts[3])
print(articles_links[3])


















# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)
# print(soup.name)
# print(soup.prettify())
#
#
# all_anchor_tags = soup.findAll(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     #print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# heading = soup.select(".heading")
# print(heading)