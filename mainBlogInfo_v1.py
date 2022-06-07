# python 3.9
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import math
import lxml # pip install lxml

'''
1. Link: investing.com > [Markets - Stocks- Stock Screener]
2. Link(USA): https://www.investing.com/stock-screener/?sp=country::5|sector::a|industry::a|equityType::a|exchange::a%3Ceq_market_cap;1
3. Change Country Link(JPN): https://www.investing.com/stock-screener/?sp=country::35%7Csector::a%7Cindustry::a%7CequityType::a%3Ceq_market_cap;1
4. Your Chrome Browser Version Check. (2022-06-07 v102.0.5005.63)
5. Link: https://chromedriver.chromium.org/downloads
6. Download ChromeDriver (2022-06-07 v102.0.5005.61)
'''

driver = webdriver.Chrome("chromeDriver/chromedriver.exe")
url = 'https://www.investing.com/stock-screener/?sp=country::35|sector::a|industry::a|equityType::a|exchange::20%3Ceq_market_cap;1'
driver.get(url)

html = BeautifulSoup(driver.page_source, 'lxml')  # pip install lxml

'''
7. check HTML get value 'data_name'('Title') at 'symbol left bold elp'
'''
data_name = html.find_all(class_='symbol left bold elp')
print([i.get_text() for i in data_name])
# ## print Result
# ['Toyota Motor', 'Sony', 'Nippon Telegraph & Telephone Corp', 'Keyence', 'KDDI Corp.', 'Tokyo Electron', 'Mitsubishi UFJ Financial', 'Softbank Group Corp.', 'Shin-Etsu Chemical', 'Recruit Holdings', 'Fast Retailing', 'SoftBank Corp', 'Nintendo', 'Mitsubishi Corp.', 'Hitachi', 'Daiichi Sankyo', 'Oriental Land Co Ltd', 'Daikin Industries', 'Denso Corp.', 'Chugai Pharmaceutical', 'Honda Motor', 'Takeda Pharmaceutical', 'Itochu Corp.', 'Sumitomo Mitsui Financial', 'Murata Mfg Co', 'Mitsui', 'Tokio Marine Holdings, Inc.', 'Nidec Corp', 'Hoya Cor', 'Seven & i Holdings', 'SMC Corp', 'Japan Tobacco', 'Fanuc Corp.', 'Mizuho Financial', 'Fujitsu', 'Japan Post Bank', 'Astellas Pharma Inc.', 'Bridgestone Corp.', 'Olympus Corp.', 'Japan Post Holdings', 'Canon', 'Z Holdings', 'Central Japan Railway Co.', 'Komatsu', 'Terumo Corp.', 'Mitsubishi Electric', 'Renesas Electronics Corp', 'Kubota Corp.', 'Orix T', 'Fujifilm Holdings Corp.']


'''
8. check HTML get value 'viewData.symbol' at 'data-column-name'
'''
data_ticker = html.select('td[data-column-name = "viewData.symbol"]')
print([i.get_text() for i in data_ticker])
# ## print Result
# ['7203', '6758', '9432', '6861', '9433', '8035', '8306', '9984', '4063', '6098', '9983', '9434', '7974', '8058', '6501', '4568', '4661', '6367', '6902', '4519', '7267', '4502', '8001', '8316', '6981', '8031', '8766', '6594', '7741', '3382', '6273', '2914', '6954', '8411', '6702', '7182', '4503', '5108', '7733', '6178', '7751', '4689', '9022', '6301', '4543', '6503', '6723', '6326', '8591', '4901']

'''
9. get total page, total item value results get.
'''
end_num = driver.find_element(By.CLASS_NAME, value='js-total-results').text
print(math.ceil(int(end_num) / 50))

# next mainBlogInfo_v2.py
