import pandas as pd 
import plotly.figure_factory as ff
import csv
df = pd.read_csv(r"/Users/anshul/Desktop/Class 108/data.csv")
x = df["Weight(Pounds)"].tolist()
fig = ff.create_distplot([x], ["weight"],show_hist=False)
fig.show()