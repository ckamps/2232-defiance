import pandas as pd
import plotly.express as px

df = pd.read_csv(r'..\..\data\mo-river-data-2010-2024.csv')

fig = px.line(df, x = 'date', y = 'river-level', title='Missouri River Water Levels 2010-2024')
#fig.show()

fig.write_image(r'..\..\assets\img\river\river-levels.png', width=1800, height=800, scale=1)
