import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
from palmerpenguins import load_penguins
import seaborn as sns
import matplotlib.pyplot as plt
from shiny import render

# Load the palmerpenguins dataset
penguins = load_penguins()

# Set up the UI and layout
ui.page_opts(title="Penguins are Cool", fillable=True)

# (P2.1) Add a Shiny UI sidebar for user interaction
with ui.sidebar(open="open"):
    ui.h2("Sidebar")

    # (P2.1) Slider for filtering bill length data
    ui.input_slider("slider", "Max Bill Length (mm)", min=33, max=60, value=45)

    # (P2.3) Dropdown to choose a column attribute
    ui.input_selectize(
        "selected_attribute",
        "Choose an Attribute",
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
    )

    # (P2.4) Numeric input for number of Plotly histogram bins
    ui.input_numeric("plotly_bin_count", "Number of Plotly Bins", value=10)

    #  (P2.5) Use ui.input_slider() to create a slider input for the number of Seaborn bins
    #  (P2.5) the minimum value for the input (as an integer)
    #  (P2.5) the maximum value for the input (as an integer)
    #  (P2.5) the default value for the input (as an integer)
    ui.input_slider(
        "seaborn_bin_count", "Number of Seaborn Bins", min=5, max=50, value=20
    )

# Define layout with render_plotly outputs for vertical stacking
with ui.layout_columns():

    @render_plotly
    def plot1():
        # Filter data based on slider value
        filtered_penguins = penguins[penguins["bill_length_mm"] <= input.slider()]

        # Plotly histogram for bill length
        fig = px.histogram(
            filtered_penguins,
            x="bill_length_mm",
            title="Penguins Bill Length Histogram",
        )
        fig.update_traces(marker_line_color="black", marker_line_width=1.5)
        return fig

    @render_plotly
    def plot2():
        # Get selected attribute and bin count for Plotly histogram
        selected_attribute = input.selected_attribute()
        bin_count = input.plotly_bin_count() if input.plotly_bin_count() else None

        # Plotly histogram for selected attribute
        fig = px.histogram(
            penguins,
            x=selected_attribute,
            title=f"Penguins {selected_attribute.replace('_', ' ').title()} Histogram",
            nbins=bin_count,
            color_discrete_sequence=["red"],
        )
        fig.update_traces(marker_line_color="black", marker_line_width=1.5)
        return fig


# Add the Seaborn histogram inside a card component
with ui.card():
    ui.card_header("Seaborn Histogram")

    #  (P2.5) the name of the input (in quotes), e.g. "seaborn_bin_count"
    #  (P2.5) the label for the input (in quotes)
    @render.plot
    def plot3():
        # Create Seaborn histogram using the selected attribute and bin count
        fig, ax = plt.subplots()
        sns.histplot(
            data=penguins,
            x=input.selected_attribute(),
            bins=input.seaborn_bin_count(),
            ax=ax,
        )
        ax.set_title("Penguins Bill Length")
        ax.set_xlabel(input.selected_attribute())
        ax.set_ylabel("Count")

        return fig


##### P2

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

