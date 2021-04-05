import requests
from bs4 import BeautifulSoup as bs
import csv
file = open("moive.csv", mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["title", "star", "img_src",
                "director", "actors", "published_date"])
url = 'https://movie.naver.com/movie/running/current.nhn'
movie_html = requests.get(url)
movie_soup = bs(movie_html.text, "html.parser")
movie_big_box = movie_soup.find('ul', {"class": "lst_detail_t1"})
movie_list = movie_big_box.find_all('li')
final_reuslt = []
for info in movie_list:
    title = info.find('dl', {"class": "lst_dsc"}).find(
        'dt', {"class": "tit"}).find('a').text
    star = info.find('dl', {"class": "lst_dsc"}).find('dd', {"class": "star"}).find(
        'dl', {"class": "info_star"}).find('dd').find('div', {"class": "star_t1"}).find('span', {"class": "num"}).text
    img_src = info.find("div", {"class": "thumb"}).find('a').find('img')['src']
    director = info.find("dl", {"class": "lst_dsc"}).find(
        'dl', {"class": "info_txt1"}).find_all('dd')[1].find('a').text
    actors = info.find('dl', {"class": "lst_dsc"}).find('dl', {
        "class": "info_txt1"}).find_all('dd')[-1].find('span', {"class": "link_txt"}).text.replace('\r', '').replace('\t', '').replace('\n', '')
    published_date = info.find('dl', {"class": "lst_dsc"}).find(
        'dl', {"class": "info_txt1"}).find_all('dd')[0].text.replace('\r', '').replace('\t', '').replace('\n', '')
    movie_info = {
        "title": title,
        "star": star,
        "img_src": img_src,
        "director": director,
        "actors": actors,
        "published_date": published_date}
    final_reuslt.append(movie_info)

for result in final_reuslt:
    row = []
    row.append(result['title'])
    row.append(result['star'])
    row.append(result['img_src'])
    row.append(result['director'])
    row.append(result['actors'])
    row.append(result['published_date'])
    writer.writerow(row)


file.close()
