import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
population_stdev = statistics.stdev(data)
print(population_mean)
print(population_stdev)

fig = ff.create_distplot([data],["population reading time"],show_hist = False)
fig.show()
'''
data_set = []
for i in range(0,100):
    randomindex = random.randint(0,len(data))
    value = data[randomindex]
    data_set.append(value)

mean_sample = statistics.mean(data_set)
stdev_sample = statistics.stdev(data_set)

print("Sample mean: ", mean_sample)
print("Sample stdev: ", stdev_sample)
'''

def randomsetofmean(counter):
    data_set = []
    for i in range(0,counter):
        randomindex = random.randint(0,len(data)-1)
        value = data[randomindex]
        data_set.append(value)
    mean = statistics.mean(data_set)
    return mean

def showfig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    print("mean of sampling distribution: ", mean)
    fig = ff.create_distplot([df],["sample reading time"],show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = 'lines', name = 'MEAN'))
    fig.show()

def standard_dev():
    meanlist = []
    for i in range(0,100):
        setofmeans = randomsetofmean(30)
        meanlist.append(setofmeans)
    standarddev = statistics.stdev(meanlist)
    print("standard deviation of sampling distribution: ", standarddev)

def setup():
    meanlist = []
    for i in range(0,100):
        setofmeans = randomsetofmean(30)
        meanlist.append(setofmeans)
    showfig(meanlist)

setup()
standard_dev()
