# python 3.9
import yahoo_fin.stock_info as si

'''
get_financials() 함수 내에 티커를 입력한 후 yearly=True, quarterly=False 인자를 입력하면 연도별 재무제표 데이터가 다운로드 된다. 만일 분기별 재무제표 데이터를 원할 경우 yearly=False, quarterly=True를 입력하면 된다.
'''
data_y = si.get_financials('7203.T', yearly=True, quarterly=False)
print(data_y)
'''
제 위에서 받은 티커 리스트에 for loop 구문을 적용하면 모든 종목의 주가 및 재무제표를 다운로드 받을 수 있다. 단, 티커 리스트에 있는 종목 중 야후 파이낸스에 데이터가 없는 종목도 있으며 이는 trycatch() 구문을 사용해 처리하면 된다.
'''
