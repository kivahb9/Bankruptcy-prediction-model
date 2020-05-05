import plotly
import chart_studio
import chart_studio.plotly as py
import plotly.graph_objs as go
from  plotly.offline import plot
from plotly.offline import init_notebook_mode, iplot

import MySQLdb
import pandas as pd
conn = MySQLdb.connect(host="localhost", user="root", passwd="admin@123", db="creditpulse")
cursor = conn.cursor()
cursor.execute('SELECT * FROM creditpulse.creditdata_testingdata');
rows = cursor.fetchall()
df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'id', 1: 'Date', 2: 'index_price', 3: 'credit_score_index_price'}, inplace=True);
df = df.sort_values(['id'], ascending=[1]);
del df['id']

trace_high = go.Scatter(
    x=df['Date'],
    y=df['index_price'],
    name = "index_price",
    line = dict(color = ('rgb(22, 96, 167)')),
    opacity = 0.8)

trace_low = go.Scatter(
    x=df['Date'],
    y=df['credit_score_index_price'],
    name = "credit_score_index_price",
    line = dict(color = ('rgb(205, 12, 24)')),
    opacity = 0.8)

data = [trace_high,trace_low]

layout = dict(
    title='Time Series with Rangeslider',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                     label='1y',
                     step='year',
                     stepmode='backward'),
                dict(count=5,
                     label='5y',
                     step='year',
                     stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
    )
)

fig = dict(data=data, layout=layout)
plotly.offline.iplot(fig, filename = "Time Series with Rangeslider")
