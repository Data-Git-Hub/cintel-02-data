import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
# (1.0) This package provides the Palmer Penguins dataset
import palmerpenguins

# (1.0) Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

ui.page_opts(title="Penguins are Cool", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")
