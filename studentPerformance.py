import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import random

df=pd.read_csv("StudentsPerformance.csv")
data=df["reading score"].tolist()
mean=statistics.mean(data)
mode=statistics.mode(data)
median=statistics.median(data)
std_dev=statistics.stdev(data)

first_std_dev_start,first_std_dev_end=mean-std_dev,mean+std_dev
second_std_dev_start,second_std_dev_end=mean-(std_dev*2),mean+(std_dev*2)
third_std_dev_start,third_std_dev_end=mean-(std_dev*3),mean+(std_dev*3)

fig=ff.create_distplot([data],["reading score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_std_dev_start,first_std_dev_start],y=[0,0.17],mode="lines",name="first_std_dev_start"))
fig.add_trace(go.Scatter(x=[first_std_dev_end,first_std_dev_end],y=[0,0.17],mode="lines",name="first_std_dev_end"))

fig.add_trace(go.Scatter(x=[second_std_dev_start,second_std_dev_start],y=[0,0.17],mode="lines",name="second_std_dev_start"))
fig.add_trace(go.Scatter(x=[second_std_dev_end,second_std_dev_end],y=[0,0.17],mode="lines",name="second_std_dev_end"))

fig.show()

print("Mean is", mean)
print("Median is", median)
print("Mode is", mode)
print("Standard Deviation is", std_dev)

listOfDataWithinOneStdDev=[result for result in data if result > first_std_dev_start and result < first_std_dev_end]
print("{}% of data lies within one standard deviation".format(len(listOfDataWithinOneStdDev)*100.0/len(data)))

listOfDataWithinTwoStdDev=[result for result in data if result > second_std_dev_start and result < second_std_dev_end]
print("{}% of data lies within two standard deviation".format(len(listOfDataWithinTwoStdDev)*100.0/len(data)))

listOfDataWithinThreeStdDev=[result for result in data if result > third_std_dev_start and result < third_std_dev_end]
print("{}% of data lies within three standard deviation".format(len(listOfDataWithinThreeStdDev)*100.0/len(data)))