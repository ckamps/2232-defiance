import requests
from io import StringIO
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date, timedelta

current_date = date.today()
previous_date = current_date - timedelta(days=1)
previous_date_formatted = previous_date.strftime("%Y-%m-%d")

url = f"https://waterdata.usgs.gov/nwis/dv?cb_00065=on&format=rdb&site_no=06935450&legacy=&referred_module=sw&period=&begin_date=2008-09-04&end_date={previous_date_formatted}"
response = requests.get(url)

if response.status_code == 200:
  content = response.content.decode('utf-8')
  content_lines = content.split('\n')
    
  #header_comments = []
  #for line in content_lines:
  #  if line.startswith("#"):
  #    header_comments.append(line)
  #  else:
  #    break
    
  #column_row_index = None
  #for i, line in enumerate(content_lines):
  #  if line.startswith("agency_cd"):
  #    column_row_index = i
  #    break
    
  #header = [line.strip() for line in content_lines[column_row_index].split('\t')]
  #print(header)

  content_io = StringIO('\n'.join(content_lines[0:]))
  #df = pd.read_csv(content_io, sep='\t', names=header)

  df = pd.read_csv(content_io, sep='\t', skiprows=2, header=0, comment='#',
                 names=['agency_cd', 'site_no', 'datetime', '75931_00065_30800', '75931_00065_30800_cd'], 
                 parse_dates=['datetime'])
else:
  print("Failed to download the file")

df['datetime'] = df['datetime'].dt.date

print(df['datetime'])
#df['datetime'] = df['datetime'].dt.date
#df['date'] = pd.to_datetime(df['datetime'], format='%Y-%m-%d')
#print(df['date'])
dmax = df['datetime'].max()
dmin = df['datetime'].min()
print(dmin)
print(dmax)

river_level_col = '75931_00065_30800'
fig = px.line(df, 
        x = 'datetime', 
        y = river_level_col, 
        labels={river_level_col: "MO river level (ft)"})

# Get MO river forecast water level at Washington MO

url = "https://api.water.noaa.gov/nwps/v1/gauges/whgm7/stageflow"
response = requests.get(url)
 
if response.status_code == 200:
    data = response.json()
    forecast_data = data['forecast']['data']
    df_forecast = pd.DataFrame(forecast_data, columns=['validTime', 'primary'])
    fig.add_trace(go.Scatter(x=df_forecast['validTime'], y=df_forecast['primary'], mode='lines',line=dict(color='red', dash='dash'), name='Forecast'))
    dmax_forecast = df_forecast['validTime'].max()
else:
    print("Failed to fetch data")

fig.update_layout(xaxis_title="")

fig.update_layout(title_text='Missouri River Water Levels 2008-2024', title_x=0.5)

fig.update_xaxes(
    ticklabelmode="period"
)

winter_seasons = []
for year in range(dmin.year, dmax.year):
  start_date = pd.to_datetime(f"{year}-12-21")
  end_date = pd.to_datetime(f"{year + 1}-03-19")
  winter_seasons.append((start_date, end_date))

for winter_start, winter_end in winter_seasons:
  fig.add_vrect(
    x0=winter_start, 
    x1=winter_end,
    annotation_text="winter",
    annotation_position="bottom right",
    fillcolor="blue", 
    opacity=0.1,
    layer="below", 
    line_width=0
  )

fig.add_trace(go.Scatter(y=[35.4,35.4], 
                         x=[dmin,dmax_forecast],
                         mode='lines', 
                         line=dict(color='red', width=2),
                         name='Flood of 1993'))

fig.add_trace(go.Scatter(y=[30,30],
                         x=[dmin,dmax_forecast],
                         mode='lines',
                         line=dict(color='black', width=2),
                         name='Water touches underside of bridge'))

fig.add_trace(go.Scatter(y=[22.6,22.6], 
                         x=[dmin,dmax_forecast],
                         mode='lines', 
                         line=dict(color='blue', width=2),
                         name='Edge of lower land starts to flood'))

fig.add_trace(go.Scatter(y=[7,7], 
                         x=[dmin,dmax_forecast],
                         mode='lines', 
                         line=dict(color='orange', width=2),
                         name='Paddle to river'))

fig.add_trace(go.Scatter(y=[5,5], 
                         x=[dmin,dmax_forecast],
                         mode='lines', 
                         line=dict(color='green', width=2),
                         name='Paddle access'))

fig.update_layout(
        font=dict(size=8),
        legend=dict(
          font=dict(size=8),
          orientation="h",
          xanchor="center",
          yanchor="top",
          y=-0.05,
          x=0.5))

fig.write_image(r'../../assets/img/river/river-levels.png', width=1800, height=800, scale=1)
fig.write_json(r'../../static/json/river-levels.json')
