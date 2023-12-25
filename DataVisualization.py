import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
   
def visualize_data_lineplot():
    conn = sqlite3.connect('database.db')
    df = pd.read_sql_query("SELECT * FROM lineplot", conn)
    conn.close()

    plt.plot(df['xvalue'], df['yvalue'])
    plt.xlabel('xvalue')
    plt.ylabel('yvalue')
    plt.title('Data Visualization')

    #timer to close the figure
    plt.ion()
    plt.show()
    plt.pause(1)
    plt.close('all')
    
def visualize_data_scatterplot():
    conn = sqlite3.connect('database.db')
    df = pd.read_sql_query("SELECT * FROM scatterplot", conn)
    conn.close()

    plt.scatter(df['xvalue'], df['yvalue'], c='blue', alpha=0.5)  # Using scatter plot
    plt.xlabel('xvalue')
    plt.ylabel('yvalue')
    plt.title('Scatter Plot Visualization')
    plt.grid(True)  # Adding a grid
    plt.show()

    #timer to close the figure
    plt.ion()
    plt.show()
    plt.pause(1)
    plt.close('all')

def visualize_data_barchart():
    conn = sqlite3.connect('database.db')
    df = pd.read_sql_query("SELECT * FROM barchart", conn)
    conn.close()

    # Grouping the data by category and summing the values
    grouped_df = df.groupby('category').sum()

    plt.bar(grouped_df.index, grouped_df['value'])
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.title('Bar Chart Visualization')

    # Using plt.show() in non-blocking mode with a timer
    plt.ion()
    plt.show()
    plt.pause(5)  # Adjust the time as needed
    plt.close('all')

def visualize_data_barchart_horizontal():
    conn = sqlite3.connect('database.db')
    df = pd.read_sql_query("SELECT * FROM barchart", conn)
    conn.close()

    # Grouping the data by category and summing the values
    grouped_df = df.groupby('category').sum()

    plt.barh(grouped_df.index, grouped_df['value'])
    plt.ylabel('Category')
    plt.xlabel('Value')
    plt.title('Horizontal Bar Chart Visualization')

    # Using plt.show() in non-blocking mode with a timer
    plt.ion()
    plt.show()
    plt.pause(5)  # Adjust the time as needed
    plt.close('all')
    
def visualize_data_histogram():
    conn = sqlite3.connect('database.db')
    df = pd.read_sql_query("SELECT * FROM histogram", conn)
    conn.close()

    plt.hist(df['value'], bins=10, edgecolor='black')  # Adjust bins as needed
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram Visualization')
   
    #timer to close the figure
    plt.ion()
    plt.show()
    plt.pause(1)
    plt.close('all')
    
def visualize_data_boxplot():
    conn = sqlite3.connect('database.db')
    df = pd.read_sql_query("SELECT * FROM boxplot", conn)
    conn.close()

    # Group data by category and create a list of values for each category
    grouped_data = [group["value"].values for _, group in df.groupby("category")]

    plt.boxplot(grouped_data)
    plt.xticks(range(1, len(df['category'].unique()) + 1), df['category'].unique())
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.title('Box Plot Visualization')
    
    #timer to close the figure
    plt.ion()
    plt.show()
    plt.pause(1)
    plt.close('all')
    
def visualize_data_piechart():
    conn = sqlite3.connect('database.db')
    df = pd.read_sql_query("SELECT * FROM piechart", conn)  # Fetch data from the 'piechart' table
    conn.close()

    # The 'value' column contains the sizes of the pie slices
    # The 'category' column contains the labels for each slice
    plt.pie(df['value'], labels=df['category'], autopct='%1.1f%%', startangle=140)
    plt.title('Pie Chart Visualization')

    #timer to close the figure
    plt.ion()
    plt.show()
    plt.pause(1)
    plt.close('all')
    
def visualize_data_areaplot():
    conn = sqlite3.connect('database.db')
    df = pd.read_sql_query("SELECT * FROM areaplot", conn)  # Fetch from 'areaplot' table
    conn.close()

    plt.fill_between(df['xvalue'], df['yvalue'], color='skyblue', alpha=0.5)
    plt.xlabel('xvalue')
    plt.ylabel('yvalue')
    plt.title('Area Plot Visualization')

    # Show the plot
    plt.show()

    #timer to close the figure
    plt.ion()
    plt.show()
    plt.pause(1)
    plt.close('all')
    
def visualize_data_stackedbarchart():
    conn = sqlite3.connect('database.db')
    df = pd.read_sql_query("SELECT * FROM stackedbarchart", conn)  # Fetch data from the 'stackedbarchart' table
    conn.close()

    # Grouping the data by category
    grouped_df = df.groupby('category').sum()

    categories = grouped_df.index
    values1 = grouped_df['value1']
    values2 = grouped_df['value2']

    # Create a stacked bar chart
    plt.bar(categories, values1, label='Value 1')
    plt.bar(categories, values2, bottom=values1, label='Value 2')  # Stacking value2 on top of value1
    plt.xlabel('Category')
    plt.ylabel('Values')
    plt.title('Stacked Bar Chart Visualization')
    plt.legend()
    
     #timer to close the figure
    plt.ion()
    plt.show()
    plt.pause(1)
    plt.close('all')
    
def visualize_data_heatmap():
    conn = sqlite3.connect('database.db')
    df = pd.read_sql_query("SELECT * FROM heatmap", conn)  # Fetch data from the 'heatmap' table
    conn.close()

    # Create a grid for the heatmap
    grid_size = 11  # Adjust based on your data range
    grid = np.zeros((grid_size, grid_size))

    # Populate the grid with intensity values
    for _, row in df.iterrows():
        grid[int(row['x']), int(row['y'])] = row['value']  # Assumes x, y are integer grid coordinates

    plt.imshow(grid, cmap='hot', interpolation='nearest')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Heatmap Visualization')
    plt.colorbar()  # Add a color bar to indicate intensity levels

    #timer to close the figure
    plt.ion()
    plt.show()
    plt.pause(1)
    plt.close('all')
    
def visualize_data_contourplot():
    conn = sqlite3.connect('database.db')
    df = pd.read_sql_query("SELECT * FROM contourplot", conn)  # Fetch data from the 'contourplot' table
    conn.close()

    # Creating a structured grid
    grid_size = 10  # Change this based on your data
    x = np.linspace(0, grid_size, grid_size)
    y = np.linspace(0, grid_size, grid_size)
    X, Y = np.meshgrid(x, y)

    # Reshape DataFrame to match grid
    Z = df.pivot(index='y', columns='x', values='z').values

    # Create a contour plot
    plt.contourf(X, Y, Z, cmap='viridis')  # Use plt.contour for non-filled contours
    plt.colorbar()  # Add a color bar to indicate contour levels
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Contour Plot Visualization')


    #timer to close the figure
    plt.ion()
    plt.show()
    plt.pause(1)
    plt.close('all')

def visualize_data_3dplot():
    conn = sqlite3.connect('database.db')
    df = pd.read_sql_query("SELECT * FROM three_d_plot", conn)  # Fetch data from the 'threedplot' table
    conn.close()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(df['x'], df['y'], df['z'])  # Using scatter plot for 3D data
    ax.set_xlabel('X Value')
    ax.set_ylabel('Y Value')
    ax.set_zlabel('Z Value')
    ax.set_title('3D Plot Visualization')    
    plt.show()

    #timer to close the figure
    plt.ion()
    plt.show()
    plt.pause(1)
    plt.close('all')
    
def close_figure():
    plt.close('all')
    
