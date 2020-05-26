import numpy as np
import pandas as pd

 
import plotly
import plotly.express as px
import matplotlib.pylab as plt
 
import plotly.offline as pyo
import plotly.graph_objs as go
 
from plotly.subplots import make_subplots
 
import cufflinks as cf
 
cf.go_offline(connected=True)
 
import plotly.io as pio
 
pio.renderers.default = "notebook_connected"
 
import os
if not os.path.exists("images"):
 
    os.mkdir("images")
 
case = pd.read_csv('Case.csv')
patient_info = pd.read_csv('PatientInfo.csv')
patient_route = pd.read_csv('PatientRoute.csv')
time = pd.read_csv('Time.csv')
time_age = pd.read_csv('TimeAge.csv',)
time_gender = pd.read_csv('TimeGender.csv')
time_province = pd.read_csv('TimeProvince.csv')
region = pd.read_csv('Region.csv')
weather = pd.read_csv('Weather.csv')
trend = pd.read_csv('SearchTrend.csv')
 

 
def pie_chart(data, col, title = ''):
    cnt_df = data[col].value_counts().reset_index()
    fig = px.pie(cnt_df, 
                 values = col, 
                 names = 'index', 
                 title = title, 
                 template = 'seaborn',
                 color_discrete_sequence=px.colors.sequential.RdBu)
    fig.update_traces(rotation=90, pull=0.05, textinfo="value+percent+label")
    fig.show()
 

 
"""
print(case.head())

print(patient_info.head()) 
 
print(patient_route.head())

print(time.head())
 
print(time_age.head())

print(time_gender.head()) 

print(time_province.head())

print(region.head())
 
print(weather.head())
 
print(trend.head())
"""
 

 
# Now the number of confirmed data, more than 50 people
case2 = case[case['confirmed'] >= 50]
print(case2) 
case3 = pd.DataFrame(case2.groupby(['infection_case'])['confirmed'].max())
case3 = case3.sort_values(by=['confirmed'], ascending=False)
print(case3)
 

# The main route of infection rate visualization
fig = px.pie(case3, values='confirmed', names= case3.index,
                 title = "The main route of infection ")
fig.update_traces(textposition='inside', textinfo='percent+label')
 
fig.show()

fig = go.Figure()
 
fig.add_trace(go.Line(x=time.date, y=time.confirmed, mode='lines', name = 'confirmed embroidery over time', line = dict (color = 'orange')))

# Embroidery confirmed according to whether the outbreak
case_group = pd.DataFrame(case.groupby(['group'])['confirmed'].sum())
 
case_group

fig = go.Figure(go.Bar(x=case_group.index, y=case_group.confirmed, name = 'party confirmed according to whether outbreaks', marker_color = 'pink'))
fig.show()

# Embroidery average age-specific contacts
case_age = pd.DataFrame(patient_info.groupby(['age'])['contact_number'].mean())
 
# Missing values ​​are removed in a row (90 and 100)
case_age = case_age.dropna(axis=0)
print(case_age)

fig = go.Figure()
 
fig.add_trace(go.Line(x=case_age.index, y=case_age.contact_number, mode='lines', name = 'average age by contact embroidery', line = dict (color = 'blue')))
fig.show()

#trend Data visualization
fig = go.Figure(go.Line(x=trend.date, y=trend.cold, name = 'cold'))
fig.add_trace(go.Line(x=trend.date, y=trend.coronavirus, name = 'coronavirus'))
fig.add_trace(go.Line(x=trend.date, y=trend.pneumonia, name = 'pneumonia'))
fig.add_trace(go.Line(x=trend.date, y=trend.flu, name = 'flu'))

time['confirmed_test'] = time['confirmed'] / time['test']
 
print(time.head())
 
# Can be compared death confirmed
time['deceased_confirmed'] = time['deceased'] / time['confirmed']
 
print(time.tail())
 

fig = go.Figure()
 
fig.add_trace(go.Line(x=time.date, y=time.confirmed_test, mode='lines', name = 'test can be confirmed over'))
fig.add_trace(go.Line(x=time.date, y=time.deceased_confirmed, mode='lines', name = "deaths than could confirm "))

# Attempt by the elderly population
case_elder = pd.DataFrame(region.groupby(['province'])['elderly_population_ratio'].mean())
case_elder = case_elder.reset_index()
 
fig = px.bar(case_elder, x='province', y="elderly_population_ratio")
 
fig.show()
 
# Calculate the number of days treatment (day hospital - confirmed one)
patient_info['confirmed_date'] = pd.to_datetime(patient_info['confirmed_date'])
patient_info['released_date'] = pd.to_datetime(patient_info['released_date'])
patient_info['care'] = patient_info['released_date'] - patient_info['confirmed_date']
patient_info['care'] = pd.to_numeric(patient_info['care'].dt.days, downcast='integer')
 
print(patient_info.head())

 
# Age group the average number of days treatment
case_care_age = pd.DataFrame(patient_info.groupby(['age'])['care'].mean())
case_care_age = case_care_age.dropna(axis=0)
case_care_age = case_care_age.reset_index()
print(case_care_age)
 
fig = go.Figure()
 
fig.add_trace(go.Line(x=case_care_age.age, y=case_care_age.care, mode='lines', name = 'age group the average number of days treatment'))

 #trend data visualization
fig = go.Figure(go.Line(x=trend.date, y=trend.cold, name='감기'))
fig.add_trace(go.Line(x=trend.date, y=trend.coronavirus, name='코로나바이러스'))
fig.add_trace(go.Line(x=trend.date, y=trend.pneumonia, name='폐렴'))
fig.add_trace(go.Line(x=trend.date, y=trend.flu, name='독감'))

# Positive / Checked
time['confirmed_test'] = time['confirmed'] / time['test']
print(time.head())

# Dead / Positive
time['deceased_confirmed'] = time['deceased'] / time['confirmed']
print(time.tail())
fig.show()

fig = go.Figure()
fig.add_trace(go.Line(x=time.date, y=time.confirmed_test, mode='lines', name='Proportion of positive responders to coronavirus examiners'))
fig.add_trace(go.Line(x=time.date, y=time.deceased_confirmed, mode='lines', name='The proportion of deaths to positive patients'))

#Ratio of old mans
case_elder = pd.DataFrame(region.groupby(['province'])['elderly_population_ratio'].mean())
case_elder = case_elder.reset_index()

fig = px.bar(case_elder, x='province', y="elderly_population_ratio")
fig.show()

# The average number of days of treatment by age group
patient_info['confirmed_date'] = pd.to_datetime(patient_info['confirmed_date'])
patient_info['released_date'] = pd.to_datetime(patient_info['released_date'])
patient_info['care'] = patient_info['released_date'] - patient_info['confirmed_date']

patient_info['care'] = pd.to_numeric(patient_info['care'].dt.days, downcast='integer')
print(patient_info.head())

# The average number of days of treatment by age group
case_care_age = pd.DataFrame(patient_info.groupby(['age'])['care'].mean())
case_care_age = case_care_age.dropna(axis=0)
case_care_age = case_care_age.reset_index()
print(case_care_age)

fig = go.Figure()
fig.add_trace(go.Line(x=case_care_age.age, y=case_care_age.care, mode='lines', name='The average number of days of treatment by age group'))