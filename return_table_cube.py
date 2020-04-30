import pandas as pd
from sqlalchemy import create_engine
import numpy as np
from dateutil.relativedelta import  relativedelta

engine = create_engine('mysql://root:admin@123@localhost:3306/creditpulse')
conn = engine.connect()
index_price = pd.read_sql('cubed_index_price', engine)
price = index_price.copy()
returns = pd.DataFrame(columns=['return_appreciation','date','sn500','decimalpoint_500','old_date'])
returns.loc[0, 'return_appreciation'] = 'Since inception'
returns.loc[1, 'return_appreciation'] ='10 year'
returns.loc[2, 'return_appreciation'] = '5 year'
returns.loc[3, 'return_appreciation'] ='3 year'
returns.loc[4, 'return_appreciation'] ='1 year'
returns.loc[5, 'return_appreciation'] ='YTD'
returns.loc[6, 'return_appreciation'] ='Today'
returns['date'][0] = price['date'][0]
returns['date'][5] = '2018-12-31'
returns['date'][6] = price["date"].iloc[-1]
returns['old_date'] = price["date"].iloc[-1]
returns['date'][1] = returns['old_date'][0] - pd.DateOffset(years=10)
returns['date'][2] = returns['old_date'][0] - pd.DateOffset(years=5)
returns['date'][3] = returns['old_date'][0] - pd.DateOffset(years=3)
returns['date'][4] = returns['old_date'][0]- pd.DateOffset(years=1)
returns['date'] = pd.to_datetime(returns['date'])
returns=returns.drop(['old_date'],axis=1)
test_data = pd.merge(returns,index_price,on=['date'],how ='left')
test_data= test_data.drop(['sn500','decimalpoint_500','id'],axis=1)
test_data.rename(columns={'index_price':'sn500','credit_score_index_price':'decimalpoint_500'},inplace = True)
test_data['perc']= ((test_data['sn500'][6]-test_data['sn500'])/test_data['sn500'])*100
test_data['perc_DPA']= ((test_data['decimalpoint_500'][6]-test_data['decimalpoint_500'])/test_data['decimalpoint_500'])*100
test_data= test_data.drop(['sn500','decimalpoint_500'],axis=1)
test_data.rename(columns={'perc':'sn500','perc_DPA':'decimalpoint_500'},inplace = True)
test_data.drop(test_data.tail(1).index,inplace=True)
test_data['sn500']=test_data['sn500'].round(decimals=2)
test_data['decimalpoint_500']=test_data['decimalpoint_500'].round(decimals=2)
test_data.to_sql(name = 'returns_cube', con = conn, index=False, if_exists = 'append')
