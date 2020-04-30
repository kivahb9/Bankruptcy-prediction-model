from django.shortcuts import render
import pandas as pd
from django.conf import settings
from sqlalchemy import create_engine
import numpy as np
import json
from datetime import datetime
import time
from dateutil.relativedelta import relativedelta


def index(request):
    engine = create_engine("mysql://root:admin@123@localhost:3306/creditpulse")
    constituent_data = pd.read_sql("index_price", engine)
    rs = constituent_data.groupby("date")["index_price"].agg("sum")
    sr = constituent_data.groupby("date")["credit_score_index_price"].agg("sum")
    index_price = list(rs.values)
    values = list(rs.index)
    date = []
    for j in values:
        orig_date = str(j)
        dt = datetime.strptime(orig_date, "%Y-%m-%d %H:%M:%S")
        date.append(dt.timestamp() * 1000)
    values = date
    indexprice = list(zip(values, index_price))
    indexprice = json.dumps(indexprice)
    credit_score_index_price = list(sr.values)
    credit_score_index_price_date = list(sr.index)
    credit_score_index_price_date = date
    creditscoreindexprice = list(
        zip(credit_score_index_price_date, credit_score_index_price)
    )
    creditscoreindexprice = json.dumps(creditscoreindexprice)
    table_content = constituent_data.to_html(index=None)
    table_content = table_content.replace("", "")
    table_content = table_content.replace(
        'class="dataframe"', "class='table table-striped'"
    )
    table_content = table_content.replace('border="1"', "")
    context = {"indexprice": indexprice, "creditscoreindexprice": creditscoreindexprice}
    return render(request, "creditdata/index.html", context=context)


def indexsquare(request):
    engine = create_engine("mysql://root:admin@123@localhost:3306/creditpulse")
    constituent_data = pd.read_sql("squared_index_price", engine)
    rs = constituent_data.groupby("date")["index_price"].agg("sum")
    sr = constituent_data.groupby("date")["credit_score_index_price"].agg("sum")
    index_price = list(rs.values)
    values = list(rs.index)
    date = []
    for j in values:
        orig_date = str(j)
        dt = datetime.strptime(orig_date, "%Y-%m-%d %H:%M:%S")
        date.append(dt.timestamp() * 1000)
    values = date
    indexprice = list(zip(values, index_price))
    indexprice = json.dumps(indexprice)
    credit_score_index_price = list(sr.values)
    credit_score_index_price_date = list(sr.index)
    credit_score_index_price_date = date
    creditscoreindexprice = list(
        zip(credit_score_index_price_date, credit_score_index_price)
    )
    creditscoreindexprice = json.dumps(creditscoreindexprice)
    table_content = constituent_data.to_html(index=None)
    table_content = table_content.replace("", "")
    table_content = table_content.replace(
        'class="dataframe"', "class='table table-striped'"
    )
    table_content = table_content.replace('border="1"', "")
    context = {"indexprice": indexprice, "creditscoreindexprice": creditscoreindexprice}
    return render(request, "creditdata/index.html", context=context)


def indexcube(request):
    engine = create_engine("mysql://root:admin@123@localhost:3306/creditpulse")
    constituent_data = pd.read_sql("cubed_index_price", engine)
    rs = constituent_data.groupby("date")["index_price"].agg("sum")
    sr = constituent_data.groupby("date")["credit_score_index_price"].agg("sum")
    index_price = list(rs.values)
    values = list(rs.index)
    date = []
    for j in values:
        orig_date = str(j)
        dt = datetime.strptime(orig_date, "%Y-%m-%d %H:%M:%S")
        date.append(dt.timestamp() * 1000)
    values = date
    indexprice = list(zip(values, index_price))
    indexprice = json.dumps(indexprice)
    credit_score_index_price = list(sr.values)
    credit_score_index_price_date = list(sr.index)
    credit_score_index_price_date = date
    creditscoreindexprice = list(
        zip(credit_score_index_price_date, credit_score_index_price)
    )
    creditscoreindexprice = json.dumps(creditscoreindexprice)
    table_content = constituent_data.to_html(index=None)
    table_content = table_content.replace("", "")
    table_content = table_content.replace(
        'class="dataframe"', "class='table table-striped'"
    )
    table_content = table_content.replace('border="1"', "")
    context = {"indexprice": indexprice, "creditscoreindexprice": creditscoreindexprice}
    return render(request, "creditdata/index.html", context=context)

