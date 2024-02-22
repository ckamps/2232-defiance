import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv(r'..\..\graph-data\river-data-2010-2024.csv')

dmax = df[['date']].values.max()
dmin = df[['date']].values.min()

fig = px.line(df, 
              x = 'date', 
              y = 'river-level', 
              labels={"river-level": "MO river level (ft)"},
              title='Missouri River Water Levels 2010-2024')

fig.add_trace(go.Scatter(y=[35.4,35.4], 
                         x=[dmin,dmax],
                         mode='lines', 
                         line=dict(color='black', width=3, dash='dash'),
                         name='Flood of 1993'))

fig.add_trace(go.Scatter(y=[29,29], 
                         x=[dmin,dmax],
                         mode='lines',
                         line=dict(color='red', width=3, dash='dash'),
                         name='Creek water touches bottom of bridge'))

fig.add_trace(go.Scatter(y=[24,24],
                         x=[dmin,dmax],
                         mode='lines', 
                         line=dict(color='orange', width=3, dash='dash'),
                         name='Lay down to pass under bridge'))

fig.add_trace(go.Scatter(y=[22.6,22.6], 
                         x=[dmin,dmax],
                         mode='lines', 
                         line=dict(color='yellow', width=3, dash='dash'),
                         name='Lower land starts flooding'))

fig.add_trace(go.Scatter(y=[7,7], 
                         x=[dmin,dmax],
                         mode='lines', 
                         line=dict(color='orange', width=3, dash='dash'),
                         name='Can paddle all the way to river'))

fig.add_trace(go.Scatter(y=[5,5], 
                         x=[dmin,dmax],
                         mode='lines', 
                         line=dict(color='green', width=3, dash='dash'),
                         name='Ready to paddle for 1 mile+ on creek'))

fig.update_layout(
        font=dict(size=20),
        legend=dict(font=dict(size=20)))

#fig.show()

fig.write_image(r'..\..\assets\img\river\river-levels.png', width=1800, height=800, scale=1)
