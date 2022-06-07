# python 3.9
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import math
import pandas as pd
from tqdm import tqdm
import time

'''
1. 필요한 패키지들을 불러온다.
2. webdriver.Chrome()을 통해 크롬 페이지를 연다.
3. 일본의 국가코드에 해당하는 35를 입력한고, f string을 통해 url을 생성한다.
4. driver.get()을 통해 해당 주소를 연다.
5. 페이지가 열리기까지 시간이 걸리므로 바로 내용을 크롤링 할 수 없다. 먼저 WebDriverWait() 함수를 통해 10초간 기다리며, until(EC.visibility_of_element_located())을 통해 element가 존재할 때 까지, 즉 페이지가 열릴때 까지 기다린다. 여기서는 종목수에 해당하는 부분을 입력하였다. 만일 10초 이전에 해당 데이터가 존재할 경우 wait를 멈춘다.
6. 총 몇페이지까지 존재하는지 계산한다.
7. 티커가 들어갈 빈 리스트(all_data_df)를 만든다
'''

# basic code
driver = webdriver.Chrome("chromeDriver/chromedriver.exe")
nationcode = '35'
url = f'https://investing.com/stock-screener/?sp=country::{nationcode}|sector::a|industry::a|equityType::a%3Ceq_market_cap;1'
driver.get(url)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'js-total-results')))
end_num = driver.find_element(By.CLASS_NAME, value='js-total-results').text
end_num = math.ceil(int(end_num) / 50)
all_data_df = []
'''
crawling
'''

'''
1. list(range(1, end_num+1))을 통해 1부터 끝페이지까지 리스트를 생성하며, 진행상황을 보기 위해 tqdm() 함수를 이용한다.
2. f-string 내에 국가코드와 페이지 정보를 입력해 url을 만든다.
3. driver.get()을 통해 페이지를 연다.
4. 이번에는 XPATH가 '//*[@id="resultsTable"]/tbody'인, 즉 테이블 정보가 열릴때 까지 기다린다.
5. BeautifulSoup()을 통해 html 정보를 가져온다.
6. 티커와 섹터 정보를 각각 가져와 저장한다.
7. 데이터프레임 형태로 합친다.
8. 위에서 만들어둔 all_data_df에 append()를 통해 붙인다.
9. 2초간의 슬립을 준다.
'''
# for i in tqdm(list(range(1, end_num + 1))):
for i in tqdm(list(range(1, 2))):
    url = f'https://investing.com/stock-screener/?sp=country::{nationcode}|sector::a|industry::a|equityType::a%3Ceq_market_cap;{i}'
    driver.get(url)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="resultsTable"]/tbody')))

    html = BeautifulSoup(driver.page_source, 'lxml')

    # stock name
    data_name = html.find_all(class_='symbol left bold elp')
    data_name = [i.get_text() for i in data_name]

    # ticker
    data_ticker = html.select('td[data-column-name = "viewData.symbol"]')
    data_ticker = [i.get_text() for i in data_ticker]

    # sum data(stock name, ticker)
    data_df = pd.DataFrame(
        {'name': data_name,
         'ticker': data_ticker,
         }
    )
    all_data_df.append(data_df)
    time.sleep(2)
'''
1. pd.concat()을 통해 리스트 내의 데이터프레임을 하나로 묶는다.
2. js-search-input inputDropDown 클래스는 국가를 선택하는 드랍박스 부분을 의미하며, value는 국가명을 의미한다.
3. 데이터프레임의 country 열에 해당 정보를 입력한다.
4. driver.quit()을 통해 크롬창을 종료한다.
'''
all_data_df_bind = pd.concat(all_data_df, axis=0)

data_country = html.find(class_='js-search-input inputDropDown')['value']
all_data_df_bind['country'] = data_country

print(all_data_df_bind)

driver.quit()
