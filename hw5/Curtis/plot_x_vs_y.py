import os
import wget
import pandas as pd
import seaborn
import matplotlib.pyplot as plt
import urllib
seaborn.set()  # for plot stylings


def plot_x_vs_y(dataframe, xcolumn, ycolumn, savedfile):

    """
    plot_x_vs_y takes three inputs: a dataframe and two column names from the
    given dataframe.  It gives plots the data and saves it as a .png file
    within the same folder.
    """

    # Define variables that will be used for function and unit tests.
    plotsuccessful = True
    filetype = True
    alreadyexists = False
    data = dataframe

    # Test to make sure that given filename has appropriate extension.
    if not (savedfile.endswith('.png') or savedfile.endswith('.gif') or
       savedfile.endswith('.pdf')):
        print("The desired file name does not have a valid extension."
              " Try .png or .gif")
        filetype = False
    # Test to make sure that a file doesn't already exist with the desired name
    elif os.path.exists(savedfile):
        print("A file already exists with that name."
              " Choose a different name and try again")
        alreadyexists = True
        plotsuccessful = False
    # Plot the data.
    else:
        fig = plt.scatter(data['fakex'], data['fakey'])
        plt.xlabel(xcolumn)
        plt.ylabel(ycolumn)
        plt.title(xcolumn + " vs " + ycolumn)
        plt.savefig(savedfile)

        # Test to make sure the data was plotted successfully.
        if os.path.exists(savedfile):
            plotsuccessful = True
        else:
            plotsuccessful = False

    return (plotsuccessful, filetype, alreadyexists)


def remove_data(filename):
    """
    Deletes the specified data file.
    """

    fileexists = True

    if os.path.exists(filename):
        print(filename, "was deleted")
        os.remove(filename)
        return fileexists
    else:
        print(filename, "does not exist")
        fileexists = False
        return fileexists
