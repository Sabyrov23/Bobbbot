import requests
from bs4 import BeautifulSoup

URL = "https://kaktus.media/"

HEADERS = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}

def get_html(url, params= ""):
    req= requests.get(url,headers=HEADERS, params=params)
    return req

html= get_html(URL)

def get_data(html):
    soup=BeautifulSoup(html,"html.parser")
    items= soup.find_all("dif",class_="ArticleItem")
    news=[]
    for item in items:
        news.append({
            "title":item.find("a",class_="ArticleItem--name").getText().replace("\n",""),
            "time":item.find("div",class_="ArticleItem--name").getText().replace("\n",""),
            "link":item.find("a",class_="ArticleItem--name").get("href")
        })

        return news
    def parser():
        html = get_html(URL)
        if html.status_code == 200:
            ans = get_data(html.text)
            return ans
        raise Exception("Error in parser")

    def parser():
        html = get_html(URL)
        if html.status_code == 200:
            answers = []
            for page in range (1, 2):
                html = get_html(f'{URL}page/{page}/')
                current_page= get_data(html.text)
                answers.extend(current_page)
                return answers
            else:
                raise Exception("Error in parser")

