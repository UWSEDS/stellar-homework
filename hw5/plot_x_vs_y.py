import os
import matplotlib.pyplot as plt

from pronto_utils import get_trips_and_weather


def plot_x_vs_y(dataframe, x, y, output_filename):
    """
    Creates a pdf of a scatterplot with the given x and y parameters
    from the input dataframe, notifies if a PDF file with designated name
    already exists, and saves the scatterplot to PDF if it doesn't exist
    """
    exists = False
    data = dataframe
    fig = plt.scatter(data[x], data[y])
    plt.xlabel('%s' % x)
    plt.ylabel('%s' % y)
    if os.path.isfile(output_filename+'.pdf') is True:
        print(output_filename, 'already exists as a PDF')
        exists = True
    else:
        plt.savefig(output_filename+'.pdf')
        print(output_filename, 'has been saved to a PDF')
    return (exists)
