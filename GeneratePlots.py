import time
import Database
import DataGenerator
import DataVisualization
import random
import sqlite3

def lineplot_code():
    Database.setup_database()
    DataGenerator.generate_data_for_lineplot()
    DataVisualization.visualize_data_lineplot()
    time.sleep(0)
    DataVisualization.close_figure()
    Database.clear_data_from_table()
    
def scatterplot_code():
    Database.setup_database()
    DataGenerator.generate_data_for_scatterplot()
    DataVisualization.visualize_data_scatterplot()
    time.sleep(0)
    DataVisualization.close_figure()
    Database.clear_data_from_table()
    
def Barchart_code():
    Database.setup_database()
    DataGenerator.generate_data_for_barchart()
    DataVisualization.visualize_data_barchart()
    time.sleep(0)
    DataVisualization.close_figure()
    Database.clear_data_from_table
    
def Barcharthorizontal_code():
    Database.setup_database()
    DataGenerator.generate_data_for_barchart_horizontal()
    DataVisualization.visualize_data_barchart_horizontal()
    time.sleep(0)
    DataVisualization.close_figure()
    Database.clear_data_from_table
    
def Histogram_code():
    Database.setup_database()
    DataGenerator.generate_data_for_histogram()
    DataVisualization.visualize_data_histogram()
    time.sleep(0)
    DataVisualization.close_figure()
    Database.clear_data_from_table()
    
def Boxplot_code():
    Database.setup_database()
    DataGenerator.generate_data_for_boxplot()
    DataVisualization.visualize_data_boxplot()
    time.sleep(0)
    DataVisualization.close_figure()
    Database.clear_data_from_table()
    
def Piechart_code():
    Database.setup_database()
    DataGenerator.generate_data_for_piechart()
    DataVisualization.visualize_data_piechart()
    time.sleep(0)
    DataVisualization.close_figure()
    Database.clear_data_from_table()
    
def AreaPlot_code():
    Database.setup_database()
    DataGenerator.generate_data_for_areaplot()
    DataVisualization.visualize_data_areaplot()
    time.sleep(0)
    DataVisualization.close_figure()
    Database.clear_data_from_table2()
    
def StackedBarChart_code():
    Database.setup_database()
    DataGenerator.generate_data_for_stackedbarchart()
    DataVisualization.visualize_data_stackedbarchart()
    time.sleep(0)
    DataVisualization.close_figure()
    Database.clear_data_from_table()
    
def Heatmap_code():
    Database.setup_database()
    DataGenerator.generate_data_for_heatmap()
    DataVisualization.visualize_data_heatmap()
    time.sleep(0)
    DataVisualization.close_figure()
    Database.clear_data_from_table()
    
def Contour_code():
    Database.setup_database()
    DataGenerator.generate_data_for_contourplot()
    DataVisualization.visualize_data_contourplot()
    time.sleep(0)
    DataVisualization.close_figure()
    Database.clear_data_from_table()
    
def Three_d_plot_code():
    Database.setup_database()
    DataGenerator.generate_data_for_3dplot()
    DataVisualization.visualize_data_3dplot()
    time.sleep(0)
    DataVisualization.close_figure()
    Database.clear_data_from_table()





