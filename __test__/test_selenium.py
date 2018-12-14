import time

from selenium import webdriver

# 경로 \, / 둘다 가능 (이유는 모르는데 \6이 경로로 안됨), d: 안써주는게 나음
wd = webdriver.Chrome('/JinHyukCho94/6_BigData/chromedriver_win32/chromedriver.exe')
wd.get('http://www.google.com')

# 구글 브라우저 로딩하는데 시간이 걸리니 5초 기다려
time.sleep(5)

# 화면에 있는 내용만 줌
html = wd.page_source
print(html)

# 브라우저 죽이기
wd.quit()