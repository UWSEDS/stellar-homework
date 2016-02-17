import matplotlib.pyplot as plt


def plot_x_vs_y(data, xcol, ycol, outputFileName):
    """
    Creates a plot of the two specified columns from the input data
    frame and saves the plot to a PDF file
    """

    # create a string for the output file name
    fileName = outputFileName + '.pdf'

    try:
        data.plot(kind='scatter', x=xcol, y=ycol)
        plt.title(xcol + ' vs. ' + ycol)
        plt.savefig(fileName)
        print('Success! Plot created and saved as ' + fileName)
    # if either of the column names does not belong to the data frame,
    # throw an exception
    except KeyError as e:
        print('Plot not created! Invalid column name(s): ' + str(e))
        print('Please make sure column names exist in the data frame')
