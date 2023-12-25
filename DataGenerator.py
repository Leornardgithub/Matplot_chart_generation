import sqlite3
import random
import numpy as np

def generate_data_for_lineplot():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    yvalue = 1  # Starting point for yvalue
    for i in range(100):  # Generate 100 data points
        xvalue = i  # Assuming xvalue is sequential
        fluctuation = random.randint(-10, 10)  # Random fluctuation
        yvalue += fluctuation  # Apply fluctuation

        # Optional: Keep yvalue within certain bounds
        yvalue = max(0, min(yvalue, 100))

        cursor.execute("INSERT INTO lineplot (xvalue, yvalue) VALUES (?, ?)", (xvalue, yvalue))

    conn.commit()
    conn.close()
    
def generate_data_for_scatterplot():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    for i in range(100):  # Generate 100 data points
        xvalue = random.randint(0, 100)
        yvalue = random.randint(0, 100)
        cursor.execute("INSERT INTO scatterplot (xvalue, yvalue) VALUES (?, ?)", (xvalue, yvalue))

    conn.commit()
    conn.close()

    
def generate_data_for_barchart():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']  # Example categories

    for i in range(100):  # Generate 100 data points
        category = random.choice(categories)  # Randomly choose a category
        value = random.randint(0, 100)  # Value for the bar
        cursor.execute("INSERT INTO barchart (category, value) VALUES (?, ?)", (category, value))

    conn.commit()
    conn.close()
    
def generate_data_for_barchart_horizontal():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']  # Example categories

    for i in range(100):  # Generate 100 data points
        category = random.choice(categories)  # Randomly choose a category
        value = random.randint(0, 100)  # Value for the bar
        cursor.execute("INSERT INTO barchart_horizontal (category, value) VALUES (?, ?)", (category, value))

    conn.commit()
    conn.close()       
    
def generate_data_for_histogram():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    for i in range(100):  # Generate 100 data points
        value = random.randint(0, 100)  # Generate a single value for the histogram
        cursor.execute("INSERT INTO histogram (value) VALUES (?)", (value,))

    conn.commit()
    conn.close()

def generate_data_for_boxplot():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']  # Example categories

    for i in range(100):  # Generate 100 data points
        category = random.choice(categories)
        value = random.randint(0, 100)  # Generate a single value for the box plot
        cursor.execute("INSERT INTO boxplot (category, value) VALUES (?, ?)", (category, value))

    conn.commit()
    conn.close()
    
def generate_data_for_piechart():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']  # Example categories

    for i in range(5):  # Generate data points for each category
        category = categories[i]
        value = random.randint(0, 100)  # Generate a value for the pie chart
        cursor.execute("INSERT INTO piechart (category, value) VALUES (?, ?)", (category, value))

    conn.commit()
    conn.close()
    
def generate_data_for_areaplot():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    for i in range(100):  # Generate 100 data points
        xvalue = i  # Increment xvalue sequentially
        yvalue = random.randint(0, 100)  # Generate yvalue
        cursor.execute("INSERT INTO areaplot (xvalue, yvalue) VALUES (?, ?)", (xvalue, yvalue))

    conn.commit()
    conn.close()

def generate_data_for_stackedbarchart():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']  # Example categories

    for i in range(20):  # Generate 20 sets of data points
        category = categories[i % len(categories)]  # Cycle through the categories
        value1 = random.randint(0, 100)  # First value for the stacked bar
        value2 = random.randint(0, 100)  # Second value for the stacked bar
        cursor.execute("INSERT INTO stackedbarchart (category, value1, value2) VALUES (?, ?, ?)", (category, value1, value2))

    conn.commit()
    conn.close()
    
def generate_data_for_heatmap():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    for i in range(100):  # Generate 100 data points
        xvalue = random.randint(0, 10)  # Assuming a 10x10 grid for the heatmap
        yvalue = random.randint(0, 10)
        intensity = random.randint(1, 100)  # Intensity value
        cursor.execute("INSERT INTO heatmap (x, y, value) VALUES (?, ?, ?)", (xvalue, yvalue, intensity))

    conn.commit()
    conn.close()
    
def generate_data_for_contourplot():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Assuming a 10x10 grid for the contour plot
    grid_size = 10
    for x in range(grid_size):
        for y in range(grid_size):
            z = np.sin(np.sqrt(x**2 + y**2)) + random.uniform(-0.5, 0.5)  # Example z-value calculation
            cursor.execute("INSERT INTO contourplot (x, y, z) VALUES (?, ?, ?)", (x, y, z))

    conn.commit()
    conn.close()
 
def generate_data_for_3dplot():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    for i in range(100):  # Generate 100 data points
        xvalue = random.randint(0, 100)
        yvalue = random.randint(0, 100)
        zvalue = random.randint(0, 100)  # Generate z-value
        cursor.execute("INSERT INTO three_d_plot (x, y, z) VALUES (?, ?, ?)", (xvalue, yvalue, zvalue))

    conn.commit()
    conn.close()
    
