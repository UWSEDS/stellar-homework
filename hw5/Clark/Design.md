## Component Design Specification for Use Cases
### initialize_pronto_tool
- **What it does:** Initializes pronto data analyst tool and prompts user for a command
- **Inputs:** User opens the program
- **Outputs:** User selections for program processes, prompt for user to select previous sessions
- **How it uses other components:** Calls grab_user_input to get the information that the user enters. Sends user input to other parts of the tool, such as plot_x_vs_y. Allows the user to load previous sessions by starting customize_input settings.
```python
if program_started:
    user_input = grab_user_input(user_input)
    file = customize_input_settings(filename, string)
    if file:
        #columns determined from user_input
        # ex. column_1 = user_input[ii]
        plot_x_vs_y(data_frame, column_1, column_2, filename)
    else:
        load data_frame
        plot_x_vs_y(data_frame, column_1, column_2, filename)
```
___
### grab_user_input
- **What it does:** Collects information that the user enters into the program and checks to see whether user input is valid
- **Inputs:** User input (string)
- **Outputs:** Error if string is not a valid option or returns user input if it is valid
- **How it uses other components:** Communicates with initialize_analyst_tool to collect user inputs
```python
def grab_user_input(user_input):
    column_1 = user_input[0]
    column_2 = user_input[1]
    data_frame = user_input[2]   
    filename = user_input[3]
    return column_1, column_2, data_frame, filename
```
___
### customize_input_settings
- **What it does:** Prompts user to load any previous sessions or saved work
- **Inputs:** User input (filename, string)
- **Outputs:** Name of file (string), calls function that will load the saved session
- **How it uses other components:** Prompted to open from initialize_analyst_tool. Sends request to open a session if user wants to reopen a saved session.  
```python
def customize_input_settings():
    #asks user if they would like to load an old session
    if yes:
        return session_filename
    if no:
        return data_frame from grab_user_input
```
___
### specify_output_format
- **What it does:** Allows user to specify the file format of plots or other data
- **Inputs:** User selection of file type (from dropdown list, Boolean)
- **Outputs:** Selection type (string)
- **How it uses other components:** Interacts with the save_output function to save the user data
```python
def specify_output_format(user response):
    #asks user if they would like to use a certain output format
    if yes:
        return user_specified_format
    if no:
        return default_format
```
___
### save_output
- **What it does:** Asks the user whether or not they would like to save plots or other outputs from the analyst tool
- **Inputs:** User selects the save option
- **Outputs:** Saved files in specified format
- **How it uses other components:** Uses the format option selected from specify_output_format
```python
def save_output():
    #asks user if they would like to save plots
    if yes:
        call specify_output_format()
        save figure
        return plot
    if no:
        return
```
___
### plot_x_vs_y
- **What it does:** Plots a user selected column again another user selected column
- **Inputs:** Columns user wants to plot (2 strings)
- **Outputs:** Plot
- **How it uses other components:** Uses the user input collected from the grab_user_input function. Works with save_output to save the data.
```python
Refer to plot_x_vs_y.py
```
