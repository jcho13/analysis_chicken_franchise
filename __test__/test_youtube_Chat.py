from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

request = Request("https://www.youtube.com/watch?v=yGZjSZ8W0dE")
response = urlopen(request)
html = response.read()

print(html)

bs = BeautifulSoup(html, 'html.parser')

# 들여쓰기 하면서 이쁘게 출력
print(bs.prettify())

print("----------------------bs.findAll('div', attrs={'class':'tit3'}--------------------------")
divs = bs.findAll('div', attrs={'class':'simpleText'})
print(divs)

# findAll 여러개 찾을 때
# divs = bs.findAll('div', attrs={'class':'tit3'})
#print(divs)

# index를 가져오기 위해 enumerate() 써줌
#for index, div in enumerate(divs):
#    print(index+1, div.a.text, div.a['href'], sep=" : ")




