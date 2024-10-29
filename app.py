import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
from palmerpenguins import load_penguins
from shinywidgets import output_widget, render_widget, render_plotly
import seaborn as sns
from shiny import render

# Load the palmerpenguins dataset
penguins = load_penguins()

# Set up the UI and layout
ui.page_opts(title="Penguins are Cool", fillable=True)

# (P2.1) Add a Shiny UI sidebar for user interaction
with ui.sidebar(
    open="open"
):  # (P2.1) Set open parameter to "open" to make sidebar open by default
    # (P2.1) Add a slider for filtering bill length data
    ui.input_slider(
        "slider", "Max Bill Length (mm)", min=33, max=60, value=45
    )  # Initial slider setup

# (P2.1) Define the layout columns
with ui.layout_columns():

    @render_plotly
    def plot1():
        # Filter the data based on the slider value
        filtered_penguins = penguins[
            penguins["bill_length_mm"] <= input.slider()
        ]  # Filter data dynamically

        # Create a histogram with black outlines
        fig = px.histogram(
            filtered_penguins,
            x="bill_length_mm",
            title="Penguins Bill Length Histogram",
        )

        # Add black outline to each bar
        fig.update_traces(marker_line_color="black", marker_line_width=1.5)

        return fig


##### P2

#  (P2.2) Use the ui.h2() function to add a 2nd level header to the sidebar
#  (P2.2) pass in a string argument (in quotes) to set the header text to "Sidebar"

#  (P2.3) Use ui.input_selectize() to create a dropdown input to choose a column
#  (P2.3) pass in three arguments:
#  (P2.3) the name of the input (in quotes), e.g., "selected_attribute"
#  (P2.3) the label for the input (in quotes)
#  (P2.3) a list of options for the input (in square brackets)
#  (P2.3)  e.g. ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]

#  (P2.4) Use ui.input_numeric() to create a numeric input for the number of Plotly histogram bins
#  (P2.4) pass in two arguments:
#  (P2.4) the name of the input (in quotes), e.g. "plotly_bin_count"
#  (P2.4) the label for the input (in quotes)

#  (P2.5) Use ui.input_slider() to create a slider input for the number of Seaborn bins
#  (P2.5) pass in four arguments:
#  (P2.5) the name of the input (in quotes), e.g. "seaborn_bin_count"
#  (P2.5) the label for the input (in quotes)
#  (P2.5) the minimum value for the input (as an integer)
#  (P2.5) the maximum value for the input (as an integer)
#  (P2.5) the default value for the input (as an integer)

#  (P2.6) Use ui.input_checkbox_group() to create a checkbox group input to filter the species
#  (P2.6) pass in five arguments:
#  (P2.6) the name of the input (in quotes), e.g.  "selected_species_list"
#  (P2.6) the label for the input (in quotes)
#  (P2.6) a list of options for the input (in square brackets) as ["Adelie", "Gentoo", "Chinstrap"]
#  (P2.6) a keyword argument selected= a list of selected options for the input (in square brackets)
#  (P2.6) a keyword argument inline= a Boolean value (True or False) as you like

#  (P2.7) Use ui.hr() to add a horizontal rule to the sidebar

#  (P2.8) Use ui.a() to add a hyperlink to the sidebar
#  (P2.8) pass in two arguments:
#  (P2.8) the text for the hyperlink (in quotes), e.g. "GitHub"
#  (P2.8) a keyword argument href= the URL for the hyperlink (in quotes), e.g. your GitHub repo URL
#  (P2.8) a keyword argument target= "_blank" to open the link in a new tab

# When passing in multiple arguments to a function, separate them with commas.
