import requests
from io import StringIO
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import datetime
from datetime import date

current_date = datetime.date.today()
previous_date = current_date - datetime.timedelta(days=1)
previous_date_formatted = previous_date.strftime("%Y-%m-%d")

url = f"https://waterdata.usgs.gov/nwis/dv?cb_00065=on&format=rdb&site_no=06935450&legacy=&referred_module=sw&period=&begin_date=2008-09-04&end_date={previous_date_formatted}"
response = requests.get(url)

if response.status_code == 200:
  # Convert the content to a StringIO object
  content = response.content.decode('utf-8')
  content_lines = content.split('\n')
    
  header_comments = []
  for line in content_lines:
    if line.startswith("#"):
      header_comments.append(line)
    else:
      break
    
  column_row_index = None
  for i, line in enumerate(content_lines):
    if line.startswith("agency_cd"):
      column_row_index = i
      break
    
  header = [line.strip() for line in content_lines[column_row_index].split('\t')]

  content_io = StringIO('\n'.join(content_lines[column_row_index+2:]))
  df = pd.read_csv(content_io, sep='\t', names=header)
    
  # print(df.head())  # Example: print the first few rows
else:
  print("Failed to download the file")

dmax = df[['datetime']].values.max()
dmin = df[['datetime']].values.min()

river_level_col = '75931_00065_30800'
fig = px.line(df, 
              x = 'datetime', 
              y = river_level_col, 
              labels={river_level_col: "MO river level (ft)"})

fig.update_layout(xaxis_title="")

fig.update_layout(title_text='Missouri River Water Levels 2010-2024', title_x=0.5)

#fig.update_xaxes(tickformat = '%Y-%B', dtick='M1')

fig.update_xaxes(
    ticklabelmode="period"
)

fig.add_vrect(x0="2010-12-21", x1="2011-03-19", 
              annotation_text="winter", annotation_position="bottom right",
              fillcolor="blue", opacity=0.10, line_width=0)
fig.add_vrect(x0="2011-12-21", x1="2012-03-19", 
              annotation_text="winter", annotation_position="bottom right",
              fillcolor="blue", opacity=0.10, line_width=0)
fig.add_vrect(x0="2012-12-21", x1="2013-03-19", 
              annotation_text="winter", annotation_position="bottom right",
              fillcolor="blue", opacity=0.10, line_width=0)
fig.add_vrect(x0="2013-12-21", x1="2014-03-19", 
              annotation_text="winter", annotation_position="bottom right",
              fillcolor="blue", opacity=0.10, line_width=0)
fig.add_vrect(x0="2014-12-21", x1="2015-03-19", 
              annotation_text="winter", annotation_position="bottom right",
              fillcolor="blue", opacity=0.10, line_width=0)
fig.add_vrect(x0="2015-12-21", x1="2016-03-19", 
              annotation_text="winter", annotation_position="bottom right",
              fillcolor="blue", opacity=0.10, line_width=0)
fig.add_vrect(x0="2016-12-21", x1="2017-03-19", 
              annotation_text="winter", annotation_position="bottom right",
              fillcolor="blue", opacity=0.10, line_width=0)
fig.add_vrect(x0="2017-12-21", x1="2018-03-19", 
              annotation_text="winter", annotation_position="bottom right",
              fillcolor="blue", opacity=0.10, line_width=0)
fig.add_vrect(x0="2018-12-21", x1="2019-03-19", 
              annotation_text="winter", annotation_position="bottom right",
              fillcolor="blue", opacity=0.10, line_width=0)
fig.add_vrect(x0="2019-12-21", x1="2020-03-19", 
              annotation_text="winter", annotation_position="bottom right",
              fillcolor="blue", opacity=0.10, line_width=0)
fig.add_vrect(x0="2020-12-21", x1="2021-03-19", 
              annotation_text="winter", annotation_position="bottom right",
              fillcolor="blue", opacity=0.10, line_width=0)
fig.add_vrect(x0="2021-12-21", x1="2022-03-19", 
              annotation_text="winter", annotation_position="bottom right",
              fillcolor="blue", opacity=0.10, line_width=0)
fig.add_vrect(x0="2022-12-21", x1="2023-03-19", 
              annotation_text="winter", annotation_position="bottom right",
              fillcolor="blue", opacity=0.10, line_width=0)
fig.add_vrect(x0="2023-12-21", x1="2024-03-19", 
              annotation_text="winter", annotation_position="bottom right",
              fillcolor="blue", opacity=0.10, line_width=0)

fig.add_trace(go.Scatter(y=[35.4,35.4], 
                         x=[dmin,dmax],
                         mode='lines', 
                         line=dict(color='red', width=2),
                         name='Flood 1993'))

fig.add_trace(go.Scatter(y=[30,30],
                         x=[dmin,dmax],
                         mode='lines',
                         line=dict(color='black', width=2),
                         name='Water touches bridge'))

fig.add_trace(go.Scatter(y=[22.6,22.6], 
                         x=[dmin,dmax],
                         mode='lines', 
                         line=dict(color='blue', width=2),
                         name='Lower land floods'))

fig.add_trace(go.Scatter(y=[7,7], 
                         x=[dmin,dmax],
                         mode='lines', 
                         line=dict(color='orange', width=2),
                         name='Paddle to river'))

fig.add_trace(go.Scatter(y=[5,5], 
                         x=[dmin,dmax],
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

#layout(legend = list(orientation = 'h', xanchor = "center", x = 0.5, y= 1)) 

#fig.show()

fig.write_image(r'../../assets/img/river/river-levels.png', width=1800, height=800, scale=1)
fig.write_json(r'../../static/json/river-levels.json')