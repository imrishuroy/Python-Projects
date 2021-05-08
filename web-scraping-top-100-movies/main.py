import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

all_movies = soup.findAll(name="h3", class_="jsx-4245974604")
movies_title = [movie.getText() for movie in all_movies]
movies = movies_title[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movies}\n")







#
# response = requests.get("https://news.ycombinator.com/news")
# # print(response.text)
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, "html.parser")
#
# articles = soup.findAll(name="a", class_="storylink")
# article_texts = []
# articles_links = []
#
# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.get("href")
#     articles_links.append(link)
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.findAll(name="span", class_="score")]
#
# print(article_texts)
# print(articles_links)
# print(article_upvotes)
#
# # points = []
# #
# # for item in article_upvotes:
# #     points.append(int(item[0:1]))
# #
# # print(points)
#
# max_point_index = article_upvotes.index(max(article_upvotes))
# print(max_point_index)
#
# print(article_texts[3])
# print(articles_links[3])
#
#
#
#
#
#
#
#
