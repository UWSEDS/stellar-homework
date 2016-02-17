# Pronto_Data_Analyst_Tool_v1.0

>The Pronto Data Analyst Tool (PDAT) is a compact toolbox to explore the Pronto! CycleShare dataset in Seattle, WA.  It has a wide source of tools to create interactive plots to explore trends involving time, weather, age, gender and more.  The functions created so far are listed below.

### plot_x_vs_y
A simple plotting function that plots one column of data against another.  Saves data as a .gif, .png, or .pdf file.  Checks to make sure that the desired filename isn't a dupliate and that it is has a valid extension.

Inputs: 

* dataset (panda dataframe with at least two columns)
* xcolumn (column to be x-axis)
* ycolumn (column to be y-axis)
* filename (.gif, .png, or .pdf file)

```sh
if filename not endswith ".gif" or ".png" or ".pdf",
    print "Not a valid extension."
elif filename already exists,
    print "A file with that name already exists."
else,
    plot xcolumn vs ycolumn
    save as filename
```
### calculate_averages_over_time
Takes a time-dependent dataset and outputs the average over a specified time interval e.g. take duration of ride data and find weekly averages of ride duration. Outputs dataset as a two-column dataframe.

Inputs:

* dataset (panda dataframe with a time column and at least one other column)
* timecolumn (column in DatetimeIndex format)
* ycolumn (column of time-dependent data)
* timeunits (time unit to be averaged over e.g. hours, days, weeks)

```sh
if ycolumn is not numerical,
    print "Data is not numerical."
elif timecolumn is note time data,
    print "Given column is not a time dataset."
else,
    group ycolumn by timeunits
    output average
```


### calculate_sums_over_time
Takes a time-dependent dataset and outputs the sum over a specified time interval e.g. take single ride events and compile into daily sums. Outputs dataset as a two-column dataframe.

Inputs:

* dataset (panda dataframe with a time column and at least one other column)
* timecolumn (column in DatetimeIndex format)
* ycolumn (column of time-dependent data)
* timeunits (time unit to be averaged over e.g. hours, days, weeks)

```sh
if ycolumn is not numerical,
    print "Data is not numerical."
elif timecolumn is note time data,
    print "Given column is not a time dataset."
else,
    group ycolumn by timeunits
    output sum
```

### calculate_stdevs_over_time
Takes a time-dependent dataset and outputs the standard deviation from the average over a specified time interval. Outputs dataset as a two-column dataframe.

Inputs:

* dataset (panda dataframe with a time column and at least one other column)
* timecolumn (column in DatetimeIndex format)
* ycolumn (column of time-dependent data)
* timeunits (time unit to be averaged over e.g. hours, days, weeks)

```sh
if ycolumn is not numerical,
    print "Data is not numerical."
elif timecolumn is note time data,
    print "Given column is not a time dataset."
else,
    group ycolumn by timeunits
    output stdev
```

### merge_data_files
Takes two datasets with the same indices and length and merges them together.  If indices or length do not match, it does not attempt the merge. Outputs a pandas dataframe with a single index. 

Inputs:

* dataset1 (panda dataframe)
* dataset2 (panda dataframe)

```sh
if rows(dataset1) != rows(dataset2),
    print "Datasets are not compatible."
else,
    merge datasets
```



