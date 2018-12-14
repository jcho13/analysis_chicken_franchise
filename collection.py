from datetime import datetime

import pandas as pd
import ssl
import time
from itertools import count
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from selenium import webdriver

RESULT_DIRECTORY = "__result__"

"""
# 교촌치킨 sido1 : 1~17, sido2 : 1~25 (이중 for문)
# http://www.kyochon.com/shop/domestic.asp?sido1=[1~17]&sido2=[1~25]&txtsearch=
def crawling_kyochon():
    results = []

    for sido1 in range(1, 18):
        for sido2 in count(start=1):
            try:
                url = "http://www.kyochon.com/shop/domestic.asp?sido1=%d&sido2=%d&txtsearch=" % (sido1, sido2)
                req = Request(url)
                resp = urlopen(req)

                receive = resp.read()
                html = receive.decode('utf-8')

                # 로그 남기기
                print('%s : success for request [%s]' % (datetime.now(), url))

                bs = BeautifulSoup(html, 'html.parser')
                tag_ul = bs.find("ul", attrs={'class' : 'list'}) # <ul class="list">

                for tag_span in tag_ul.findAll('span', attrs={'class' : 'store_item'}):
                    name = tag_span.find('strong').text # 속성으로 접근
                    address = tag_span.find('em').get_text().strip().split("\r")[0] # 메소드로 접근 (getter method) / \r : 개행

                    si_do_gu = address.split()[:2]
                    results.append((name, address) + tuple(si_do_gu))

            except Exception as e:
                print('%s : %s' % (datetime.now(), e))
                break



    # store
    #print("len(results) : ", len(results))
    #print(results)

#                         address.split()[:2]한걸 'si_do', 'gun_gu' 각각에 넣음
    table = pd.DataFrame(results, columns=['name', 'address', 'si_do', 'gun_gu'])
    table.to_csv(
        '{0}/kyochon_table.csv'.format(RESULT_DIRECTORY),
        encoding='utf-8',
        mode='w',
        index=True)  # mode : w 쓰기 모드
"""


"""
def crawling_nene():
    results = []
    prepage_firstShopname = ''
    for page in count(start=1):
    #for page in range(47, 50):
        url = "https://nenechicken.com/17_new/sub_shop01.asp?page=%d" % page
        request = Request(url)
        response = urlopen(request, context=ssl._create_unverified_context())
        receive = response.read()

        # UnicodeDecodeError -> replace
        html = receive.decode('utf-8', 'replace')  # utf-8 안넣어도 큰 상관은 없음

        #print(html)

        bs = BeautifulSoup(html, 'html.parser')
        tags_table = bs.findAll('table', attrs={'class' : 'shopTable'})
        print("len(tags_table): ", len(tags_table)) # 24개

        is_end = False

        for index, tag_table in enumerate(tags_table):
            name = tag_table.find('div', attrs={'class' : 'shopName'}).text
            address = tag_table.find('div', attrs={'class' : 'shopAdd'}).text
            si_do_gu = address.split()[:2]


            # 끝 검출 (마지막 페이지보다 더 가면 마지막 페이지를 보여줌)
            if index == 0:
                if prepage_firstShopname == name: # 이전 페이지 이름 == 현재 이름 => 끝
                    is_end = True
                    break
                else:
                    prepage_firstShopname = name

            results.append((name, address) + tuple(si_do_gu))

        if is_end is True: # 끝이면 for문을 빠져나가게 해야해
            break

        # 로그 출력
        print('%s : success for request [%s]' % (datetime.now(), url))


        # store
        #print("len(results) : ", len(results))
        #print(results)

    #                         address.split()[:2]한걸 'si_do', 'gun_gu' 각각에 넣음
    table = pd.DataFrame(results, columns=['name', 'address', 'si_do', 'gun_gu'])
    table.to_csv(
        '{0}/nene_table.csv'.format(RESULT_DIRECTORY),
        encoding='utf-8',
        mode='w',
        index=True)  # mode : w 쓰기 모드
"""
"""
def crawling_pelicana():
   results = []
   for page in count(start=1): # 1부터 무한대로 쭉 감 (step써도됨)
   #for page in range(113, 120):
        url = "https://pelicana.co.kr/store/stroe_search.html?gu=&si=&page=%d" % page
        request = Request(url)
        response = urlopen(request, context=ssl._create_unverified_context())

        receive = response.read()

        # UnicodeDecodeError -> replace
        html = receive.decode('utf-8', 'replace')  # utf-8 안넣어도 큰 상관은 없음

        # print(html)

        bs = BeautifulSoup(html, 'html.parser')
        # print(bs.prettify())

        tag_table = bs.find('table', attrs={'class' : 'table mt20'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        # 끝 검출
        if len(tags_tr) == 0:
            break


        # 로그 출력
        print('%s : success for request [%s]' % (datetime.now(), url))


        # <tr> 출력 (내용 뽑아내기)
        for tag_tr in tags_tr:
           strings = list(tag_tr.strings)
           #print(strings)
           name = strings[1]
           address = strings[3]
           si_do_gu = address.split()[:2] # 시도구에서 앞에 2개만 뽑아오기
           #print(name, address, si_do_gu)

           results.append((name, address) + tuple(si_do_gu))


   # store(적재)
   #print(len(result)) # 가게 개수
   #print(result)

   #                         address.split()[:2]한걸 'si_do', 'gun_gu' 각각에 넣음
   table = pd.DataFrame(results, columns=['name', 'address', 'si_do', 'gun_gu'])
   table.to_csv(
       '{0}/pelicana_table.csv'.format(RESULT_DIRECTORY),
       encoding='utf-8',
       mode='w',
       index=True) # mode : w 쓰기 모드
"""

def crawling_goobne():
    url = "https://www.goobne.co.kr/store/search_store.jsp"

    # 첫 페이지 로딩
    wd = webdriver.Chrome('/JinHyukCho94/6_BigData/chromedriver_win32/chromedriver.exe')
    wd.get(url)
    time.sleep(1)

    results = []

    for page in count(start=1):
    #for page in range(102, 104):

        # 자바 스크립트 실행
        script = 'store.getList(%d)' % page
        wd.execute_script(script)

        # 로그
        print('%s : success for script execute [%s]' % (datetime.now(), script))
        time.sleep(1)

        # 실행 결과 HTML (rendering된 HTML) 가져오기
        html = wd.page_source
        #print(html)

        # bs4을 사용해서 파싱
        bs = BeautifulSoup(html, 'html.parser')
        tag_tbody = bs.find('tbody', attrs={'id' : 'store_list'})
        tags_tr = tag_tbody.findAll('tr')

        # 마지막 검출
        # attribute부를때 이렇게 부를 수 있음
        # 103에서 끝이 검출되어야 함
        if tags_tr[0].get('class') is None:
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[6]
            si_do_gun = address.split()[:2]

            results.append((name, address) + tuple(si_do_gun))

    print(results)

   # store(적재)
   #                         address.split()[:2]한걸 'si_do', 'gun_gu' 각각에 넣음
    table = pd.DataFrame(results, columns=['name', 'address', 'si_do', 'gun_gu'])
    table.to_csv(
       '{0}/goobne_table.csv'.format(RESULT_DIRECTORY),
       encoding='utf-8',
       mode='w',
       index=True) # mode : w 쓰기 모드


if __name__ == '__main__':
    # pelicana
    #crawling_pelicana()

    # nene
    #crawling_nene()

    # kyochon
    #crawling_kyochon()

    # goobne - 크롤링의 하이라이트 (Ajax)
    crawling_goobne()

    # bhc


