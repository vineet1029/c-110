import pandas as pd
import plotly.figure_factory as pff
import random as ran
import statistics as std
df = pd.read_csv('medium_data.csv')
read = df['reading_time'].tolist()

finalList = []
def f1sam():
    sd = []
    for i in range(0,100):
        pos = ran.randint(0, len(read)-1)
        data = read[pos]
        sd.append(data)
    mean = std.mean(sd)
    finalList.append(mean)

for a in range(0,1000):
    f1sam()

graph = pff.create_distplot([finalList],['reading_time'], show_hist=False)
graph.show()