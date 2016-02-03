import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact, widgets, interactive
from IPython.display import display
import scipy
import pylab

def exploring_ride_counts_by_sex(data):
    x_widget = widgets.ToggleButtons(description='Gender:',options={'Female': ['Female'], 'Male':['Male'], 'Other':['Other'],
                                                                    'All':['Female','Male','Other']})
    y_widget = widgets.ToggleButtons(description='Date:',options={'Daily': 'dayofweek','Weekly': 'week',
                                                                  'Monthly': 'month'},)

    def plot_gender_date(x,y):
    #print(x)
    #print(y)

        fig1=data.groupby(getattr(data.index, y_widget.value))[x_widget.value[:]].mean().plot(marker='.',linestyle='none')
        fig1.axes.set_xlabel(''+ y_widget.value + '')
        fig1.axes.set_ylabel('Average number of riders')

    test=interact(plot_gender_date,x=x_widget,y=y_widget)
    
    return test


def exploring_weather_data_by_count_and_sex(data):

    x_widget = widgets.ToggleButtons(description='Gender:',options={'Female': ['Female'], 'Male':['Male'], 
                                                                    'Other':['Other'],'All':['Female','Male','Other']})
    #y_widget = widgets.ToggleButtons(description='Date:',options={'Daily': 'dayofweek','Weekly': 'week',
    #                                                              'Monthly': 'month'},)
    z_widget=widgets.ToggleButtons(description='Weather:',options={'Temperature': 'Mean_Temperature_F',
                                                                           'Precipitation': 'Precipitation_In ',
                                                                           'Humidity': 'Mean_Humidity ','Wind Speed':
                                                                           'Mean_Wind_Speed_MPH '},)

    def plot_weather_date(x,z):
        #print(x)
        #print(y)

        #fig1=data.groupby(x_widget.value)[z_widget.value].mean().plot()
        #fig1.axes.set_ylabel(z_widget.value)
        #fig1.axes.set_xlabel('Average number of riders')



        if (x_widget.value)==['Female','Male','Other']:
            ax = pylab.subplot(111)
            #figFemale=ax.scatter(data.groupby(getattr(data.index, y_widget.value))[z_widget.value].mean(), 
            #                     data.groupby(getattr(data.index, y_widget.value))[x_widget.value[0]].mean(), c='b')
            figFemale=ax.scatter(data[z_widget.value], data[x_widget.value[0]], c='b')
            figMale=ax.scatter(data[z_widget.value], data[x_widget.value[1]], c='r')
            figOther=ax.scatter(data[z_widget.value], data[x_widget.value[2]], c='y')

            plt.legend((figFemale,figMale,figOther),
               (x_widget.value[0], x_widget.value[1],x_widget.value[2]),
               scatterpoints=1,
               loc='upper left',
               ncol=3,)

            figFemale.axes.set_xlabel(''+ z_widget.value + '')
            figFemale.axes.set_ylabel('Daily number of riders')

        else:
            fig2=data.plot(kind='scatter', x=z_widget.value, y=x_widget.value, color='DarkBlue', label=z_widget.value)
            fig2.axes.set_xlabel(''+ z_widget.value + '')
            fig2.axes.set_ylabel('Daily number of riders')

    test=interact(plot_weather_date,x=x_widget,z=z_widget)
