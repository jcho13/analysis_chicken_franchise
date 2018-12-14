from bs4 import BeautifulSoup

html = '<td class="title gray blue">' \
            '<div class="tit3" id="1234id">' \
                '<a href="/movie/bi/mi/basic.nhn?code=156464" title="보헤미안 랩소디">보헤미안 랩소디</a>' \
            '</div>' \
       '</td>'

#==================================================

print("< 1. 태그 조회 : 태그 이름으로 태그 조회 >")

def ex1():
    bs = BeautifulSoup(html, 'html.parser')
    print(bs)

    tag = bs.td
    print(tag)
    print(tag.div)

    tag = bs.div
    print(tag)

    tag = bs.a
    print(tag)


print("< 2. Attribute 값 >")

def ex2():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.td

    # 클래스 속성의 값 가져옴
    print(tag['class'])

    tag = bs.div
    print(tag['class'], tag['id'])

    tag = bs.a
    print(tag['href'], tag['title'])

    # 가지고 있는 모든 걸 출력
    print(tag.attrs)

    # 오류 (없는건 못가져옴)
    # print(tag[''])


print("< 3. 태그 조회 : 태그 속성으로 태그 조회 >")
def ex3():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.find('td', attrs={'class': 'title'})
    print(tag)

    tag = bs.find(attrs={'title':'보헤미안 랩소디'})
    print(tag)



if __name__ == '__main__':
    # ex1()
    # ex2()
    ex3()
