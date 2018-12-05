import datetime

from pymongo import MongoClient

#import matplotlib.pyplot as plt

#import pandas as pd

import plotly

import plotly.graph_objs as go



def genreport():

    uri = "mongodb://<put your access key here>"

    client = MongoClient(uri)

    db = client.devdb



    plotVal = []

    plotTime = []

    cursor = db.devcollection.find({})

    for plots in cursor:

        #print(plots)

        plotVal.append(plots['value'])

        plotTime.append(plots['currentTime'])

    plotly.offline.plot({

        "data": [go.Scatter(x=plotTime, y=plotVal)],

        "layout": go.Layout(title="Glucose Timeline")

    }, auto_open=False)


