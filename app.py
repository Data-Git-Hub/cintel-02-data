import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins

# (1.0) This package provides the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

# (1.0) Add a sidebar for user interaction
ui.page_opts(title="Penguins are Cool", fillable=True)

# (P2.1) Correct use of the layout with a sidebar
with ui.layout_sidebar():
    # (P2.1)Sidebar content
    with ui.sidebar(open="open"):
        # (P2.2) Add a second-level header inside the sidebar
        ui.h2("Sidebar")  # <-- Added this line for the 2nd level header

        # (P2.1) Add input controls inside the sidebar
        ui.input_slider("num_bins", "Number of bins", min=10, max=50, value=20)
        ui.input_checkbox("show_tips", "Show tips data", value=True)

        # (P2.3) Add first dropdown input using input_selectize() for plot1
        ui.input_selectize(
            "selected_attribute_1",  # (P2.3) Name of the input for plot1
            "Choose an attribute for Plot 1",  # (P2.3) Label for the input
            [
                "bill_length_mm",
                "bill_depth_mm",
                "flipper_length_mm",
                "body_mass_g",
            ],  # (P2.3) List of options for the dropdown
        )

        # (P2.3) Add second dropdown input using input_selectize() for plot2
        ui.input_selectize(
            "selected_attribute_2",  # (P2.3) Name of the input for plot2
            "Choose an attribute for Plot 2",  # (P2.3) Label for the input
            [
                "bill_length_mm",
                "bill_depth_mm",
                "flipper_length_mm",
                "body_mass_g",
            ],  # (P2.3) List of options for the dropdown
        )

        # (P2.4) Add a numeric input for the number of Plotly histogram bins
        ui.input_numeric(
            "plotly_bin_count",  # (P2.4) Name of the input
            "Number of bins for histograms",
            20,  # <-- Set a default value of 20 for plotly_bin_count
        )

    # (P2.1) Main layout (content area next to the sidebar)
    with ui.layout_columns():

        @render_plotly
        def plot1():
            # Handle cases where the numeric input might be None or invalid
            bin_count = (
                input.plotly_bin_count() or 20
            )  # Set a fallback default value of 20
            if input.show_tips():
                return px.histogram(
                    px.data.tips(),
                    y="tip",
                    nbins=bin_count,
                    color_discrete_sequence=[
                        "blue"
                    ],  # Blue color for the first histogram
                    histnorm="",
                    opacity=0.75,
                ).update_traces(marker_line_color="black", marker_line_width=1.5)
            else:
                return px.histogram(
                    penguins_df,
                    x=input.selected_attribute_1(),
                    nbins=bin_count,
                    color_discrete_sequence=[
                        "blue"
                    ],  # Blue color for the first histogram
                    histnorm="",
                    opacity=0.75,
                ).update_traces(marker_line_color="black", marker_line_width=1.5)

        @render_plotly
        def plot2():
            # Handle cases where the numeric input might be None or invalid
            bin_count = (
                input.plotly_bin_count() or 20
            )  # Set a fallback default value of 20
            if input.show_tips():
                return px.histogram(
                    px.data.tips(),
                    y="total_bill",
                    nbins=bin_count,
                    color_discrete_sequence=[
                        "red"
                    ],  # Red color for the second histogram
                    histnorm="",
                    opacity=0.75,
                ).update_traces(marker_line_color="black", marker_line_width=1.5)
            else:
                return px.histogram(
                    penguins_df,
                    x=input.selected_attribute_2(),
                    nbins=bin_count,
                    color_discrete_sequence=[
                        "red"
                    ],  # Red color for the second histogram
                    histnorm="",
                    opacity=0.75,
                ).update_traces(marker_line_color="black", marker_line_width=1.5)



######## P2 Requirements


# Use ui.input_slider() to create a slider input for the number of Seaborn bins
#   pass in four arguments:
#   the name of the input (in quotes), e.g. "seaborn_bin_count"
#   the label for the input (in quotes)
#   the minimum value for the input (as an integer)
#   the maximum value for the input (as an integer)
#   the default value for the input (as an integer)

# Use ui.input_checkbox_group() to create a checkbox group input to filter the species
#   pass in five arguments:
#   the name of the input (in quotes), e.g.  "selected_species_list"
#   the label for the input (in quotes)
#   a list of options for the input (in square brackets) as ["Adelie", "Gentoo", "Chinstrap"]
#   a keyword argument selected= a list of selected options for the input (in square brackets)
#   a keyword argument inline= a Boolean value (True or False) as you like

# Use ui.hr() to add a horizontal rule to the sidebar

# Use ui.a() to add a hyperlink to the sidebar
#   pass in two arguments:
#   the text for the hyperlink (in quotes), e.g. "GitHub"
#   a keyword argument href= the URL for the hyperlink (in quotes), e.g. your GitHub repo URL
#   a keyword argument target= "_blank" to open the link in a new tab

# When passing in multiple arguments to a function, separate them with commas.
