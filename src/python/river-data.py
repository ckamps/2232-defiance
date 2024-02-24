import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
from dateutil.rrule import rrule, MONTHLY

df = pd.read_csv(r'..\..\graph-data\river-data-2010-2024.csv')

df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

dmax = df[['date']].values.max()
dmin = df[['date']].values.min()

print(dmin)
print(dmax)

fig = px.line(df, 
              x = 'date', 
              y = 'river-level', 
              labels={"river-level": "MO river level (ft)"})

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
fig.add_vrect(x0="2023-12-21", x1=dmax, 
              annotation_text="winter", annotation_position="bottom right",
              fillcolor="blue", opacity=0.10, line_width=0)

fig.add_trace(go.Scatter(y=[35.4,35.4], 
                         x=[dmin,dmax],
                         mode='lines', 
                         line=dict(color='red', width=1),
                         name='Flood 1993'))

fig.add_trace(go.Scatter(y=[31,31], 
                         x=[dmin,dmax],
                         mode='lines',
                         line=dict(color='black', width=1),
                         name='Water touches bridge'))

fig.add_trace(go.Scatter(y=[22.6,22.6], 
                         x=[dmin,dmax],
                         mode='lines', 
                         line=dict(color='yellow', width=1),
                         name='Lower land floods'))

fig.add_trace(go.Scatter(y=[7,7], 
                         x=[dmin,dmax],
                         mode='lines', 
                         line=dict(color='orange', width=1),
                         name='Paddle to river'))

fig.add_trace(go.Scatter(y=[5,5], 
                         x=[dmin,dmax],
                         mode='lines', 
                         line=dict(color='green', width=1),
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

fig.write_image(r'..\..\assets\img\river\river-levels.png', width=1800, height=800, scale=1)
fig.write_json(r'..\..\static\json\river-levels.json')