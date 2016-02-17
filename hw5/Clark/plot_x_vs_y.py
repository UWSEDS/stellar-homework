"""
Creates a plot of column_1 versus column_2

Input arguments:
data_frame -- pandas data frame of pronto-data
column_1 -- data to be plotted on the x axis
column_2 -- data to be plotted on the y axis
output_filename -- name of the file that you would like to save the plot to

No output arguments.
"""

import pandas as pd
import matplotlib.pyplot as plt

def plot_x_vs_y(data_frame, column_1, column_2, output_filename):

    #Attempts to plot column_1 versus column_2 and then save the figure
    try:
        data_frame.plot(x=column_1, y=column_2)
        plt.savefig(output_filename)
        figure_saved = 'Figure ' + output_filename + ' successfully saved.'
        return figure_saved

    #Throws an error if the column names are incorrect or if the data frame is
    #   empty
    except KeyError:
        figure_not_saved = 'Please verify column names are correct.'
        return figure_not_saved
    except AttributeError:
        figure_not_saved = 'Please enter valid data frame.'
        return figure_not_saved
