import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
from palmerpenguins import load_penguins
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
    ui.h2("Sidebar")  # (P2.2) Add a second-level header with the text "Sidebar"

    # (P2.1) Add a slider for filtering bill length data
    ui.input_slider(
        "slider", "Max Bill Length (mm)", min=33, max=60, value=45
    )  # Initial slider setup

    # (P2.3) Use ui.input_selectize() to create a dropdown input to choose a column
    ui.input_selectize(
        "selected_attribute",  # Name of the input
        "Choose an Attribute",  # Label for the input
        [
            "bill_length_mm",
            "bill_depth_mm",
            "flipper_length_mm",
            "body_mass_g",
        ],  # List of options
    )

    # (P2.4) Use ui.input_numeric() to create a numeric input for the number of Plotly histogram bins
    ui.input_numeric(
        "plotly_bin_count",  # Name of the input
        "Number of Plotly Bins",  # Label for the input
        value=10,  # Default value for the number of bins
    )

# Define layout with separate render_plotly outputs for vertical stacking
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

    @render_plotly
    def plot2():
        # Get the selected attribute from the dropdown input
        selected_attribute = input.selected_attribute()

        # Use the numeric input for setting bins in plot2
        bin_count = input.plotly_bin_count() if input.plotly_bin_count() else None

        # Create a second histogram based on the selected attribute
        fig = px.histogram(
            penguins,
            x=selected_attribute,
            title=f"Penguins {selected_attribute.replace('_', ' ').title()} Histogram",
            nbins=bin_count,  # Apply user-specified bin count to plot2
            color_discrete_sequence=["red"],  # Set bars to red
        )

        # Add black outline to each bar
        fig.update_traces(marker_line_color="black", marker_line_width=1.5)

        return fig


##### P2

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

