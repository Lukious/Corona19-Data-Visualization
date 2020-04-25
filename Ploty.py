# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 18:49:25 2020

@author: BCML20
"""


import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import matplotlib.pylab as plt
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.io as pio

case = pd.read_csv('Case.csv')
patient_info = pd.read_csv('PatientInfo.csv')
patient_route = pd.read_csv('PatientRoute.csv')
policy = pd.read_csv('Policy.csv')
seoulfloating = pd.read_csv('SeoulFloating.csv')
time = pd.read_csv('Time.csv')
time_age = pd.read_csv('TimeAge.csv',)
time_gender = pd.read_csv('TimeGender.csv')
time_province = pd.read_csv('TimeProvince.csv')
region = pd.read_csv('Region.csv')
weather = pd.read_csv('Weather.csv')
trend = pd.read_csv('SearchTrend.csv')
timegender = pd.read_csv('TimeGender.csv')
timeprovince = pd.read_csv('TimeProvince.csv')

cleared = case[case['confirmed'] >= 50]
infect_path = pd.DataFrame(cleared.groupby(['infection_case'])['confirmed'].max())
infect_path = infect_path.sort_values(by=['confirmed'], ascending=False)

fig = px.pie(case3, values='confirmed', names= case3.index,
                 title='주요 감염경로')
fig.update_traces(textposition='inside', textinfo='percent+label')
#fig.show()

age20 = time_age['age'] == '20s' 
age30 = time_age['age'] == '30s' 
age40 = time_age['age'] == '40s' 
age50 = time_age['age'] == '50s' 
age60 = time_age['age'] == '60s' 
age70 = time_age['age'] == '70s' 
age80 = time_age['age'] == '80s' 
age90 = time_age['age'] == '90s' 

age20_data = time_age[age20]
age30_data = time_age[age30]
age40_data = time_age[age40]
age50_data = time_age[age50]
age60_data = time_age[age60]
age70_data = time_age[age70]
age80_data = time_age[age80]
age90_data = time_age[age90]
fig = go.Figure()
fig.add_trace(go.Line(x=age20_data.date, y=age20_data.confirmed, name='20s'))
fig.add_trace(go.Line(x=age30_data.date, y=age30_data.confirmed, name='30s'))
fig.add_trace(go.Line(x=age40_data.date, y=age40_data.confirmed, name='40s'))
fig.add_trace(go.Line(x=age50_data.date, y=age50_data.confirmed, name='50s'))
fig.add_trace(go.Line(x=age60_data.date, y=age60_data.confirmed, name='60s'))
fig.add_trace(go.Line(x=age70_data.date, y=age70_data.confirmed, name='70s'))
fig.add_trace(go.Line(x=age80_data.date, y=age80_data.confirmed, name='80s'))
fig.add_trace(go.Line(x=age90_data.date, y=age90_data.confirmed, name='90s'))
# fig.show()

recent = time_age['date'] == '2020-04-20'
recent_data = time_age[recent]

fig = px.pie(recent_data, values='confirmed', names= recent_data.age,
                 title='Distribution of Infected peoples age')
fig.show()





