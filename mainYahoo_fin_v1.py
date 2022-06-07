# python 3.9
import yahoo_fin.stock_info as si  # pip install yahoo_fin

'''
파이썬에서 야후 파이낸스의 주가 및 재무제표는 yahoo_fin 패키지를 이용하면 된다.
'''
price = si.get_data('7203.T') # get_data 함수 내에 티커를 입력하면 주가가 다운로드 된다.
print(price.head())
