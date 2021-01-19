import requests # http method를 사용하기 위해서 import
import json
from bs4 import BeautifulSoup # from ~ import ~ 조사

# 블로그 전체 게시글 제목 가져오기
# 아이디를 넣으면, 그 아이디의 블로그 전체 게시글 제목들을 가져오는 함수 구현


def get_blog_posts(id):
    
    url = data['tistory-left'] + id + data['tistory-right']
    req = requests.get(url) # 응답상태코드 반환

    soup = BeautifulSoup(req.content, 'html.parser') 
    # req.content에 html 코드가 담겨있음
    # html.parser을 가지고 할 것이다

    res = soup.select('#mArticle > div > a.link_post > strong') # res는 array

    for i in res:
        print(i.contents[0]) # or i.text
        # contents의 0번째 원소를 불러옴


if __name__ == "__main__":

    with open('./data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    get_blog_posts(data['member'][0])
