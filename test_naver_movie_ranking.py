from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

request = Request("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
response = urlopen(request)
html = response.read().decode('cp949')

print(html)

bs = BeautifulSoup(html, 'html.parser')

# 들여쓰기 하면서 이쁘게 출력
print(bs.prettify())

print("----------------------bs.findAll('div', attrs={'class':'tit3'}--------------------------")

# findAll 여러개 찾을 때
divs = bs.findAll('div', attrs={'class':'tit3'})
print(divs)

# index를 가져오기 위해 enumerate() 써줌
for index, div in enumerate(divs):
    print(index+1, div.a.text, div.a['href'], sep=" : ")




